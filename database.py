from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://root:root@localhost:3306/joviancareers'
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs