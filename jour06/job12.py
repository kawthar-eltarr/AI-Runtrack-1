import mysql.connector

group_id = input('Please enter a group id : ')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

sql = "SELECT job.name, unit.name FROM `job` INNER JOIN `registration` ON job.id = registration.job_fk INNER JOIN `unit` ON job.unit_fk = unit.id WHERE registration.group_id = '" + group_id + "'"
mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
  print(x)
  

