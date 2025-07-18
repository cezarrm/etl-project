# ETL Project with Python

This project performs a complete **ETL (Extract, Transform, Load)** pipeline using Python and data extracted from the [https://dummyjson.com](https://dummyjson.com) API. The data is collected, stored as raw JSON files, transformed into structured CSVs, and finally merged into unified datasets by entity.

---

## Technologies Used

- `Python`
- `pandas`
- `requests`
- `json`

---

## Project Structure

project/
│
├── raw/ # Stores raw JSON files
│ ├── user/
│ └── products/
│
├── curated/ # Stores transformed CSV files
│ ├── user/
│ └── products/
│
├── load/ # Final consolidated CSV files
│
├── etl_dummyjson.py # Main ETL pipeline script
└── README.md # This file

---

## Pipeline Features

### 1. **Extract**

The function `extract_data(endpoint)` fetches JSON data from the REST API.  
The function `loop_data(endpoint)` loops through multiple records (limited by the `limit` variable) and stores each one in `raw/{endpoint}/{id}.json`.

---

### 2. **Transform**

The function `transform_data_json_to_csv(endpoint, i)` reads each raw JSON file and transforms it into a CSV file inside `curated/{endpoint}/`.

---

### 3. **Load**

The function `load_to_single_csv(endpoint)` merges all CSV files for a given entity into a single consolidated file in `load/{endpoint}_final.csv`.

---

### 4. **ETL Pipeline Function**

The function `etl_pipeline(endpoint)` runs the full ETL process for a given endpoint.  
Finally, the script runs the pipeline for each entity:

```python
endpoints = ["user", "products"]
for endpoint in endpoints:
    etl_pipeline(endpoint)

### How to Run
Install the required packages:

pip install pandas requests
Run the script:


python etl_dummyjson.py
Final CSV files will be available in the /load directory.

### Notes
- The script is limited to 10 records per entity (limit = 10) feel free to increase it.
- Folders like raw/, curated/, and load/ are created automatically.
- This project was made using the content that I found in DataEngineerHelp Channel on Youtube

### Learnings
- Performing HTTP requests with requests
- Reading and writing JSON and CSV files
- Building structured ETL pipelines
- Data transformation with pandas
- Organizing clean and modular Python code

