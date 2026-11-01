import sqlite3

database = sqlite3.connect("Inventory.db")

database.execute("PRAGMA foreign_keys = ON")

database.execute("""
          CREATE TABLE IF NOT EXISTS PRODUCTS(
          Product_id INTEGER PRIMARY KEY,
          Product_name TEXT,
          Product_Price REAL,
          Product_quantity INTEGER,
          Minimum_stock INTEGER
        )
""")
database.commit()

database.execute("""
         INSERT INTO PRODUCTS(Product_name , Product_Price , Product_quantity, Minimum_stock)
         VALUES('Printer',10000,10,5)
""")
database.commit()


database.execute("""
             CREATE TABLE IF NOT EXISTS Orders (
             Order_id INTEGER PRIMARY KEY,
             product_id INTEGER,
             Order_quantity INTEGER,
             Order_date VARCHAR(20),
             Customer_name CHAR(20),
             Order_Price REAL,


             FOREIGN KEY (product_id)
             REFERENCES Products(Product_id)
            )
""")

database.commit()
database.close()
