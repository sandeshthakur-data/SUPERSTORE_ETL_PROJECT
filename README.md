# Superstore ETL Project

## Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline using Python and MySQL.

## Technologies Used
- Python
- Pandas
- MySQL
- SQLAlchemy
- PyMySQL
- Logging

## Project Structure

SUPERSTORE_ETL_PROJECT/
│
├── 1_data/
├── 2_scripts/
├── 3_output/
├── logs/
├── requirements.txt
├── README.md
└── .gitignore

## ETL Process

### 1. Extract
- Read data from the Excel file.

### 2. Transform
- Clean missing values.
- Rename columns.
- Remove duplicates.
- Save cleaned data as CSV.

### 3. Load
- Load the cleaned CSV into the MySQL database.

### 4. Logging
- Record ETL execution in `logs/etl.log`.

## How to Run

```bash
python 2_scripts/main.py
```

## Output
- Clean CSV file in `3_output/`
- Data loaded into MySQL
- Log file in `logs/etl.log`