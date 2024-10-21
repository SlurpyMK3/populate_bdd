import os
import csv
import time
import sqlite3

from sql_tables import CREATE_TABLES


f = open('orders.csv', 'r')
luc = []
reader = csv.reader(f, delimiter=';')

for i in reader:
    luc.append(i)
    print(i)
    if len(luc) == 5: 
         break


luc = []  # Initialisation d'une liste vide pour stocker les lignes du fichier
reader = csv.reader(f, delimiter=';')    # Crée un lecteur CSV qui sépare les colonnes par un point-virgule (';')

conn = sqlite3.connect('C:/Users/axelm/Desktop/Cours/Mathieu/Brief_3/Projet/data/projet.db3')  # Remplace par le chemin de ta base de données
cursor = conn.cursor()
# Ouvre le fichier CSV 'orders.csv' en mode lecture ('r')
with open('orders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  # Crée un lecteur CSV
    luc = []  # Initialisation d'une liste vide pour stocker les lignes du fichier

    for i in reader:  # Boucle sur chaque ligne (enregistrement) lue du fichier
        luc.append(i)  # Ajoute la ligne lue (sous forme de liste) à la liste luc
        print(i)  # Affiche la ligne actuelle dans la console

        id = i[7]  # Récupère l'ID du produit à partir de la colonne 8 (index 7)
        description = i[8]
        price = i[9]

        # Utilise des paramètres pour éviter les erreurs de syntaxe

        sql_request = "INSERT OR IGNORE INTO product (id, description, price) VALUES (?, ?, ?);"
        cursor.execute(sql_request, (id, description, price))

with open('orders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    luc = [] 

    for i in reader:  
        luc.append(i) 
        print(i) 

        id = i[3]  
        country = i[4]



        sql_request = "INSERT OR REPLACE INTO customer (id, country) VALUES (?, ?);"
        cursor.execute(sql_request, (id, country))




with open('orders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    luc = [] 

    for i in reader:  
        luc.append(i)  
        print(i)  

        id = i[0] 7)
        invoice_nb = i[1]
        invoice_date = i[2]
        customer_id = i[3]

        sql_request = "INSERT OR IGNORE INTO customer_order (id, invoice_nb, invoice_date, customer_id) VALUES (?, ?, ?, ?);"
        cursor.execute(sql_request, (id, invoice_nb, invoice_date, customer_id))


with open('orders.csv', 'r') as file: 
    reader = csv.reader(file, delimiter=';') 
    luc = []  

    for i in reader: 
        luc.append(i)  
        print(i)  

        id = i[5]  
        quantity = i[6]
        order_id = i[0]
        product_id = i[7]
        sql_request = "INSERT OR IGNORE INTO order_detail (id, quantity, order_id, product_id) VALUES (?, ?, ?, ?);"
        cursor.execute(sql_request, (id, quantity, order_id, product_id))



conn.commit()
conn.close()