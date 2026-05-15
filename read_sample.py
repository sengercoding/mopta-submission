import pandas as pd

# ── Configuration ────────────────────────────────────────────────────────────
INPUT_FILE       = "AIMMS-MOPTA Interfor data.xlsx"
OUTPUT_FILE      = "AIMMS-MOPTA Interfor data SAMPLE.xlsx"
SAMPLE_SHIPMENTS = 100  # drives everything else
RANDOM_STATE     = 42

# ── Load ─────────────────────────────────────────────────────────────────────
data = pd.read_excel(INPUT_FILE, sheet_name=None)

# ── Step 1: Sample shipments first ───────────────────────────────────────────
# Everything else is derived from shipments to guarantee consistency
shipments_sample = data["Shipments"].sample(
    n=min(SAMPLE_SHIPMENTS, len(data["Shipments"])),
    random_state=RANDOM_STATE
)

# ── Step 2: Derive locations from sampled shipments ──────────────────────────
active_locs = set(shipments_sample["Origin"]) | set(shipments_sample["Destination"])
locations_df = data["Locations"][data["Locations"]["Location"].isin(active_locs)]

# Warn if any origin/destination is missing from the Locations sheet
missing_locs = active_locs - set(locations_df["Location"])
if missing_locs:
    print(f"Warning: {len(missing_locs)} locations referenced in shipments but missing from Locations sheet: {missing_locs}")

# ── Step 3: Filter lanes to active locations only ────────────────────────────
lanes_sample = data["Lanes"][
    data["Lanes"]["Origin"].isin(active_locs) &
    data["Lanes"]["Destination"].isin(active_locs)
]

# Warn if any shipment lane is missing
shipment_pairs = set(zip(shipments_sample["Origin"], shipments_sample["Destination"]))
lane_pairs     = set(zip(lanes_sample["Origin"], lanes_sample["Destination"]))
missing_lanes  = shipment_pairs - lane_pairs
if missing_lanes:
    print(f"Warning: {len(missing_lanes)} shipment lanes missing from Lanes sheet: {missing_lanes}")

# ── Step 4: Filter carriers whose home depot is in active locations ───────────
# This is the key fix vs the original — carriers are derived, not sampled independently
carriers_df = data["Carriers"][data["Carriers"]["Carrier Home"].isin(active_locs)]
if len(carriers_df) == 0:
    print("Warning: No carriers found for sampled locations. Consider increasing SAMPLE_SHIPMENTS.")

# ── Step 5: Filter due dates / any other order-linked sheets if present ───────
# Add similar filters here if your Excel has more sheets

# ── Report ────────────────────────────────────────────────────────────────────
print(f"\nLocations : {len(data['Locations']):>6}  →  {len(locations_df)}")
print(f"Carriers  : {len(data['Carriers']):>6}  →  {len(carriers_df)}")
print(f"Shipments : {len(data['Shipments']):>6}  →  {len(shipments_sample)}")
print(f"Lanes     : {len(data['Lanes']):>6}  →  {len(lanes_sample)}")
print(f"Active locations: {sorted(active_locs)}")

# ── Write output ──────────────────────────────────────────────────────────────
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    locations_df.reset_index(drop=True).to_excel(writer, sheet_name="Locations", index=False)
    carriers_df.reset_index(drop=True).to_excel(writer, sheet_name="Carriers",   index=False)
    shipments_sample.reset_index(drop=True).to_excel(writer, sheet_name="Shipments", index=False)
    lanes_sample.reset_index(drop=True).to_excel(writer, sheet_name="Lanes",     index=False)

print(f"\nSample file written to: {OUTPUT_FILE}")