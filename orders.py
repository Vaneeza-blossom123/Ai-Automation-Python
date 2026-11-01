import sqlite3
from datetime import date

database = sqlite3.connect("Inventory.db")


def orders_received():

    print("Hello, we are here to take your order.")
    print("1 for Laptop")
    print("2 for Mouse")
    print("3 for Keyboard")
    print("4 for Scanner")
    print("5 for Printer")

    current_date = str(date.today())

    product_id = int(input("Enter product ID: "))

    order_result = database.execute(
        """
            SELECT Product_quantity, Product_price
            FROM Products
            WHERE Product_id = ?
        """,
        (product_id,),
    ).fetchone()

    if order_result is None:
        print("Product not found.")
        return
    else:
        customer_name = input("Enter customer name: ")
        order_quantity = int(input("Enter product quantity: "))

    product_quantity, product_price = order_result

    if order_quantity <= product_quantity and order_quantity < 5:
        Order_Price = order_quantity * product_price

        database.execute(
            """
                INSERT INTO ORDERS(product_id , 
                Order_quantity, 
                Order_price, 
                Customer_name,
                Order_date)
        
                VALUES(?,?,?,?,?)
                """,
            (product_id, order_quantity, Order_Price, customer_name, current_date),
        )
        database.commit()
        updated_quantity = product_quantity - order_quantity
        database.execute(
            """
            UPDATE PRODUCTS 
            SET PRODUCT_QUANTITY = ? 
            WHERE PRODUCT_ID = ? 


""",
            (updated_quantity, product_id),
        )
        database.commit()
        print("Order accepted!")
        print("Customer:", customer_name)
        print("Quantity:", order_quantity)
        print("Order price:", Order_Price)

        return Order_Price

    else:
        print("Order quantity is not avaiable in stock.")


orders_received()
