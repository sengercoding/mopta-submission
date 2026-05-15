import json
import os
import re
import sys
import pandas as pd
 
solution_path = "solution.csv"
routes_path   = "routes.csv"
excel_path    = "AIMMS-MOPTA Interfor data.xlsx"
 
for f, label in [(solution_path, "solution"), (routes_path, "routes"), (excel_path, "Excel input")]:
    if not os.path.exists(f):
        print(f"ERROR: {label} file not found: {f}")
        sys.exit(1)
 
print(f"Reading solution:  {solution_path}")
print(f"Reading routes:    {routes_path}")
print(f"Reading Excel:     {excel_path}")
 
with open(solution_path, "r", encoding="utf-8-sig") as f:
    content = f.read()
 
lines = content.split("\n")
active_ids = set()
for line in lines:
    m = re.match(r"\s+(\S+)\s+1\s+NonBasic", line)
    if m:
        active_ids.add(str(m.group(1)).strip("'"))
 
total_cost_match = re.search(r"total_cost\s*:=\s*([\d.]+)", content)
total_cost = float(total_cost_match.group(1)) if total_cost_match else None
 
print(f"  Active variable IDs found: {len(active_ids)}")
if total_cost:
    print(f"  Total cost from solution:  ${total_cost:,.2f}")
 
routes_df = pd.read_csv(
    routes_path,
    dtype={"route_id": str, "order1": str, "order2": str, "order3": str}
)
routes_df["route_id"] = routes_df["route_id"].str.strip()
 
xl          = pd.read_excel(excel_path, sheet_name=None)
ships       = xl["Shipments"].copy()
lanes       = xl["Lanes"].copy()
carriers_xl = xl["Carriers"].copy()
 
ships["OrderID"]     = ships["Order Number"].astype(str)
ships["Origin"]      = ships["Origin"].str.upper()
ships["Destination"] = ships["Destination"].str.upper()
lanes["Origin"]      = lanes["Origin"].str.upper()
lanes["Destination"] = lanes["Destination"].str.upper()
 
lane_open = {
    (r["Origin"], r["Destination"]): float(r["Total Cost"])
    for _, r in lanes.iterrows()
}
ships["OpenMarketCost"] = ships.apply(
    lambda r: lane_open.get((r["Origin"], r["Destination"]),
              lane_open.get((r["Destination"], r["Origin"]), 0.0)), axis=1
)
 
all_carrier_names = list(carriers_xl["Carrier"].astype(str))
 
route_id_set    = set(routes_df["route_id"])
active_routes   = routes_df[routes_df["route_id"].isin(active_ids)].copy()
open_market_ids = [oid for oid in active_ids if oid not in route_id_set]
open_market_df  = ships[ships["OrderID"].isin(open_market_ids)]
 
covered_orders = set()
for _, r in active_routes.iterrows():
    covered_orders.add(str(r["order1"]))
    if str(r.get("order2", "")) not in ("", "nan"):
        covered_orders.add(str(r["order2"]))
    if str(r.get("order3", "")) not in ("", "nan"):
        covered_orders.add(str(r["order3"]))
 
open_market_only_cost = float(ships["OpenMarketCost"].sum())
fixed_fleet_cost      = 4000 * 20 * 2
open_market_cost      = float(open_market_df["OpenMarketCost"].sum())
route_cost_total      = float(active_routes["route_cost"].sum())
 
if total_cost is None:
    total_cost = fixed_fleet_cost + route_cost_total + open_market_cost
    print(f"  total_cost not found in solution — computed: ${total_cost:,.2f}")
 
 
def route_detail(rdf):
    out = []
    for _, r in rdf.iterrows():
        o2 = str(r.get("order2", ""))
        o3 = str(r.get("order3", ""))
        out.append({
            "route_id":       r["route_id"],
            "stop_count":     int(r["stop_count"]),
            "order1":         str(r["order1"]),
            "order2":         "" if o2 in ("", "nan") else o2,
            "order3":         "" if o3 in ("", "nan") else o3,
            "total_miles":    round(float(r["total_miles"]), 1),
            "deadhead_miles": round(float(r["deadhead_miles"]), 1),
            "deadhead_ratio": round(float(r["deadhead_ratio"]), 4),
            "route_cost":     round(float(r["route_cost"]), 2),
        })
    return out
 
 
carrier_stats = []
for carrier_name, grp in active_routes.groupby("carrier"):
    w1 = grp[grp["week_of"] == 1]
    w2 = grp[grp["week_of"] == 2]
    carrier_stats.append({
        "name":           carrier_name,
        "total_routes":   int(len(grp)),
        "week1_routes":   int(len(w1)),
        "week2_routes":   int(len(w2)),
        "orders_covered": int(grp["stop_count"].sum()),
        "route_cost":     round(float(grp["route_cost"].sum()), 2),
        "avg_miles":      round(float(grp["total_miles"].mean()), 1),
        "routes_w1":      route_detail(w1),
        "routes_w2":      route_detail(w2),
    })
 
carrier_stats.sort(key=lambda x: -x["orders_covered"])
 
stop_counts = active_routes["stop_count"].value_counts().to_dict()
stop_counts["total"] = int(len(active_routes))
pd.DataFrame(carrier_stats).to_csv("report_carriers.csv", index=False)
active_routes.to_csv("report_routes.csv", index=False)
open_market_df.to_csv("report_open_market.csv", index=False)
savings     = open_market_only_cost - total_cost
savings_pct = savings / open_market_only_cost * 100
 
with open("solution_report.md", "w", encoding="utf-8") as f:
    f.write("# Freight Optimization Report\n\n")
 
    f.write("## Summary\n")
    f.write(f"- Total optimized cost: ${total_cost:,.2f}\n")
    f.write(f"- Open market baseline: ${open_market_only_cost:,.2f}\n")
    f.write(f"- Savings: ${savings:,.2f} ({savings_pct:.1f}%)\n\n")
 
    f.write("## Coverage\n")
    f.write(f"- Dedicated orders: {len(covered_orders)}\n")
    f.write(f"- Open market orders: {len(open_market_ids)}\n")
    f.write(f"- Total orders: {len(ships)}\n\n")
 
    f.write("## Cost Breakdown\n")
    f.write(f"- Fixed fleet cost: ${fixed_fleet_cost:,.2f}\n")
    f.write(f"- Route cost: ${route_cost_total:,.2f}\n")
    f.write(f"- Open market cost: ${open_market_cost:,.2f}\n\n")
 
    f.write("## Carrier Summary\n")
    for c in carrier_stats:
        f.write(f"- {c['name']}: {c['orders_covered']} orders, "
                f"{c['total_routes']} routes, "
                f"${c['route_cost']:,.2f}\n")
 

