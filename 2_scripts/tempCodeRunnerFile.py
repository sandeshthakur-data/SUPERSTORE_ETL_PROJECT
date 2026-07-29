from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")

from sqlalchemy.engine import URL
url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=password,
    host="localhost",
    port=3306,
    database="superstore_db",
)
engine = create_engine(url)