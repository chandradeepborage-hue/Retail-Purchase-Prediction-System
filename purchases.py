import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from database import get_connection


def open_purchases():
    window = tk.Toplevel()
    window.title("Purchases - Retail Purchase Prediction System")
    window.geometry("1000x650")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # Colors
    DARK = "#172033"
    PRIMARY = "#4F46E5"
    WHITE = "#FFFFFF"
    TEXT = "#172033"
    GRAY = "#667085"

    # Sidebar
    sidebar = tk.Frame(window, bg=DARK)
    sidebar.place(x=0, y=0, width=210, height=650)

    # Logo
    logo = tk.Label(
        sidebar,
        text="RetailPredict",
        font=("Arial", 20, "bold"),
        bg=DARK,
        fg=WHITE
    )
    logo.place(x=25, y=35)

    # Main area
    main_area = tk.Frame(window, bg="#F4F6FA")
    main_area.place(x=210, y=0, width=790, height=650)

    # Page title
    title = tk.Label(
        main_area,
        text="Purchases",
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    title.place(x=0, y=0, width=790, height=75)

    # Description
    description = tk.Label(
        main_area,
        text="Manage customer purchase records",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    )
    description.place(x=30, y=100)

    # Purchase form
    form_card = tk.Frame(main_area, bg=WHITE)
    form_card.place(x=30, y=135, width=730, height=185)

    form_title = tk.Label(
        form_card,
        text="Add New Purchase",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    form_title.place(x=20, y=15)

    # Purchase ID
    tk.Label(
        form_card,
        text="Purchase ID",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=20, y=55)

    purchase_id_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    purchase_id_entry.place(x=20, y=80, width=120, height=32)

    # Customer ID
    tk.Label(
        form_card,
        text="Customer ID",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=160, y=55)

    customer_id_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    customer_id_entry.place(x=160, y=80, width=120, height=32)

    # Product ID
    tk.Label(
        form_card,
        text="Product ID",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=300, y=55)

    product_id_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    product_id_entry.place(x=300, y=80, width=120, height=32)

    # Quantity
    tk.Label(
        form_card,
        text="Quantity",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=440, y=55)

    quantity_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    quantity_entry.place(x=440, y=80, width=100, height=32)

    # Price
    tk.Label(
        form_card,
        text="Price",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=560, y=55)

    price_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    price_entry.place(x=560, y=80, width=100, height=32)

    # Purchase table
    table_card = tk.Frame(main_area, bg=WHITE)
    table_card.place(x=30, y=340, width=730, height=270)

    # Table title
    tk.Label(
        table_card,
        text="Purchase Records",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(anchor="w", padx=20, pady=15)

    # Table columns
    columns = (
        "Purchase ID",
        "Customer ID",
        "Product ID",
        "Purchase Date",
        "Quantity",
        "Discount",
        "Purchase Amount"
    )

    purchase_table = ttk.Treeview(
        table_card,
        columns=columns,
        show="headings",
        height=8
    )

    for column in columns:
        purchase_table.heading(
            column,
            text=column
        )

    purchase_table.column("Purchase ID", width=85)
    purchase_table.column("Customer ID", width=85)
    purchase_table.column("Product ID", width=80)
    purchase_table.column("Purchase Date", width=100)
    purchase_table.column("Quantity", width=65)
    purchase_table.column("Discount", width=70)
    purchase_table.column("Purchase Amount", width=110)

    purchase_table.pack(
        padx=15,
        fill="x"
    )

    # ==========================================
    # Load Purchases From MySQL
    # ==========================================

    def load_purchases():

        for item in purchase_table.get_children():
            purchase_table.delete(item)

        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    Purchase_ID,
                    Customer_ID,
                    Product_ID,
                    Purchase_Date,
                    Quantity,
                    Discount,
                    Purchase_Amount
                FROM purchase
                ORDER BY Purchase_ID
            """)

            records = cursor.fetchall()

            for record in records:
                purchase_table.insert(
                    "",
                    tk.END,
                    values=record
                )

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                f"Unable to load purchase records.\n\n{e}"
            )

    # ==========================================
    # Add Purchase Function
    # ==========================================

    def add_purchase():

        purchase_id = purchase_id_entry.get().strip()
        customer_id = customer_id_entry.get().strip()
        product_id = product_id_entry.get().strip()
        quantity = quantity_entry.get().strip()
        price = price_entry.get().strip()

        # Validation
        if purchase_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Purchase ID."
            )
            return

        if customer_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Customer ID."
            )
            return

        if product_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Product ID."
            )
            return

        if quantity == "":
            messagebox.showerror(
                "Error",
                "Please enter Quantity."
            )
            return

        if price == "":
            messagebox.showerror(
                "Error",
                "Please enter Price."
            )
            return

        # Convert values
        try:
            quantity_value = int(quantity)
            price_value = float(price)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Quantity must be an integer and Price must be a number."
            )
            return

        if quantity_value <= 0:
            messagebox.showerror(
                "Error",
                "Quantity must be greater than 0."
            )
            return

        if price_value <= 0:
            messagebox.showerror(
                "Error",
                "Price must be greater than 0."
            )
            return

        # Calculate purchase amount
        total_amount = quantity_value * price_value

        # Purchase date = today's date
        purchase_date = date.today()

        # Discount = 0 by default
        discount = 0

        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            # Check Customer ID
            cursor.execute(
                "SELECT Customer_ID FROM customer WHERE Customer_ID = %s",
                (customer_id,)
            )

            customer_exists = cursor.fetchone()

            if customer_exists is None:
                messagebox.showerror(
                    "Error",
                    "Customer ID does not exist in database."
                )
                cursor.close()
                conn.close()
                return

            # Check Product ID
            cursor.execute(
                "SELECT Product_ID FROM product WHERE Product_ID = %s",
                (product_id,)
            )

            product_exists = cursor.fetchone()

            if product_exists is None:
                messagebox.showerror(
                    "Error",
                    "Product ID does not exist in database."
                )
                cursor.close()
                conn.close()
                return

            # Insert purchase into database
            query = """
                INSERT INTO purchase
                (
                    Purchase_ID,
                    Customer_ID,
                    Product_ID,
                    Purchase_Date,
                    Quantity,
                    Discount,
                    Purchase_Amount
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                purchase_id,
                customer_id,
                product_id,
                purchase_date,
                quantity_value,
                discount,
                total_amount
            )

            cursor.execute(query, values)

            # Permanently save
            conn.commit()

            cursor.close()
            conn.close()

            # Refresh table
            load_purchases()

            messagebox.showinfo(
                "Success",
                "Purchase added successfully to database."
            )

            # Clear entries
            purchase_id_entry.delete(0, tk.END)
            customer_id_entry.delete(0, tk.END)
            product_id_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)

        except Exception as e:

            try:
                conn.rollback()
                conn.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                f"Unable to save purchase.\n\n{e}"
            )

    # Add button
    add_button = tk.Button(
        form_card,
        text="Add Purchase",
        font=("Arial", 10, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=add_purchase
    )
    add_button.place(
        x=20,
        y=135,
        width=140,
        height=32
    )

    # Close button
    close_button = tk.Button(
        sidebar,
        text="Close",
        font=("Arial", 10, "bold"),
        bg="#252D42",
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=window.destroy
    )
    close_button.place(
        x=25,
        y=590,
        width=160,
        height=35
    )

    # ==========================================
    # Load Existing Records When Page Opens
    # ==========================================

    load_purchases()
