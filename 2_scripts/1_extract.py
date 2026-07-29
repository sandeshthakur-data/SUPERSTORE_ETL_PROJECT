
from logging_config import logger

logger.info("Extraction started")

import pandas as pd  # Import the pandas library



# Read the Excel file into a DataFrame
df = pd.read_excel("1_data/SampleSuperstore.xlsx")

# # Show the first 5 rows of the dataset
# print(df.head())

# # Show the number of rows and columns
# print(df.shape)

# # Show all column names
# print(df.columns)

# # Show the data type of each column
#print(df.dtypes) 

# Show dataset information
#print(df.info())

#Show missing values
#print(df.isnull().sum())

# # Show summary statistics
print(df.describe())
logger.info("Extraction completed")