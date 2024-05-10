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







