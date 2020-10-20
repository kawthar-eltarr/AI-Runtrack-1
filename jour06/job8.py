import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT unit.name FROM `unit` WHERE unit.name LIKE '%Pool%'")

for x in mycursor:
  print(x)