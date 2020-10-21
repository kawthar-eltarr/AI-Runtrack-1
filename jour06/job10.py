import mysql.connector

group_by = input('Please enter a group id : ')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laplateforme"
)

mycursor = mydb.cursor()

sql = "SELECT job.name FROM `job` INNER JOIN `registration` ON job.id = registration.job_fk WHERE registration.group_id = '" + group_by + "'"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
  print(x)
