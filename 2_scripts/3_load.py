
from logging_config import logger

logger.info("loading started")

import pandas as pd
from sqlalchemy import create_engine

# Load the cleaned CSV
df = pd.read_csv(r"3_output\clean_superstore.csv")

# Connect to MySQL
# Format: mysql+pymysql://username:password@host:port/database
engine = create_engine("mysql+pymysql://root:sandesh%40123@localhost:3306/superstore_db")

# Load into a table (creates it if it doesn't exist)
df.to_sql("superstore", con=engine, if_exists="replace", index=False)

print("Data loaded successfully into superstore_db.superstore")

logger.info("Loading completed")






