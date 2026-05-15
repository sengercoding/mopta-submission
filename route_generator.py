import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from tqdm import tqdm
import pickle
from load_data import get_data
from typing import Union

k = 50
k_4orders = 20

routes_file = "routes.csv"
data_path = "data.pkl"
excel_file = "AIMMS-MOPTA Interfor data.xlsx"

try:
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
except:
    data = get_data(excel_file, data_path)

LANE_DISTANCES: dict[tuple[str, str], float] = {}
for _, row in data["lanes"].iterrows():
    LANE_DISTANCES[(row["Origin"], row["Destination"])] = row["Mileage"]

orders_df = data["shipments"]
print(f"Open market cost = {sum([r['Dedicated Fleet cost'] for _, r in orders_df.iterrows()])}")
due1 = datetime(2026, 1, 17)
due2 = datetime(2026, 1, 24)
# Note that due to the data, we assume that every order is due on a Sunday

@dataclass
class Order:
    order_no: int
    origin: str
    destination: str
    open_market_cost: float
    dedicated_fleet_cost: float
    distance: float
    due_date: datetime

@dataclass
class Carrier:
    id: int
    home: str
    name: str

@dataclass
class Route:
    carrier: Carrier
    orders: list[Order]
    def __post_init__(self) -> None:
        self.id: int = 0
        self.loaded_distance: float = sum([o.distance for o in self.orders])
        deadhead_miles: float = LANE_DISTANCES[(self.carrier.home, self.orders[0].origin)]
        for i in range(1,len(self.orders)):
            deadhead_miles += LANE_DISTANCES[(self.orders[i-1].destination, self.orders[i].origin)]
        self.deadhead_miles = deadhead_miles
        self.dedicated_fleet_cost = sum([o.dedicated_fleet_cost for o in self.orders])

    def final_near_home(self) -> bool:
        last_order = self.orders[-1]
        return LANE_DISTANCES[(last_order.destination, self.carrier.home)] <= 100

    def weekly_max_mileage(self) -> bool:
        return self.loaded_distance + self.deadhead_miles <= 450*5

    def deadhead_limit(self) -> bool:
        return self.deadhead_miles <= self.loaded_distance

    def is_feasible_weekly(self):
        return self.final_near_home() and self.weekly_max_mileage() and self.deadhead_limit()

    def to_dict(self) -> dict[str, Union[float, int]]:
        n_orders = len(self.orders)
        d = {}
        d["route_id"] = self.id
        d["carrier"] = self.carrier.name
        d["order_count"] = n_orders
        d["order1"] = self.orders[0].order_no
        d["order2"] = self.orders[1].order_no if n_orders >= 2 else ""
        d["order3"] = self.orders[2].order_no if n_orders >= 3 else ""
        d["order4"] = self.orders[3].order_no if n_orders >= 4 else ""
        d["total_miles"] = self.loaded_distance + self.deadhead_miles
        d["loaded_miles"] = self.loaded_distance
        d["deadhead_ratio"] = self.deadhead_miles / (self.loaded_distance + self.deadhead_miles)
        d["route_cost"] = self.dedicated_fleet_cost
        d["week_of"] = 1 if self.orders[-1].due_date == due1 else 2
        return d

orders_week1: list[Order] = []
orders_week2: list[Order] = []
carriers: list[Carrier] = []

# create order objects
for _, row in orders_df.iterrows():
    order = Order(row["Order Number"], row["Origin"], row["Destination"],
                  row["Open Market cost"], row["Dedicated Fleet cost"], row["Mileage"],
                  row["Due Date"])
    if row["Due Date"] == due1:
        orders_week1.append(order)
    elif row["Due Date"] == due2:
        orders_week2.append(order)
    else:
        raise ValueError

# create carrier objects
for i, (_, row) in enumerate(data["carriers"].iterrows()):
    carrier = Carrier(i, row["Carrier Home"], row["Carrier"])
    carriers.append(carrier)

def build_neighbors(orders: list[Order], limit: int) -> dict[int, list[Order]]:
    neighbors = {}
    for o1 in orders:
        candidates = sorted(
            [o2 for o2 in orders if o2 is not o1],
            key=lambda o2: LANE_DISTANCES[(o1.destination, o2.origin)]
        )
        neighbors[o1.order_no] = candidates[:limit]
    return neighbors

ROUTES: list[Route] = []

for orders_week in [orders_week1, orders_week2]:
    neighbors = build_neighbors(orders_week, k)
    neighbors_4stop = build_neighbors(orders_week, k_4orders)

    for carrier in tqdm(carriers, desc=f"Week of {orders_week[0].due_date.date()}"):
        reachable = sorted(orders_week, key=lambda o: LANE_DISTANCES[(carrier.home, o.origin)])[:k]
        close_to_home_ids = {
            o.order_no for o in orders_week
            if LANE_DISTANCES[(o.destination, carrier.home)] <= 100
        }

        # 1-stop
        for o1 in reachable:
            route = Route(carrier, [o1])
            if route.is_feasible_weekly():
                ROUTES.append(route)

        # 2-stop
        for o1 in reachable:
            for o2 in orders_week:
                if o2.order_no == o1.order_no: continue
                if o2.order_no not in close_to_home_ids: continue
                route = Route(carrier, [o1, o2])
                if route.is_feasible_weekly():
                    ROUTES.append(route)

        # 3-stop
        for o1 in reachable:
            for o2 in neighbors[o1.order_no]:
                for o3 in neighbors[o2.order_no]:
                    if o3.order_no in (o1.order_no, o2.order_no): continue
                    if o3.order_no not in close_to_home_ids: continue
                    route = Route(carrier, [o1, o2, o3])
                    if route.is_feasible_weekly():
                        ROUTES.append(route)

        # 4-stop
        for o1 in reachable:
            for o2 in neighbors_4stop[o1.order_no]:
                for o3 in neighbors_4stop[o2.order_no]:
                    if o3.order_no in (o1.order_no, o2.order_no): continue
                    for o4 in neighbors_4stop[o3.order_no]:
                        if o4.order_no in (o1.order_no, o2.order_no, o3.order_no): continue
                        if o4.order_no not in close_to_home_ids: continue
                        route = Route(carrier, [o1, o2, o3, o4])
                        if route.is_feasible_weekly():
                            ROUTES.append(route)

for i, route in enumerate(ROUTES):
    route.id = i + 1

print(f"Found {len(ROUTES)} feasible routes")

routes_df = pd.DataFrame([r.to_dict() for r in ROUTES])
routes_df.to_csv(routes_file, index=False)
print(f"Written to {routes_file}")
