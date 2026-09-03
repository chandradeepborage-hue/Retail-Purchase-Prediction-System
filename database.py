import mysql.connector
from tkinter import messagebox

# DATABASE SETTINGS

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root123"
DB_NAME = "retailpurchasedb"

# DATABASE CONNECTION

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn

    except mysql.connector.Error as e:
        messagebox.showerror(
            "Database Error",
            f"Unable to connect to database.\n\n{e}"
        )
        return None

# GET CUSTOMER COUNT

def get_customer_count():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM customer"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# GET PRODUCT COUNT

def get_product_count():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM product"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# GET PURCHASE COUNT

def get_purchase_count():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM purchase"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# GET PREDICTION COUNT

def get_prediction_count():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM prediction"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# GET PURCHASE HISTORY COUNT

def get_history_count():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM purchase_history"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# GET TOTAL PURCHASE AMOUNT

def get_total_purchase_amount():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(
            SUM(Purchase_Amount),
            0
        )
        FROM purchase
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return float(total)

# GET TOTAL PREDICTED PURCHASE

def get_total_predicted_purchase():
    conn = get_connection()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(
            SUM(Predicted_Purchase),
            0
        )
        FROM prediction
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return float(total)

# TEST CONNECTION

if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("Database connected successfully!")
        connection.close()
