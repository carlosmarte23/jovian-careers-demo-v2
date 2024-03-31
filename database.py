from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
db_connection_string = os.getenv("DATABASE_URL")
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
  
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    return dict(rows[0]._mapping)
  
def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    params = {"job_id": job_id,
              "full_name": data["full_name"],
              "email": data["email"],
              "linkedin_url": data["linkedin_url"],
              "education": data["education"],
              "work_experience": data["work_experience"],
              "resume_url": data["resume_url"]
              }

    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
      
    try:
        conn.execute(query, params)
        conn.commit()  
    except Exception as e:
        conn.rollback()  
        print("Error during insert:", e)  