import mysql.connector

name = input('Please enter the author\'s name : ')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="runtrack1"
)

mycursor = mydb.cursor()

sql = "SELECT livre.titre FROM `livre` INNER JOIN `auteur` ON livre.auteur_id = auteur.id WHERE auteur.nom LIKE '%" + name + "%' OR auteur.prenom LIKE '%" + name + "%'"

mycursor.execute(sql)
result = mycursor.fetchall()

for l in result:
    print(l)

