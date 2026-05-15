import pandas as pd
import zipcodes
import pickle

def get_data(input_file_path: str, output_path: str = "data.pkl") -> dict[str, pd.DataFrame]:
    """
    Read shipping data and calculate open market and dedicated cost

    Args:
        input_file_path (str): Path to the Excel table containing data
    
    Returns:
        out (dict[str, pd.DataFrame]): A dictionary containing lanes, shipments, locations, difficult_lanes and carriers dataframes
    """
    print("Loading data")
    input_data = pd.read_excel(input_file_path, sheet_name=None)

    lanes = input_data["Lanes"]
    shipments = input_data["Shipments"]
    locations = input_data["Locations"]
    difficult_lanes = input_data["Difficult Lanes"]

    # Make city names upper case
    lanes["Origin"] = lanes["Origin"].str.upper()
    lanes["Destination"] = lanes["Destination"].str.upper()
    shipments["Origin"] = shipments["Origin"].str.upper()
    shipments["Destination"] = shipments["Destination"].str.upper()
    shipments["Due Date"] = pd.to_datetime(shipments["Due Date"])
    locations["Location"] = locations["Location"].str.upper()

    # Get ZIP Codes for each location
    all_zips = {}
    for index, row in locations.iterrows():
        city, state = row["Location"].split(",")
        info = zipcodes.filter_by(city = city.capitalize(), state = state)
        zips = []
        for detail in info:
            zips.append(detail["zip_code"])
        all_zips[row["Location"]] = zips
    locations["zip codes"] = all_zips.values()

    # Add dedicated fleet costs and mileages to shipments
    costs = []
    mileages = []
    for index, row in shipments.iterrows():
        # if index> 100:
        #     break
        row["Origin"] = row["Origin"].upper()
        origin = row["Origin"]

        row["Destination"] = row["Destination"].upper()
        destination = row["Destination"]
        lane = lanes[(lanes["Origin"]==origin) & (lanes["Destination"]==destination)]
        assert lane.shape[0] == 1
        lane = lane.iloc[0]
        costs.append(lane["Cost"])
        mileages.append(lane["Mileage"])
    shipments["Dedicated Fleet cost"] = costs
    shipments["Mileage"] = mileages

    # Match city to area description in difficult lanes
    _location_cache = {row["Location"]: row["zip codes"] for _, row in locations.iterrows()}
    def area_match(city: str, area: str) -> bool:
        if "_" in area:
            # e.g. GA_300, GA_301
            if city not in _location_cache:
                return False
            prefix = area.split("_")[1]
            zipcodes = _location_cache[city]
            return any(z[:3] == prefix for z in zipcodes)
        else:
            # e.g. TX
            c, state = city.split(",")
            return state == area
    # Add surcharge per mile to shipments
    surcharges = []
    for index, row in shipments.iterrows():
        surcharge = 0
        origin, destination = row["Origin"], row["Destination"]
        candidates = difficult_lanes[difficult_lanes["Origin"]==origin]
        if candidates.shape[0] != 0:
            for idx, candidate in candidates.iterrows():
                if area_match(destination, candidate["Destination"]):
                    surcharge = float(candidate["Additional Cost $/Mile"])
        surcharges.append(surcharge)
    shipments["Surcharges"] = surcharges

    # Add open market cost to shipments
    shipments["Open Market cost"] = shipments["Dedicated Fleet cost"] + shipments["Mileage"] * shipments["Surcharges"]
    out = {"lanes": lanes, "shipments": shipments, "locations": locations,  
           "difficult_lanes": difficult_lanes, "carriers": input_data["Carriers"]}
    print("Loaded data")

    if output_path is not None:
        with open(output_path, 'wb') as f:
            pickle.dump(out, f)

    return out