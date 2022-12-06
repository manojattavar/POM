import cx_Oracle

con = cx_Oracle.connect("connection string")
cursor = con.cursor()

cursor.execute("insert into tableName values('', '')")

cursor.execute("select * from employee")

for i in range(0, len(cursor)):
    print(cursor[i])