import mysql.connector

name = input('Please enter the job\'s name : ')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

sql = "SELECT job.name, unit.name FROM `job` INNER JOIN `unit` ON job.unit_fk = unit.id WHERE job.name LIKE '"+ name +"'"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
  print(x)
