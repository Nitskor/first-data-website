import sqlalchemy
from sqlalchemy import create_engine,text
import os


db_URL = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_URL)


def load_jobs():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = result.mappings().all()
  return jobs

