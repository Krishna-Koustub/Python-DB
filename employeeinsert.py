import mysql.connector as mysql
db = mysql.connect(
    port="3306",
    host="localhost",
    user="root",
    passwd="Kk@100202",
    database="matrossbear"
)

print("Database connection success")

sql = "insert into employees (employee_id, name, gender, email) values(%s, %s, %s, %s)"
value = (401,'Ahmad','M','ahmad@gmail.com')

cur = db.cursor()

try:
     cur.execute(sql, value)
     db.commit()
     print("Insert success ...")

except mysql.Error as e:
     print("Insert error " + e)

db.close()