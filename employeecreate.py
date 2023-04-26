import mysql.connector as mysql
db = mysql.connect(
    port="3306",
    host="localhost",
    user="root",
    passwd="Kk@100202",
    database="matrossbear"
)

try:
     
     print("Database connection success")

     cur = db.cursor()
     cur.execute("DROP TABLE IF EXISTS EMPLOYEE")

     sql = """create table employees(
             employee_id int(3),
             name varchar(15),
             gender varchar(1),
             email varchar(30),
             primary key (employee_id)) engine=innodb"""
     
     cur.execute(sql)
     print("Table created successfully")

except mysql.Error as e:
     print("Table creation problem")

