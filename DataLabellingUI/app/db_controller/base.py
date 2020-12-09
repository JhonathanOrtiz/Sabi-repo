from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
db = os.environ.get("DB_NAME")
host = os.environ.get("DB_HOST")
production = os.environ.get("PRODUCTION")
port = "5432"
if production:
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
else:
    engine = create_engine('sqlite:///app/db_controller/db.sqlite', connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)

Base = declarative_base()
