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
root.geometry('650x430')

def show_products():
    window = Toplevel(height=400, width=650)

    # Frame BDD
    frame = tk.Frame(root)
    frame.pack()

    bd_info = tk.LabelFrame(window, text="Base de données", fg='DarkOrange2', font=('Arial', 10, 'bold'))
    bd_info.pack(pady=50, padx=50, ipadx=10, ipady=10)

    # Texte dans la frame BDD
    # bd_info2 = tk.Label(bd_info, text="Titre")
    # bd_info2.pack()

    # Frame Produits

    bd_info3 = tk.LabelFrame(bd_info, text="Produits", fg='dodger blue', font=('Arial', 10, 'bold'))
    bd_info3.pack()

    # Infos produits: ID, nom, description, prix, quantité, categorie
    bd_info2 = tk.Label(bd_info3, text="ID", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info2.grid(row=0, column=0, pady=5)

    bd_info5 = tk.Label(bd_info3, text="Nom", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info5.grid(row=0, column=1, pady=5)

    bd_info6 = tk.Label(bd_info3, text="Description", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info6.grid(row=0, column=2, pady=5)

    bd_info7 = tk.Label(bd_info3, text="Prix", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info7.grid(row=0, column=3, pady=5)

    bd_info8 = tk.Label(bd_info3, text="Quantité", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info8.grid(row=0, column=4, pady=5)

    bd_info9 = tk.Label(bd_info3, text="ID Catégorie", fg='green4', font=('Tahoma', 10, 'bold'))
    bd_info9.grid(row=0, column=5, pady=5)

    # Affiche produits en tableau
    cursor.execute("SELECT * FROM produit limit 0,10")
    i=1
    for product in cursor:
        for j in range(len(product)):
            product_entry = Text(bd_info3, width=12, fg='black', font=('Tahoma', 10, 'bold'), height=1) 
            product_entry.grid(row=i, column=j)
            product_entry.insert(END, product[j]) # Ecrit le nom du produit dans l'entry
            product_entry.config()
        i += 1

    # Catégories
    bd_info4 = tk.LabelFrame(bd_info, text="Catégories", fg='dodger blue', font=('Arial', 10, 'bold'))
    bd_info4.pack()

    # Affiche catégories en tableau
    cursor.execute("SELECT * FROM categorie limit 0,10")
    i=0 
    for category in cursor:
        for j in range(len(category)):
            category_entry = Text(bd_info4, width=20, fg='black', font=('Tahoma', 10, 'bold'), height=1) 
            category_entry.grid(row=i, column=j)
            category_entry.insert(END, category[j])
        i += 1

# Afficher les produits
show_product = Button(root, text='Afficher les produits', padx=10, pady=10, bg='SpringGreen4', activebackground='SpringGreen4', activeforeground='black', font=('Tahoma', 8, 'bold'), command=show_products)
show_product.pack(pady=10)

# Actions
actions = tk.LabelFrame(root, text='Actions', font=('Arial', 10, 'bold'))
actions.pack()

def click_name(event):
    name_entry.config(state=NORMAL)
    name_entry.delete(0, END)

def click_desc(event):
    desc_entry.config(state=NORMAL)
    desc_entry.delete(0, END)

def click_prix(event):
    price_entry.config(state=NORMAL)
    price_entry.delete(0, END)

def click_quantite(event):
    quantity_entry.config(state=NORMAL)
    quantity_entry.delete(0, END)

def click_id_category(event):
    id_category_entry.config(state=NORMAL)
    id_category_entry.delete(0, END)

def click_delete(event):
    delete.config(state=NORMAL)
    delete.delete(0, END)

def click_modif(event):
    modif.config(state=NORMAL)
    modif.delete(0, END)

# Entry Actions
name_entry = Entry(actions, justify=CENTER, border=4)
name_entry.insert(0, 'Nom')
name_entry.config(state=DISABLED)
name_entry.bind("<Button-1>", click_name)
name_entry.grid(row=0, column=0)

desc_entry = Entry(actions, justify=CENTER, border=4)
desc_entry.insert(0, 'Description')
desc_entry.config(state=DISABLED)
desc_entry.bind("<Button-1>", click_desc)
desc_entry.grid(row=1, column=0, pady=10)

price_entry = Entry(actions, justify=CENTER, border=4)
price_entry.insert(0, 'Prix')
price_entry.config(state=DISABLED)
price_entry.bind("<Button-1>", click_prix)
price_entry.grid(row=2, column=0, pady=10)

quantity_entry = Entry(actions, justify=CENTER, border=4)
quantity_entry.insert(0, 'Quantité')
quantity_entry.config(state=DISABLED)
quantity_entry.bind("<Button-1>", click_quantite)
quantity_entry.grid(row=3, column=0, pady=10)

id_category_entry = Entry(actions, justify=CENTER, border=4)
id_category_entry.insert(0, 'ID Categorie')
id_category_entry.config(state=DISABLED)
id_category_entry.bind("<Button-1>", click_id_category)
id_category_entry.grid(row=4, column=0, pady=10)

# Entry pour les modifications
name_entry2 = Entry(actions, justify=CENTER, border=4)
name_entry2.insert(0, 'Nom')
name_entry2.config(state=DISABLED)
name_entry2.bind("<Button-1>", click_name)
name_entry2.grid(row=0, column=2)

desc_entry2 = Entry(actions, justify=CENTER, border=4)
desc_entry2.insert(0, 'Description')
desc_entry2.config(state=DISABLED)
desc_entry2.bind("<Button-1>", click_desc)
desc_entry2.grid(row=1, column=2, pady=10)

price_entry2 = Entry(actions, justify=CENTER, border=4)
price_entry2.insert(0, 'Prix')
price_entry2.config(state=DISABLED)
price_entry2.bind("<Button-1>", click_prix)
price_entry2.grid(row=2, column=2, pady=10)

quantity_entry2 = Entry(actions, justify=CENTER, border=4)
quantity_entry2.insert(0, 'Quantité')
quantity_entry2.config(state=DISABLED)
quantity_entry2.bind("<Button-1>", click_quantite)
quantity_entry2.grid(row=3, column=2, pady=10)

id_category_entry = Entry(actions, justify=CENTER, border=4)
id_category_entry.insert(0, 'ID Categorie')
id_category_entry.config(state=DISABLED)
id_category_entry.bind("<Button-1>", click_id_category)
id_category_entry.grid(row=4, column=2, pady=10)

delete = Entry(actions, justify=CENTER, border=4)
delete.insert(0, 'ID du produit')
delete.config(state=DISABLED)
delete.bind("<Button-1>", click_delete)
delete.grid(row=0, column=1)

modif = Entry(actions, justify=CENTER, border=4)
modif.insert(0, 'ID Categorie')
modif.config(state=DISABLED)
modif.bind("<Button-1>", click_modif)
modif.grid(row=0, column=2)

# Boutons et fonctions de la frame Actions
def func_add_product():
    # récupère tous les entry
    name = name_entry.get()
    description = desc_entry.get()
    prix = price_entry.get()
    quantite = quantity_entry.get()
    id_category = id_category_entry.get()
    # requête pour ajouter un nouveau produit dans la table produit
    query = f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('{name}', '{description}', '{prix}', '{quantite}', '{id_category}');"
    cursor.execute(query) # exécuter la requête
    bd.commit() # commit dans la BDD
    print(name_entry.get(), desc_entry.get(), price_entry.get(), quantity_entry.get(), id_category_entry.get())

def func_delete_product():
    product = delete.get() # product = entry supprimer
    query = f"DELETE FROM produit where id = {product};" # supprimer dans la table produit ou l'id = product
    cursor.execute(query)
    bd.commit()

def func_modif_product():
    pass
    # Get l'entry, get l'ID dans le tableau Produit, et modifier le produit par l'entry.

# Boutons et fonctions de la frame Actions
add_product = Button(actions, text='Ajouter un produit', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_add_product)
add_product.grid(row=6, column=0, padx=10, pady=10)

delete_product = Button(actions, text='Supprimer un produit', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_delete_product)
delete_product.grid(row=1, column=1, padx=10, pady=10)

modif_product = Button(actions, text='Modifier un produit', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_modif_product)
modif_product.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()

# Créer une base de données namemée “boutique” et les tables “produit” et “categorie”.
query = "CREATE DATABASE boutique;"
query2 = "USE boutique;"

# Crée la table produit
query3 = "CREATE TABLE produit (id INT primary key auto_increment, name VARCHAR(255), \
    description text, prix int, quantite int, id_categorie int);"

# Crée la table categorie
query4 = "CREATE TABLE categorie (id INT primary key auto_increment, name VARCHAR(255));"

# Insertion de produits dans la table produit
query5 = "INSERT INTO produit (name, description, prix, quantite, id_categorie) VALUES ('Piano', 'Instrument de musique', 500, 1, 1), ('Ordinateur', 'Informatique', 1500, 3, 2);"

# Insertion de categories dans la table categorie
query6 = "INSERT INTO categorie (name) VALUES ('Instrument à clavier');"
query7 = "INSERT INTO categorie (name) VALUES ('Informatique');"

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
# | id | name        | description           | prix | quantite | id_categorie |
# +----+------------+-----------------------+------+----------+--------------+
# |  1 | Piano      | Instrument de musique |  500 |        1 |            1 |
# |  2 | Ordinateur | Informatique          | 1500 |        3 |            2 |
# +----+------------+-----------------------+------+----------+--------------+