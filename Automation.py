import os
import sqlite3

import requests
from dotenv import load_dotenv

database = sqlite3.connect("Inventory.db")  # Connecting with a database 'Inventory.db'.


def inventory_automation():

    stock_quantity = database.execute("""
      SELECT Product_id, 
      Product_quantity,
      Minimum_stock,
      Product_name
      FROM PRODUCTS 
""")  # Retrieve the product_id and minimum stock from the PRODUCTS table.

    products = (
        stock_quantity.fetchall()
    )  # decompsing the result of the query into id , minimum_stock and a name variable
    for product_id, Product_quantity, minimum_stock, name in products:
        if Product_quantity <= minimum_stock:
            load_dotenv()
            key = os.getenv('API')
            chat_id = os.getenv('chat_id')
            url = f"https://api.telegram.org/bot{key}/sendMessage"
            message = f"The product {name} is below the minimum stock level. Please restock it."
            requests.post(
                url,
                data={"chat_id": chat_id, "text": message},
            )


inventory_automation()
