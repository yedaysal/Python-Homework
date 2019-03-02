#--------Reading XML file and parsing it--------#
import os
from xml.etree import ElementTree
import pymysql

file_name = 'students.xml'
xml_file = os.path.abspath(os.path.join(file_name))
dom = ElementTree.parse(xml_file)
root = dom.getroot()

IDs=[]
Names = []
Ages = []
GPAs = []

for child in root:

    id = child.attrib
    IDs.append(id['id'])

    for element in child:

        if (element.tag == 'name'):
            Names.append(element.text)
        elif(element.tag == 'age'):
            Ages.append(int(element.text))
        elif(element.tag == 'gpa'):
            GPAs.append(float(element.text))

#--------Inserting all students into the database one-by-one--------#

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(0,len(IDs)):

    # Prepare SQL query to insert a record into the database
    sql = """INSERT INTO STUDENTS(ID,NAME,AGE,GPA)
          VALUES('%s','%s','%d','%.2f')""" % (IDs[i],Names[i],Ages[i],GPAs[i])

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

    except:
        # Rollback in case there is any error
        db.rollback()

# Disconnect from server
db.close()
