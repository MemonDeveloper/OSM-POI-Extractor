import pandas as pd
import math
import os
from datetime import datetime
from pyrosm import OSM

# 🔁 Step 1: Ask for the folder path containing .osm.pbf files
folder_path = input("📁 Enter folder path with .osm.pbf files: ").strip()

# ✅ Step 2: Check if folder exists
if not os.path.isdir(folder_path):
    print("❌ Folder not found. Please check the path and try again.")
    exit()

# ✅ Step 3: Get all .osm.pbf files in the folder
pbf_files = [f for f in os.listdir(folder_path) if f.endswith(".osm.pbf")]

if not pbf_files:
    print("⚠️ No .osm.pbf files found in the folder.")
    exit()

# ✅ Step 4: Process each file
for pbf_filename in pbf_files:
    pbf_file_path = os.path.join(folder_path, pbf_filename)
    base_filename = os.path.splitext(pbf_filename)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f"\n📦 Processing: {pbf_filename}")
    
    try:
        osm = OSM(pbf_file_path)
        pois = osm.get_pois()
    except Exception as e:
        print(f"❌ Error processing {pbf_filename}: {e}")
        continue

    if pois is None or pois.empty:
        print(f"⚠️ No POIs found in {pbf_filename}. Skipping.")
        continue

    # columns_to_keep = ["name", "amenity", "shop", "leisure", "tourism","addr:street", "addr:city", "addr:state", "lon", "lat"]
    columns_to_keep = ["name", "amenity", "shop"]
    available_columns = [col for col in columns_to_keep if col in pois.columns]
    pois_clean = pois[available_columns].copy()

    total_rows = len(pois_clean)
    max_rows = 300000
    num_files = math.ceil(total_rows / max_rows)

    print(f"✅ Found {total_rows} POIs. Saving to {num_files} CSV file(s)...")

    for i in range(num_files):
        start = i * max_rows
        end = start + max_rows
        chunk = pois_clean.iloc[start:end]
        output_filename = f"{base_filename}_pois_{timestamp}_{i + 1}.csv"
        chunk.to_csv(output_filename, index=False)
        # chunk.to_excel(output_filename, index=False)
        print(f"📁 Saved: {output_filename} with {len(chunk)} rows")

print("\n🎉 All files processed successfully!")