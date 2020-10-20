import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT unit.name FROM `unit`")

for x in mycursor:
  print(x)