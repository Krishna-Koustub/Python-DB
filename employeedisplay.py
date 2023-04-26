import mysql.connector as mysql
db = mysql.connect(
    port="3306",
    host="localhost",
    user="root",
    passwd="Kk@100202",
    database="matrossbear"
)
print("Database connection success")

cur = db.cursor()

sql = "select * from employees"

try:
     cur.execute(sql)
     results = cur.fetchall()
     for row in results :
         employeeId = row[0]
         name = row[1]
         gender = row[2]
         email = row[3]
      
         print(employeeId,name, gender, email)
except:
     print("Unable to fetch data ...")


db.close()