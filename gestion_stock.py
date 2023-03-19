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

# Centrer la fenêtre
appwidth = 1350
appheight = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = (screenwidth / 2) - (appwidth / 2)
y = (screenheight / 2) - (appheight / 2)

root.title("Gestion de stock")
root.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')

def show_products():
    # Centrer la fenêtre
    appwidth = 1000
    appheight = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = (screenwidth / 2) - (appwidth / 2)
    y = (screenheight / 2) - (appheight / 2)
    window = Toplevel()
    window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')

    # Frame BDD
    frame = tk.Frame(root)
    frame.pack()

    bd_info = tk.LabelFrame(window, text="Base de données", fg='DarkOrange2', font=('Arial', 10, 'bold'))
    bd_info.pack(pady=50, padx=50, ipadx=10, ipady=10)

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

frame = tk.Frame(root)
frame.pack()

bd_info = tk.LabelFrame(root, text="Base de données", fg='DarkOrange2', font=('Arial', 10, 'bold'))
bd_info.pack(pady=50, padx=50, ipadx=10, ipady=10)

# Afficher les produits
show_product = Button(bd_info, text='Afficher les produits et catégories', padx=10, pady=10, bg='SpringGreen4', activebackground='SpringGreen4', activeforeground='black', font=('Tahoma', 8, 'bold'), command=show_products)
show_product.grid(row=0, column=0)

# Actions produits
actions = tk.LabelFrame(bd_info, text='Actions produits', fg='dodger blue', font=('Arial', 10, 'bold'))
actions.grid(row=1, column=0)

# Actions catégories
actions_cat = tk.LabelFrame(bd_info, text='Actions catégories', fg='dodger blue', font=('Arial', 10, 'bold'))
actions_cat.grid(row=1, column=1)

# Clique sur les entry colonne1 (ajout produit)
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

def click_edit(event):
    edit.config(state=NORMAL)
    edit.delete(0, END)

# Clique sur les entry colonne3 (modif produit)
def click_name2(event):
    name_entry2.config(state=NORMAL)
    name_entry2.delete(0, END)

def click_desc2(event):
    desc_entry2.config(state=NORMAL)
    desc_entry2.delete(0, END)

def click_prix2(event):
    price_entry2.config(state=NORMAL)
    price_entry2.delete(0, END)

def click_quantite2(event):
    quantity_entry2.config(state=NORMAL)
    quantity_entry2.delete(0, END)

def click_id_category2(event):
    id_category_entry2.config(state=NORMAL)
    id_category_entry2.delete(0, END)

def click_edit2(event):
    edit.config(state=NORMAL)
    edit.delete(0, END)

# Entry Actions
name_entry = Entry(actions, justify=CENTER, border=4)
name_entry.insert(0, 'Nom*')
name_entry.config(state=DISABLED)
name_entry.bind("<Button-1>", click_name)
name_entry.grid(row=0, column=0)

desc_entry = Entry(actions, justify=CENTER, border=4)
desc_entry.insert(0, 'Description*')
desc_entry.config(state=DISABLED)
desc_entry.bind("<Button-1>", click_desc)
desc_entry.grid(row=1, column=0, pady=10)

price_entry = Entry(actions, justify=CENTER, border=4)
price_entry.insert(0, 'Prix*')
price_entry.config(state=DISABLED)
price_entry.bind("<Button-1>", click_prix)
price_entry.grid(row=2, column=0, pady=10)

quantity_entry = Entry(actions, justify=CENTER, border=4)
quantity_entry.insert(0, 'Quantité*')
quantity_entry.config(state=DISABLED)
quantity_entry.bind("<Button-1>", click_quantite)
quantity_entry.grid(row=3, column=0, pady=10)

id_category_entry = Entry(actions, justify=CENTER, border=4)
id_category_entry.insert(0, 'ID Categorie*')
id_category_entry.config(state=DISABLED)
id_category_entry.bind("<Button-1>", click_id_category)
id_category_entry.grid(row=4, column=0, pady=10)

# Entry pour les modifications
name_entry2 = Entry(actions, justify=CENTER, border=4)
name_entry2.insert(0, 'Nom')
name_entry2.config(state=DISABLED)
name_entry2.bind("<Button-1>", click_name2)
name_entry2.grid(row=1, column=2)

desc_entry2 = Entry(actions, justify=CENTER, border=4)
desc_entry2.insert(0, 'Description')
desc_entry2.config(state=DISABLED)
desc_entry2.bind("<Button-1>", click_desc2)
desc_entry2.grid(row=2, column=2, pady=10)

price_entry2 = Entry(actions, justify=CENTER, border=4)
price_entry2.insert(0, 'Prix')
price_entry2.config(state=DISABLED)
price_entry2.bind("<Button-1>", click_prix2)
price_entry2.grid(row=3, column=2, pady=10)

quantity_entry2 = Entry(actions, justify=CENTER, border=4)
quantity_entry2.insert(0, 'Quantité')
quantity_entry2.config(state=DISABLED)
quantity_entry2.bind("<Button-1>", click_quantite2)
quantity_entry2.grid(row=4, column=2, pady=10)

id_category_entry2 = Entry(actions, justify=CENTER, border=4)
id_category_entry2.insert(0, 'ID Categorie')
id_category_entry2.config(state=DISABLED)
id_category_entry2.bind("<Button-1>", click_id_category2)
id_category_entry2.grid(row=5, column=2, pady=10)

# Entry supprimer un produit
delete = Entry(actions, justify=CENTER, border=4)
delete.insert(0, 'ID du produit*')
delete.config(state=DISABLED)
delete.bind("<Button-1>", click_delete)
delete.grid(row=0, column=1)

