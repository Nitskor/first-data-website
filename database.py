from flask import jsonify
import sqlalchemy
from sqlalchemy import create_engine,text
import os
import psycopg2


db_URL = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_URL)


def load_jobs():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = result.mappings().all()
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val':id})
    job =[dict(row) for row in result.mappings().all()] 
    return job

def add_application_to_db(job_id,data):
  
  with engine.connect() as conn:
    with conn.begin():
      query = text("INSERT INTO applications (job_id,full_name,email,age,work_experience) VALUES(:job_id,:full_name,:email,:age,:work_experience)")
      params = {'job_id':job_id,'full_name':data['full_name'],'email':data['email'],'age':data['age'],'work_experience':data['work_experience']}
      conn.execute(query,params)



  
    


