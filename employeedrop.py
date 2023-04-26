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

sql = "drop table if exists employees";

try:
     cur.execute(sql)
     db.commit()
     print('Table dropped successfully ...')

except:
     print("Unable to drop the table/table not found")

db.close()