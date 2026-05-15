# read_input_data.py
# ===================
# Loads all input data into AIMMS for the multi-stop route model.
#
# Cost logic:
#   Lanes."Cost"       -> DedicatedFleetCost (payment to dedicated carrier)
#   Lanes."Total Cost" -> OpenMarketCost     (spot market cost, incl. surcharges)
#
# Workflow:
#   1. Run route_generator.py to build routes.csv (feasible 1- and 2-stop routes)
#   2. Load routes.csv + original Excel data into AIMMS sets and parameters

from singleton import my_aimms
import pandas as pd
import math
import subprocess
import os

# ---------------------------------------------------------------------------
# Step 1: Generate routes (run route_generator.py if needed)
# ---------------------------------------------------------------------------
ROUTES_FILE  = "routes-three-stops-fast.csv"
INPUT_EXCEL  = "AIMMS-MOPTA Interfor data.xlsx"
ROUTE_SCRIPT = "route_generator_three_stops.py"

if not os.path.exists(ROUTES_FILE):
    print("routes.csv not found — running route_generator.py ...")
    result = subprocess.run(["python", ROUTE_SCRIPT], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"route_generator.py failed:\n{result.stderr}")
    print(result.stdout)
else:
    print(f"Using existing {ROUTES_FILE}")

# ---------------------------------------------------------------------------
# Step 2: Load Excel
# ---------------------------------------------------------------------------
input_data = pd.read_excel(INPUT_EXCEL, sheet_name=None)

carriers_df  = input_data["Carriers"]
shipments_df = input_data["Shipments"]
lanes_df     = input_data["Lanes"]

# Normalise to uppercase
carriers_df["Carrier Home"] = carriers_df["Carrier Home"].str.upper()
shipments_df["Origin"]      = shipments_df["Origin"].str.upper()
shipments_df["Destination"] = shipments_df["Destination"].str.upper()
lanes_df["Origin"]          = lanes_df["Origin"].str.upper()
lanes_df["Destination"]     = lanes_df["Destination"].str.upper()

# ---------------------------------------------------------------------------
# Lane lookups
#   Cost       -> dedicated fleet payment
#   Total Cost -> open market cost (already includes all surcharges)
# ---------------------------------------------------------------------------
lane_mileage   = {(r["Origin"], r["Destination"]): r["Mileage"]     for _, r in lanes_df.iterrows()}
lane_ded_cost  = {(r["Origin"], r["Destination"]): r["Cost"]        for _, r in lanes_df.iterrows()}
lane_open_cost = {(r["Origin"], r["Destination"]): r["Total Cost"]  for _, r in lanes_df.iterrows()}

def _lookup(table, key, label):
    if key not in table:
        raise KeyError(f"Lane {key} not found in Lanes sheet ({label}).")
    return table[key]

# ---------------------------------------------------------------------------
# Step 3: Shipment preprocessing
# ---------------------------------------------------------------------------
parsed = pd.to_datetime(shipments_df["Due Date"], errors="coerce")
fallback = parsed.isna()
if fallback.any():
    parsed.loc[fallback] = pd.to_datetime(
        shipments_df.loc[fallback, "Due Date"], errors="coerce", dayfirst=True
    )
if parsed.isna().any():
    bad = shipments_df.loc[parsed.isna(), "Due Date"].head(10).tolist()
    raise ValueError(f"Unparseable Due Date values: {bad}")

