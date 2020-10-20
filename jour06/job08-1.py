import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT student.id, count(id) FROM `student` GROUP by `promotion_fk`")

for x in mycursor:
  print(x)
