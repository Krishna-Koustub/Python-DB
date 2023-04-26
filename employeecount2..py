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

sql = "select count(*) from employees"

try:
     cur.execute(sql)
     row_count = cur.fetchone()[0]
     print("row_count = ",row_count)

except:
     print("Unable to fetch data ...")


db.close()