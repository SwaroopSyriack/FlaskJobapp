from sqlalchemy import create_engine,text
from sqlalchemy.engine import result
from sqlalchemy.engine.interfaces import ReflectedCheckConstraint
data_con = "mysql+pymysql://2vz9oPmQ7SZb6cW.root:MIzOz5e0BdcVq8vv@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/test?charset=utf8mb4"



engine = create_engine(data_con,connect_args={
"ssl" : {
    "ca": "isrgrootx1.pem"
}
  
})

def load_jobs_from_db():
  with engine.connect() as con:
    rel = con.execute(text("Select * from jobs"))
    col = rel.keys()
    rows = rel.fetchall()
  return [dict(zip(col, row)) for row in rows]

def load_job_from_db(id):
  with engine.connect() as con:
    rels = con.execute(text("select * from jobs where id = :val"),{"val":id})
  rows = rels.all()
  cols = rels.keys()
  print(rows)
  if len(rows) == 0:
    return None
  else:

    return dict(zip(cols, rows[0]))
    
def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO application(jobid, fullname, email, linkedin_url, education, work_experience, resume_url) VALUES (:jobid, :fullname, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query, 
       {   'jobid': job_id['id'], 
           'fullname': data['full_name'],
           'email': data['email'],
           'linkedin_url': data['linkedin_url'],
           'education': data['education'],
           'work_experience': data['work_experience'],
           'resume_url': data['resume_url']
       })






