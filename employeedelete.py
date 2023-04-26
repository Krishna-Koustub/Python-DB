import mysql.connector as mysql
db = mysql.connect(
    port="3306",
    host="localhost",
    user="root",
    passwd="Kk@100202",
    database='matrossbear'
)

print("Database connection success")

cur = db.cursor()

sql = "delete from employees where employee_id = %s";
value = (102,)

try:
     cur.execute(sql, value)
     db.commit()
     print('Row deleted successfully ...')

except:
     print("Unable to delete the row ...")

db.close()