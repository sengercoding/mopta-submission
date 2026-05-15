import pandas as pd

routes_df = pd.read_csv("routes.csv", dtype=str)

# --- route_carrier.csv: RouteCarrier(r,t) ---
routes_df[["route_id","carrier"]]\
    .rename(columns={"route_id":"r","carrier":"t"})\
    .assign(value=1)\
    .to_csv("route_carrier.csv", index=False)

# --- route_covers.csv: RouteCovers(r,o) ---
covers = []
for _, row in routes_df.iterrows():
    covers.append({"r": row["route_id"], "o": row["order1"], "value": 1})
    if str(row.get("order2","")) not in ("","nan"):
        covers.append({"r": row["route_id"], "o": row["order2"], "value": 1})
    if str(row.get("order3","")) not in ("","nan"):
        covers.append({"r": row["route_id"], "o": row["order3"], "value": 1})
    if str(row.get("order4","")) not in ("","nan"):
        covers.append({"r": row["route_id"], "o": row["order4"], "value": 1})
pd.DataFrame(covers).to_csv("route_covers.csv", index=False)

xl = pd.read_excel("AIMMS-MOPTA Interfor data.xlsx", sheet_name=None)
shipments_df = xl["Shipments"].copy()
carriers_df  = xl["Carriers"].copy()

shipments_df["OrderID"]     = shipments_df["Order Number"].astype(str)
shipments_df["Origin"]      = shipments_df["Origin"].str.upper()
shipments_df["Destination"] = shipments_df["Destination"].str.upper()
carriers_df["Carrier Home"] = carriers_df["Carrier Home"].str.upper()

order_origin = dict(zip(shipments_df["OrderID"], shipments_df["Origin"]))
order_dest   = dict(zip(shipments_df["OrderID"], shipments_df["Destination"]))
carrier_home = dict(zip(carriers_df["Carrier"].astype(str), carriers_df["Carrier Home"]))

# --- routes_strings.csv: all string parameters indexed by r ---
routes_df["RouteCarrierHome"]  = routes_df["carrier"].map(carrier_home)
routes_df["RouteOrder1Origin"] = routes_df["order1"].map(order_origin)
routes_df["RouteOrder1Dest"]   = routes_df["order1"].map(order_dest)
routes_df["RouteOrder2Origin"] = routes_df["order2"].apply(
    lambda x: order_origin.get(str(x), "") if str(x) not in ("", "nan") else "")
routes_df["RouteOrder2Dest"]   = routes_df["order2"].apply(
    lambda x: order_dest.get(str(x), "")   if str(x) not in ("", "nan") else "")
routes_df["RouteOrder3Origin"] = routes_df["order3"].apply(
    lambda x: order_origin.get(str(x), "") if str(x) not in ("", "nan") else "")
routes_df["RouteOrder3Dest"]   = routes_df["order3"].apply(
    lambda x: order_dest.get(str(x), "")   if str(x) not in ("", "nan") else "")
routes_df["RouteOrder4Origin"] = routes_df["order4"].apply(
    lambda x: order_origin.get(str(x), "") if str(x) not in ("", "nan") else "")
routes_df["RouteOrder4Dest"]   = routes_df["order4"].apply(
    lambda x: order_dest.get(str(x), "")   if str(x) not in ("", "nan") else "")


routes_df[["route_id",
           "RouteCarrierHome",
           "RouteOrder1Origin", "RouteOrder1Dest",
           "RouteOrder2Origin", "RouteOrder2Dest",
           "RouteOrder3Origin", "RouteOrder3Dest",
           "RouteOrder4Origin", "RouteOrder4Dest", 
           "route_id","stop_count","route_cost","week_of",
           "total_miles","deadhead_miles","deadhead_ratio"]]\
            .to_csv("routes_params.csv", index=False)