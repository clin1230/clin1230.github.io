#!/usr/local/bin/python3.11

import cgi
import json
import mysql.connector

form = cgi.FieldStorage()
fname =  form.getvalue('fname')
email =  form.getvalue('email')
comment =  form.getvalue('comment')


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="Tina"
)


cursor = conn.cursor()

SQLcommand = "INSERT INTO `comment` (`person_name`, `person_email`, `person_comment`) VALUES ('" + fname  +  "','" + email + "','" + comment + "');"
cursor.execute(SQLcommand)

conn.commit()


#cursor.execute("SELECT * FROM `comment`;")
#result = cursor.fetchall()

# rows_as_dict = []
# for row in result:
#     row_dict = {
#         'person_name': row[0], 
#         'person_email': row[1],
#         'person_comment': row[2]
#     }
#     rows_as_dict.append(row_dict)

# json_data = json.dumps(rows_as_dict, indent=3)

cursor.close()
conn.close()

print("Content-Type: text/html\n\n")
#print(json_data)




