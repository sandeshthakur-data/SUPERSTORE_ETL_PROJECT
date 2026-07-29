
from logging_config import logger
import subprocess

logger.info("ETL Pipeline Started")

subprocess.run(["python", "2_scripts/1_extract.py"], check=True)
subprocess.run(["python", "2_scripts/2_transform.py"], check=True)
subprocess.run(["python", "2_scripts/3_load.py"], check=True)

logger.info("ETL Pipeline Completed Successfully!")
print("ETL Pipeline Completed Successfully!")