first_due = parsed.min().normalize()
shipments_df["DueDay"]  = ((parsed - first_due).dt.days + 7).astype(int)
shipments_df["WeekOf"]  = (shipments_df["DueDay"] // 7).astype(int)
shipments_df["OrderID"] = shipments_df["Order Number"].astype(str)

shipments_df["Mileage"] = shipments_df.apply(
    lambda r: _lookup(lane_mileage,   (r["Origin"], r["Destination"]), "Mileage"), axis=1
)
shipments_df["DedicatedFleetCost"] = shipments_df.apply(
    lambda r: _lookup(lane_ded_cost,  (r["Origin"], r["Destination"]), "Cost"), axis=1
)
shipments_df["OpenMarketCost"] = shipments_df.apply(
    lambda r: _lookup(lane_open_cost, (r["Origin"], r["Destination"]), "Total Cost"), axis=1
)

shipments_df["LoadDays"]  = shipments_df["Mileage"].apply(lambda m: max(1, math.ceil(m / 450)))
shipments_df["LoadStart"] = (shipments_df["DueDay"] - shipments_df["LoadDays"] + 1).clip(lower=0)

# ---------------------------------------------------------------------------
# Step 4: Load routes
# ---------------------------------------------------------------------------
routes_df = pd.read_csv(ROUTES_FILE, dtype={"order1": str, "order2": str})
routes_df["route_id"] = routes_df["route_id"].astype(str)

all_order_ids = set(shipments_df["OrderID"])
route_orders  = (
    set(routes_df["order1"])
    | set(routes_df["order2"].replace("", float("nan")).dropna())
)
missing = route_orders - all_order_ids
if missing:
    print(f"WARNING: {len(missing)} route order IDs not in shipments — dropping affected routes")
    routes_df = routes_df[
        routes_df["order1"].isin(all_order_ids) &
        routes_df["order2"].apply(lambda x: x == "" or x in all_order_ids)
    ]

print(f"Loaded {len(routes_df):,} routes covering {routes_df['carrier'].nunique()} carriers")

# ---------------------------------------------------------------------------
# Step 5: Populate AIMMS sets
# ---------------------------------------------------------------------------
my_aimms.Carriers.assign(set(carriers_df["Carrier"].astype(str)))
my_aimms.Orders.assign(list(shipments_df["OrderID"]))
my_aimms.Routes.assign(list(routes_df["route_id"]))
my_aimms.Weeks.assign(
    sorted({str(int(w)) for w in shipments_df["WeekOf"].unique()})
)

# ---------------------------------------------------------------------------
# Step 6: Order-indexed parameters
# ---------------------------------------------------------------------------
my_aimms.Mileage.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["Mileage"]))
)
my_aimms.OpenMarketCost.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["OpenMarketCost"]))
)
my_aimms.DedicatedFleetCost.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["DedicatedFleetCost"]))
)
my_aimms.DueDay.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["DueDay"].astype(int)))
)
my_aimms.WeekOf.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["WeekOf"].astype(int)))
)
my_aimms.LoadDays.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["LoadDays"].astype(int)))
)
my_aimms.LoadStart.assign(
    dict(zip(shipments_df["OrderID"], shipments_df["LoadStart"].astype(int)))
)

# ---------------------------------------------------------------------------
# Step 7: Route-indexed parameters
# ---------------------------------------------------------------------------
my_aimms.RouteCost.assign(
    dict(zip(routes_df["route_id"], routes_df["route_cost"]))
)
my_aimms.RouteWeek.assign(
    dict(zip(routes_df["route_id"], routes_df["week_of"].astype(int)))
)
my_aimms.RouteTotalMiles.assign(
    dict(zip(routes_df["route_id"], routes_df["total_miles"]))
)
my_aimms.RouteDeadheadMiles.assign(
    dict(zip(routes_df["route_id"], routes_df["deadhead_miles"]))
)
my_aimms.RouteDeadheadRatio.assign(
    dict(zip(routes_df["route_id"], routes_df["deadhead_ratio"]))
)
my_aimms.RouteStops.assign(
    dict(zip(routes_df["route_id"], routes_df["stop_count"].astype(int)))
)

# RouteCarrier(r, t)
rc_df = pd.DataFrame(
    [(r["route_id"], r["carrier"], 1) for _, r in routes_df.iterrows()],
    columns=["r", "t", "RouteCarrier"]
)
my_aimms.RouteCarrier.assign(rc_df)

# RouteCovers(r, o)
covers_rows = []
for _, r in routes_df.iterrows():
    covers_rows.append((r["route_id"], str(r["order1"]), 1))
    if r["order2"] != "" and pd.notna(r["order2"]):
        covers_rows.append((r["route_id"], str(r["order2"]), 1))

