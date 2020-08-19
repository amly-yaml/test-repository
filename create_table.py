import sqlite3

connection = sqlite3.connect('myWeb.db')
cursor = connection.cursor()

table_order = "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, shipping_name text, payment_type text, shipping_fee real)"
cursor.execute(table_order)

table_order_detail = "CREATE TABLE IF NOT EXISTS order_detail (id INTEGER PRIMARY KEY, product_name text, price real, quantity int)"
cursor.execute(table_order_detail)

connection.commit()
connection.close()