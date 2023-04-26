
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

sql = "update employees set email = %s where employee_id = %s";
value = ("johnxyz@gmail.com",101)

try:
     cur.execute(sql, value)
     db.commit()
     print('Table updated successfully ...')

except mdb.Error as e:
     print("Unable to update table ..." + e)

db.close()

