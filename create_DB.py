#--------Creating a database--------#
import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS STUDENTS")

# Create table as per requirement
sql = """CREATE TABLE STUDENTS (
         ID  CHAR(20) NOT NULL,
         NAME  CHAR(100),
         AGE INT,  
         GPA FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()