# Extract optimization results from AIMMS and write them to CSV / console.
# Run this AFTER MainExecution has solved Goal_Function.
from singleton import my_aimms
import pandas as pd

# ---------------------------------------------------------------------------
# Pull variable values back from AIMMS
# ---------------------------------------------------------------------------
# .data() returns a pandas DataFrame because data_type_preference=PANDAS in singleton.
# For sparse variables only the non-default (non-zero) entries are returned.
y_df       = my_aimms.y.data()           # columns: t, o, y
v_df       = my_aimms.v.data()           # columns: o, v
cost_tw_df = my_aimms.CostTW.data()      # columns: t, w, CostTW
total_cost = my_aimms.total_cost.data()  # scalar

# Round the binaries — solver returns them as floats very close to 0 or 1
y_df["y"] = y_df["y"].round().astype(int)
v_df["v"] = v_df["v"].round().astype(int)

# Keep only the rows where the binary is actually 1
assigned   = y_df[y_df["y"] == 1].copy()
open_mkt   = v_df[v_df["v"] == 1].copy()

# ---------------------------------------------------------------------------
# Per-order assignment table (one row per order)
# ---------------------------------------------------------------------------
orders_all = my_aimms.Orders.data()  # list of order IDs
orders_df  = pd.DataFrame({"o": list(orders_all)})

# Look up the carrier for each order; orders not in `assigned` go to open market or are unfilled
order_to_carrier = dict(zip(assigned["o"], assigned["t"]))
order_to_v       = dict(zip(open_mkt["o"], open_mkt["v"]))

def status_for(o):
    if o in order_to_carrier:
        return "Dedicated"
    if o in order_to_v:
        return "Open market"
    return "Unfilled"

orders_df["Carrier"] = orders_df["o"].map(order_to_carrier).fillna("")
orders_df["Status"]  = orders_df["o"].apply(status_for)
orders_df = orders_df.rename(columns={"o": "Order"})

# ---------------------------------------------------------------------------
# Per-carrier summary
# ---------------------------------------------------------------------------
carrier_summary = (
    assigned.groupby("t")
            .size()
            .reset_index(name="OrdersAssigned")
            .rename(columns={"t": "Carrier"})
)
# Total weekly pay per carrier (sum over weeks)
pay_by_carrier = (
    cost_tw_df.groupby("t")["CostTW"]
              .sum()
              .reset_index()
              .rename(columns={"t": "Carrier", "CostTW": "TotalPaid"})
)
carrier_summary = carrier_summary.merge(pay_by_carrier, on="Carrier", how="outer").fillna(0)

# ---------------------------------------------------------------------------
# Cost breakdown
# ---------------------------------------------------------------------------
fleet_cost = float(cost_tw_df["CostTW"].sum())

# Open-market cost = sum of OpenMarketCost(o) for orders sent to open market
omc_df = my_aimms.OpenMarketCost.data().rename(columns={"OpenMarketCost": "omc"})
om_cost = float(omc_df.merge(open_mkt, on="o")["omc"].sum())

# ---------------------------------------------------------------------------
# Console summary
# ---------------------------------------------------------------------------
n_total    = len(orders_df)
n_dedicated = (orders_df["Status"] == "Dedicated").sum()
n_open      = (orders_df["Status"] == "Open market").sum()
n_unfilled  = (orders_df["Status"] == "Unfilled").sum()

print("=" * 56)
print(f"Orders total       : {n_total}")
print(f"  -> Dedicated     : {n_dedicated}")
print(f"  -> Open market   : {n_open}")
print(f"  -> Unfilled      : {n_unfilled}")
print("-" * 56)
print(f"Fleet cost         : ${fleet_cost:>12,.0f}")
print(f"Open market cost   : ${om_cost:>12,.0f}")
print(f"Total objective    : ${fleet_cost + om_cost:>12,.0f}")
print(f"AIMMS total_cost   : ${float(total_cost):>12,.0f}")
print("=" * 56)
print("\nPer-carrier summary:")
print(carrier_summary.to_string(index=False))

# ---------------------------------------------------------------------------
# Write to disk for downstream use
# ---------------------------------------------------------------------------
orders_df.to_csv("solution_orders.csv", index=False)
carrier_summary.to_csv("solution_carriers.csv", index=False)
cost_tw_df.to_csv("solution_cost_per_week.csv", index=False)

print("\nWritten: solution_orders.csv, solution_carriers.csv, solution_cost_per_week.csv")