#!/usr/local/bin/python3.11

import cgi
import json
import mysql.connector



form = cgi.FieldStorage()
currentpage = str(form.getvalue('currentpage'))
itemperpage = str(form.getvalue('itemperpage'))
#category =  form.getvalue('category')
#comment =  form.getvalue('description')
#comment =  form.getvalue('title')


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="Blog"
)

cursor = conn.cursor()


cursor.execute("SELECT * FROM `article` WHERE `number` > ("+  currentpage  +"-1)*"+   itemperpage    +" LIMIT "+     itemperpage    +";")
result = cursor.fetchall()


conn.commit()


rows_as_dict = []
for row in result:
    row_dict = {
        'number': row[0], 
        'category': row[1],
        'title': row[2],
        'date': row[3],
        'description': row[4],
        'image': row[5]
    }
    rows_as_dict.append(row_dict)

json_data = json.dumps(rows_as_dict)

cursor.close()
conn.close()

print("Content-Type: text/html\n\n")
print(json_data)