my_aimms.RouteCovers.assign(
    pd.DataFrame(covers_rows, columns=["r", "o", "RouteCovers"])
)

# ---------------------------------------------------------------------------
# Step 8: Location coordinates and types (for map visualisation)
# ---------------------------------------------------------------------------
locations_df = input_data["Locations"].copy()
locations_df["Location"] = locations_df["Location"].str.upper()

my_aimms.Locations.assign(list(locations_df["Location"]))
my_aimms.LocationLat.assign(
    dict(zip(locations_df["Location"], locations_df["Latitude"]))
)
my_aimms.LocationLon.assign(
    dict(zip(locations_df["Location"], locations_df["Longitude"]))
)

# Assign LocationType: "home" | "origin" | "destination"
# A location can be multiple types; priority: home > origin > destination
carrier_homes_set = set(carriers_df["Carrier Home"].str.upper())
order_origins_set = set(shipments_df["Origin"])
order_dests_set   = set(shipments_df["Destination"])

location_type = {}
for loc in locations_df["Location"]:
    if loc in carrier_homes_set:
        location_type[loc] = "home"
    elif loc in order_origins_set:
        location_type[loc] = "origin"
    elif loc in order_dests_set:
        location_type[loc] = "destination"
    else:
        location_type[loc] = "destination"  # fallback

my_aimms.LocationType.assign(location_type)

# ---------------------------------------------------------------------------
# Step 9: Route location strings (for BuildMapData procedure)
# ---------------------------------------------------------------------------
order_origin_map = dict(zip(shipments_df["OrderID"], shipments_df["Origin"]))
order_dest_map   = dict(zip(shipments_df["OrderID"], shipments_df["Destination"]))
carrier_home_map = dict(zip(carriers_df["Carrier"].astype(str),
                            carriers_df["Carrier Home"].str.upper()))

route_carrier_home  = {}
route_order1_origin = {}
route_order1_dest   = {}
route_order2_origin = {}
route_order2_dest   = {}
route_order3_origin = {}
route_order3_dest = {}

for _, row in routes_df.iterrows():
    rid = row["route_id"]
    route_carrier_home[rid]  = carrier_home_map.get(row["carrier"], "")
    route_order1_origin[rid] = order_origin_map.get(str(row["order1"]), "")
    route_order1_dest[rid]   = order_dest_map.get(str(row["order1"]), "")
    o2 = str(row["order2"]) if row["order2"] != "" and pd.notna(row["order2"]) else ""
    route_order2_origin[rid] = order_origin_map.get(o2, "") if o2 else ""
    route_order2_dest[rid]   = order_dest_map.get(o2, "") if o2 else ""
    o3 = str(row["order3"]) if row["order3"] != "" and pd.notna(row["order3"]) else ""
    route_order3_origin[rid] = order_origin_map.get(o3, "") if o3 else ""
    route_order3_dest[rid]   = order_dest_map.get(o3, "") if o3 else ""
    
    

my_aimms.RouteCarrierHome.assign(route_carrier_home)
my_aimms.RouteOrder1Origin.assign(route_order1_origin)
my_aimms.RouteOrder1Dest.assign(route_order1_dest)
my_aimms.RouteOrder2Origin.assign(route_order2_origin)
my_aimms.RouteOrder2Dest.assign(route_order2_dest)
my_aimms.RouteOrder3Origin.assign(route_order3_origin)
my_aimms.RouteOrder3Dest.assign(route_order3_dest)


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print("\n=== AIMMS Data Load Summary ===")
print(f"  Carriers:            {len(carriers_df)}")
print(f"  Orders:              {len(shipments_df)}")
print(f"  Routes:              {len(routes_df):,}")
print(f"    1-stop:            {(routes_df['stop_count'] == 1).sum():,}")
print(f"    2-stop:            {(routes_df['stop_count'] == 2).sum():,}")
print(f"    3-stop:            {(routes_df['stop_count'] == 3).sum():,}")
print(f"  Weeks:               {shipments_df['WeekOf'].nunique()}")
print(f"  RouteCovers entries: {len(covers_rows):,}")