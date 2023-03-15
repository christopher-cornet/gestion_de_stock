import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="boutique"
)

cursor = bd.cursor()

# Créer une base de données nommée “boutique” et les tables “produit” et “categorie”.
query = "CREATE DATABASE boutique;"
query2 = "USE boutique;"

# Crée la table produit
query3 = "CREATE TABLE produit (id INT primary key auto_increment, nom VARCHAR(255), \
    description text, prix int, quantite int, id_categorie int);"

# Crée la table categorie
query4 = "CREATE TABLE categorie (id INT primary key auto_increment, nom VARCHAR(255));"

# Insertion de produits dans la table produit
query5 = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('Piano', 'Instrument de musique', 500, 1, 1), ('Ordinateur', 'Informatique', 1500, 3, 2);"

# Insertion de categories dans la table categorie
query6 = "INSERT INTO categorie (nom) VALUES ('Instrument à clavier');"
query7 = "INSERT INTO categorie (nom) VALUES ('Informatique');"

cursor.execute(query)

cursor.close()

# Insérer des produits dans la table “produits” et différentes catégories.

# À l’aide de l’interface graphique de votre choix, créer un tableau de bord, permettant la
# gestion des stocks.

# Sur le tableau de bord, la liste complète des produits en stock sont affichés. L’utilisateur
# doit avoir la possibilité d’ajouter un produit, de supprimer un produit et de modifier le
# produit (stock, prix, ...).



# Table produit:
# +----+------------+-----------------------+------+----------+--------------+
# | id | nom        | description           | prix | quantite | id_categorie |
# +----+------------+-----------------------+------+----------+--------------+
# |  1 | Piano      | Instrument de musique |  500 |        1 |            1 |
# |  2 | Ordinateur | Informatique          | 1500 |        3 |            2 |
# +----+------------+-----------------------+------+----------+--------------+