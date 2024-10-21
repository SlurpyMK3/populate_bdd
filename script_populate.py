conn = sqlite3.connect('C:/Users/axelm/Desktop/Cours/Mathieu/Brief_3/Projet/data/projet.db3')
cursor = conn.cursor()

# Lecture du fichier CSV
with open('orders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)  # Lire toutes les lignes dans une liste

    for i in data:
        print(i)

        # Insertion dans la table product
        id = i[7]
        description = i[8]
        price = i[9]
        sql_request = "INSERT OR IGNORE INTO product (id, description, price) VALUES (?, ?, ?);"
        cursor.execute(sql_request, (id, description, price))

        # Insertion dans la table customer
        id = i[3]
        country = i[4]
        sql_request = "INSERT OR REPLACE INTO customer (id, country) VALUES (?, ?);"
        cursor.execute(sql_request, (id, country))

        # Insertion dans la table customer_order
        id = i[0]
        invoice_nb = i[1]
        invoice_date = i[2]
        customer_id = i[3]
        sql_request = "INSERT OR IGNORE INTO customer_order (id, invoice_nb, invoice_date, customer_id) VALUES (?, ?, ?, ?);"
        cursor.execute(sql_request, (id, invoice_nb, invoice_date, customer_id))

        # Insertion dans la table order_detail
        id = i[5]
        quantity = i[6]
        order_id = i[0]
        product_id = i[7]
        sql_request = "INSERT OR IGNORE INTO order_detail (id, quantity, order_id, product_id) VALUES (?, ?, ?, ?);"
        cursor.execute(sql_request, (id, quantity, order_id, product_id))

# Commit et fermeture de la connexion
conn.commit()
conn.close()