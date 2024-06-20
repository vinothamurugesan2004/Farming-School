#!C:\python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

Form=cgi.FieldStorage()
FName=Form.getvalue('name')
FAge=Form.getvalue('age')
FPhoneNumber=Form.getvalue('phone')
FEmailAddress=Form.getvalue('email')
FGender=Form.getvalue('gender')
FAddress=Form.getvalue('address')
FEducation=Form.getvalue('education')
FVisitor=Form.getvalue('visitor')


print("<h1><center>Thankyou For Register...</center></h1>")
print("<h2>This the data you entered:</h2>")
print(FName,FAge,FPhoneNumber,FEmailAddress,FGender,FAddress,FEducation,FVisitor)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="farming"
)

mycursor=mydb.cursor()

sql="INSERT INTO student(Name,Age,PhoneNumber,EmailAddress,Gender,Address,Education,Visitor)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
val=(FName,FAge,FPhoneNumber,FEmailAddress,FGender,FAddress,FEducation,FVisitor)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")