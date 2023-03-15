import mysql.connector
from tkinter import * 
import tkinter as tk

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="boutique"
)

cursor = bd.cursor()

root = tk.Tk()

root.title("Gestion de stock")
root.geometry('650x400')

frame = tk.Frame(root)
frame.pack()

bd_info = tk.LabelFrame(frame, text="Base de données", font=('Arial', 10, 'bold'))
bd_info.pack(pady=100)

# Texte dans la frame BDD
# bd_info2 = tk.Label(bd_info, text="Titre")
# bd_info2.pack()

bd_info3 = tk.LabelFrame(bd_info, text="Produits", fg='green', font=('Arial', 10, 'bold'))

# Infos produits: ID, Nom, description, prix, quantité, categorie
bd_info2 = tk.Label(bd_info3, text="ID", fg='green')
bd_info2.grid(row=3, column=0)

bd_info5 = tk.Label(bd_info3, text="Nom", fg='green')
bd_info5.grid(row=3, column=1)

bd_info6 = tk.Label(bd_info3, text="Description", fg='green')
bd_info6.grid(row=3, column=2)

bd_info7 = tk.Label(bd_info3, text="Prix", fg='green')
bd_info7.grid(row=3, column=3)

bd_info8 = tk.Label(bd_info3, text="Quantité", fg='green')
bd_info8.grid(row=3, column=4)

bd_info9 = tk.Label(bd_info3, text="Catégorie", fg='green')
bd_info9.grid(row=3, column=5)

bd_info3.pack()
cursor.execute("SELECT * FROM produit limit 0,10")
i=0 
for produit in cursor:
    for j in range(len(produit)):
        produit_entry = Entry(bd_info3, width=15, fg='black', justify=CENTER, background="white") 
        produit_entry.grid(row=i, column=j)
        produit_entry.insert(END, produit[j]) # Ecrit le nom du produit dans l'entry
    i=i+1

bd_info4 = tk.LabelFrame(bd_info, text="Catégories", font=('Arial', 10, 'bold'))
bd_info4.pack()
cursor.execute("SELECT * FROM categorie limit 0,10")
i=0 
for categorie in cursor:
    for j in range(len(categorie)):
        categorie_entry = Entry(bd_info4, width=18, fg='black', justify=CENTER) 
        categorie_entry.grid(row=i, column=j)
        categorie_entry.insert(END, categorie[j])
    i=i+1

root.mainloop()

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

bd.commit()

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