# Entry ID du produit à modifier
edit = Entry(actions, justify=CENTER, border=4)
edit.insert(0, 'ID du produit*')
edit.config(state=DISABLED)
edit.bind("<Button-1>", click_edit)
edit.grid(row=0, column=2)

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

def func_delete_product():
    product = delete.get() # product = entry supprimer
    query = f"DELETE FROM produit WHERE id = {product};" # supprimer dans la table produit ou l'id = product
    cursor.execute(query)
    bd.commit()

def func_edit_product():
    id = edit.get()
    name = name_entry2.get()
    desc = desc_entry2.get()
    price = price_entry2.get()
    quantity = quantity_entry2.get()
    idcat = id_category_entry2.get()
    query = f"UPDATE produit SET nom = '{name}', description = '{desc}', prix = {price}, quantite = {quantity}, id_categorie = {idcat} where id = {id};"
    cursor.execute(query)
    bd.commit()

def edit_name():
    id = edit.get()
    name = name_entry2.get()
    query = f"UPDATE produit SET nom = '{name}' WHERE id = '{id}';" # modifier le nom d'un produit
    cursor.execute(query)
    bd.commit()

def edit_desc():
    id = edit.get()
    desc = desc_entry2.get()
    query = f"UPDATE produit SET description = '{desc}' WHERE id = '{id}';" # modifier la description d'un produit
    cursor.execute(query)
    bd.commit()

def edit_price():
    id = edit.get()
    price = price_entry2.get()
    query = f"UPDATE produit SET prix = '{price}' WHERE id = '{id}';" # modifier le prix d'un produit
    cursor.execute(query)
    bd.commit()

def edit_quantity():
    id = edit.get()
    quantity = quantity_entry2.get()
    query = f"UPDATE produit SET quantite = '{quantity}' WHERE id = '{id}';" # modifier la quantité d'un produit
    cursor.execute(query)
    bd.commit()

def edit_id_categorie():
    id = edit.get()
    idcat = id_category_entry2.get()
    query = f"UPDATE produit SET id_categorie = '{idcat}' WHERE id = '{id}';" # modifier l'ID de la catégorie d'un produit
    cursor.execute(query)
    bd.commit()

# Boutons et fonctions de la frame Actions
add_product = Button(actions, text='Ajouter un produit', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_add_product)
add_product.grid(row=5, column=0, padx=10, pady=10)

delete_product = Button(actions, text='Supprimer un produit', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_delete_product)
delete_product.grid(row=1, column=1, padx=10, pady=10)

edit_product = Button(actions, text='Tout modifier', padx=10, pady=10, bg='DarkOrange2', activebackground='DarkOrange2', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_edit_product)
edit_product.grid(row=0, column=3, padx=10, pady=10)

edit_product = Button(actions, text='Modifier le nom', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=edit_name)
edit_product.grid(row=1, column=3, padx=10, pady=10)

edit_product2 = Button(actions, text='Modifier la description', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=edit_desc)
edit_product2.grid(row=2, column=3, padx=10, pady=10)

edit_product3 = Button(actions, text='Modifier le prix', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=edit_price)
edit_product3.grid(row=3, column=3, padx=10, pady=10)

edit_product4 = Button(actions, text='Modifier la quantité', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=edit_quantity)
edit_product4.grid(row=4, column=3, padx=10, pady=10)

edit_product5 = Button(actions, text="Modifier l'ID catégorie", padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=edit_id_categorie)
edit_product5.grid(row=5, column=3, padx=10, pady=10)

# Frame catégories
def adding_categorie():
    id = id_categorie.get()
    nom = name_categorie.get()
    # requête pour ajouter un nouveau produit dans la table produit
    query = f"INSERT INTO categorie (id, nom) VALUES ('{id}', '{nom}');"
    cursor.execute(query) # exécuter la requête
    bd.commit() # commit dans la BDD

def func_delete_categorie():
    id = del_categorie.get()
    query = f"DELETE FROM categorie WHERE id = {id};" # supprimer dans la table produit ou l'id = product
    cursor.execute(query)
    bd.commit()
    
add_categorie = Button(actions_cat, text='Ajouter une catégorie', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=adding_categorie)
add_categorie.grid(row=5, column=0, padx=10, pady=10)

delete_categorie = Button(actions_cat, text='Supprimer une catégorie', padx=10, pady=10, bg='RoyalBlue1', activebackground='RoyalBlue1', activeforeground='black', font=('Tahoma', 8, 'bold'), command=func_delete_categorie)
delete_categorie.grid(row=1, column=1, padx=10, pady=10)

def click_id_categorie(event):
    id_categorie.config(state=NORMAL)
    id_categorie.delete(0, END)

def click_name_categorie(event):
    name_categorie.config(state=NORMAL)
    name_categorie.delete(0, END)

def click_del_categorie(event):
    del_categorie.config(state=NORMAL)
    del_categorie.delete(0, END)

id_categorie = Entry(actions_cat, justify=CENTER, border=4)
id_categorie.insert(0, 'ID*')
id_categorie.config(state=DISABLED)
id_categorie.bind("<Button-1>", click_id_categorie)
id_categorie.grid(row=0, column=0, pady=10)

name_categorie = Entry(actions_cat, justify=CENTER, border=4)
name_categorie.insert(0, 'Nom*')
name_categorie.config(state=DISABLED)
name_categorie.bind("<Button-1>", click_name_categorie)
name_categorie.grid(row=1, column=0, pady=10)

del_categorie = Entry(actions_cat, justify=CENTER, border=4)
del_categorie.insert(0, 'ID*')
del_categorie.config(state=DISABLED)
del_categorie.bind("<Button-1>", click_del_categorie)
del_categorie.grid(row=0, column=1, pady=10)

root.mainloop()