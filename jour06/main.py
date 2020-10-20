import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="runtrack1"
)

mycursor = mydb.cursor()

auteurs = [("Smith", "John"), ("Chaouati","Sarah"), ("Caillat","Clément"), ("Dupond", "Martin"), ("Collas", "Pauline")]
for a in auteurs:
     sql = "INSERT INTO auteur (nom, prenom) VALUES (%s, %s)"
     mycursor.execute(sql, a)

livres = [("Toto à l'école", 2), ("Jacky et le monstre", 2), ("Kawthar mange le couscous", 1), ("Martine en a marre de la COVID", 4), ("Sarah et le sommeil pesant", 3)]

for l in livres:
    sql = "INSERT INTO livre (titre, auteur_id) VALUES (%s, %s)"
    mycursor.execute(sql, l)

mydb.commit()

