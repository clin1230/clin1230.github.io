#!/usr/local/bin/python3.11

import cgi
import json
import mysql.connector
import math



form = cgi.FieldStorage()

#itemperpage = str(form.getvalue('itemperpage'))
itemperpage = 5


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="Blog"
)

cursor = conn.cursor()


cursor.execute("SELECT COUNT(*) FROM `article`;")
result = cursor.fetchall()

conn.commit()



total=result[0][0]
pagenumber=math.ceil(total/itemperpage)



cursor.close()
conn.close()


print("Content-Type: text/html\n\n")
print(pagenumber)




