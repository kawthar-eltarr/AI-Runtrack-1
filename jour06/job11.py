import mysql.connector

student_id = input('Please enter a student id : ')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

sql = "SELECT unit.name FROM `unit` INNER JOIN `student` ON unit.id = student.current_unit_fk WHERE student.id = '" + student_id + "'"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
  print(x)
