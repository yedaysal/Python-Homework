#--------Retrieving and printing the number of students whose age is grater than 20--------#
import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM STUDENTS WHERE AGE > '%d'" % (20)

counter = 0

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:

        counter=counter+1

except:
    print("Error:Unable to fetch data")

print("Number of students whose age are grater than 20 is = {}".format(counter))

db.close()