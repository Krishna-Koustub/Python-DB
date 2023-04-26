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
employeeId = 101

sql = "select * from employees where employee_id =%s";

try:
     value = (employeeId,)
     n = cur.execute(sql,value)
     if n > 0:
        row = cur.fetchone()
        print(row[0],row[1],row[2],row[3])

except:
     print("Unable to select the row ...")

db.close()