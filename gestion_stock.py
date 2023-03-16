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

def show_products():
    window = Toplevel(height=400, width=650)

    # Frame BDD
    frame = tk.Frame(root)
    frame.pack()

    bd_info = tk.LabelFrame(window, text="Base de données", font=('Arial', 10, 'bold'))
    bd_info.pack(pady=30, ipadx=10, ipady=10)

    # Texte dans la frame BDD
    # bd_info2 = tk.Label(bd_info, text="Titre")
    # bd_info2.pack()

    # Frame Produits

    bd_info3 = tk.LabelFrame(bd_info, text="Produits", fg='green', font=('Arial', 10, 'bold'))
    bd_info3.pack()

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

    bd_info9 = tk.Label(bd_info3, text="ID Catégorie", fg='green')
    bd_info9.grid(row=3, column=5)

    # Affiche produits en tableau
    cursor.execute("SELECT * FROM produit limit 0,10")
    i=0 
    for produit in cursor:
        for j in range(len(produit)):
            produit_entry = Text(bd_info3, width=12, fg='black', height=1) 
            produit_entry.grid(row=i, column=j)
            produit_entry.insert(END, produit[j]) # Ecrit le nom du produit dans l'entry
            produit_entry.config()
        i += 1

    # Catégories
    bd_info4 = tk.LabelFrame(bd_info, text="Catégories", fg='blue', font=('Arial', 10, 'bold'))
    bd_info4.pack()

    # Affiche catégories en tableau
    cursor.execute("SELECT * FROM categorie limit 0,10")
    i=0 
    for categorie in cursor:
        for j in range(len(categorie)):
            categorie_entry = Text(bd_info4, width=20, fg='black', height=1) 
            categorie_entry.grid(row=i, column=j)
            categorie_entry.insert(END, categorie[j])
        i += 1

# Afficher les produits
show_product = Button(root, text='Afficher les produits', padx=10, pady=10, command=show_products)
show_product.pack(pady=70)

# Actions
buttons = tk.Frame(root)
buttons.pack()

actions = tk.LabelFrame(buttons, text="Actions", font=('Arial', 10, 'bold'))
actions.pack(pady=20)

# Entry Actions
add = Entry(actions, justify=CENTER, border=4)
add.grid(row=0, column=0)

delete = Entry(actions, justify=CENTER, border=4)
delete.grid(row=0, column=1)

modif = Entry(actions, justify=CENTER, border=4)
modif.grid(row=0, column=2)

# Boutons et fonctions de la frame Actions
def func_add_product():
    query = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('Maraiste', 'Petit bonhomme', 500, 1, 1), ('Clavier', 'Matériel', 150, 5, 2);"
    cursor.execute(query)
    bd.commit()
    print(add.get())
    # cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('Piano', 'Instrument de musique', 500, 1, 1), ('Ordinateur', 'Informatique', 1500, 3, 2);")
    # bd.commit()

def func_delete_product():
    delete.delete(0, END)

def func_modif_product():
    pass
    # Get l'entry, get l'ID dans le tableau Produit, et modifier le produit par l'entry.

# Boutons et fonctions de la frame Actions
add_product = Button(actions, text='Ajouter un produit', padx=10, pady=10, command=func_add_product)
add_product.grid(row=1, column=0, padx=10, pady=10)

delete_product = Button(actions, text='Supprimer un produit', padx=10, pady=10, command=func_delete_product)
delete_product.grid(row=1, column=1, padx=10, pady=10)

modif_product = Button(actions, text='Modifier un produit', padx=10, pady=10, command=func_modif_product)
modif_product.grid(row=1, column=2, padx=10, pady=10)

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