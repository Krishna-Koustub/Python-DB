import MySQL.connector as mdb

DBNAME = "krishna"
DBHOST = "localhost"
DBUSER = "root"
DBPASS = "Kk@100202"

db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
print("Database connection success")

sql = "insert into employees (employee_id, name, gender, email) values(%s, %s, %s, %s)"
value = (401,'Ahmad','M','ahmad@gmail.com')

cur = db.cursor()

try:
     cur.execute(sql, value)
     db.commit()
     print("Insert success ...")

except mdb.Error as e:
     print("Insert error " + e)

db.close() 