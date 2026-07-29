
from logging_config import logger

# your existing code

logger.info("Transformation start")

import pandas as pd  # Import pandas library

# Read the Excel file
df = pd.read_excel("1_data/SampleSuperstore.xlsx")

# Count duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Show new dataset size
print(df.shape)

# Count missing values in each column
print(df.isnull().sum())

# Show original column names
print(df.columns)

# Rename all column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Show new column names
print(df.columns)# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Convert ship_date to datetime
df["ship_date"] = pd.to_datetime(df["ship_date"])

# Check the data types
print(df.dtypes)

# Create a new column for shipping days
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

# Show the first 5 rows
print(df[["order_date", "ship_date", "shipping_days"]].head())

# Save the cleaned data to CSV
df.to_csv("3_output/clean_superstore.csv", index=False)

print("Cleaned data saved successfully!")

logger.info("Transformation completed")