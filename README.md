# OSM POI Extractor 📍🗺️

This Python script allows you to extract Points of Interest (POIs) from OpenStreetMap (`.osm.pbf`) files. It leverages the `pyrosm` library to parse the OSM data and outputs the extracted POIs into one or more CSV files, making it easy to analyze or use in other applications.

-----

## Features ✨

  * **Batch Processing**: Automatically processes all `.osm.pbf` files found in a specified folder.
  * **POI Extraction**: Extracts `name`, `amenity`, and `shop` information from POIs.
  * **Large File Handling**: Automatically splits large output into multiple CSV files (max 300,000 rows per file) to prevent memory issues and make files more manageable.
  * **Timestamped Output**: Generates uniquely named CSV files with timestamps for easy organization.
  * **User-Friendly Interface**: Simple command-line interface for specifying the input folder.

-----

## Prerequisites 🛠️

Before you can run this script, ensure you have the following installed:

  * **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
  * **Required Python Libraries**: These will be installed via `pip`.

-----

## Installation 💻

1.  **Clone the repository** (or download the `main.py` file):
    ```bash
    git clone https://github.com/MemonDeveloper/OSM-POI-Extractor.git
    cd OSM-POI-Extractor
    ```
2.  **Create a `requirements.txt` file**: In the root directory of your project, create a file named `requirements.txt` and paste the following content:
    ```
    pyrosm
    pandas
    openpyxl # For general Excel operations, though not directly used in .csv output, good to include if pandas uses it
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
      * **Note for `pyrosm`**: `pyrosm` relies on `libosmium` and `geos`. On some systems, you might need to install these system-level dependencies first.
          * **Debian/Ubuntu**: `sudo apt update && sudo apt install libosmium2-dev libgeos-dev`
          * **macOS (Homebrew)**: `brew install libosmium geos`
          * **Windows**: Installation can be more involved. Refer to the `pyrosm` documentation or use a Conda environment.

-----

## Usage ▶️

1.  **Download `.osm.pbf` files**: Obtain OpenStreetMap data extracts in `.osm.pbf` format. You can find these from:

      * **Geofabrik**: [https://download.geofabrik.de/](https://download.geofabrik.de/) (for country/region extracts)
      * **OpenStreetMap**: [https://download.openstreetmap.fr/extracts/oceania/australia/](https://download.openstreetmap.fr/extracts/oceania/australia/) (for specific extracts like Provinces)
      * Place these `.osm.pbf` files into a dedicated folder on your system.

2.  **Run the script**:

    ```bash
    python main.py
    ```

3.  **Enter the folder path**: The script will prompt you to enter the full path to the folder containing your `.osm.pbf` files:

    ```
    📁 Enter folder path with .osm.pbf files: C:\Users\YourUser\Downloads\OSM_Data
    ```

    (On Linux/macOS, it might look like `/home/youruser/osm_data/`)

The script will then iterate through each `.osm.pbf` file in the specified folder, extract the POIs, and save them as CSV files in the same directory where you run the script.

-----

## Output CSV Format 📊

Each output CSV file will contain the following columns:

  * `name`: The name of the Point of Interest.
  * `amenity`: The type of amenity (e.g., `restaurant`, `school`, `hospital`).
  * `shop`: The type of shop (e.g., `supermarket`, `bakery`, `clothes`).

-----

## Important Notes ⚠️

  * **Data Volume**: `.osm.pbf` files can be very large, and processing them can take a significant amount of time and memory. The script automatically splits outputs to handle this, but be patient with large extracts.
  * **Column Selection**: The script currently extracts `name`, `amenity`, and `shop` columns. If you need more data (e.g., `leisure`, `tourism`, address details), you can modify the `columns_to_keep` list in the `main.py` file.
  * **Error Handling**: The script includes basic error handling for file processing and empty POI results.

-----

## Contributing 🤝

Feel free to fork this repository, open issues, and submit pull requests if you have suggestions for improvements or bug fixes.

-----
