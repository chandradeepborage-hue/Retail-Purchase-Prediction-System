import tkinter as tk
from tkinter import ttk, messagebox
from database import get_connection

def open_products():
    window = tk.Toplevel()
    window.title("Products - Retail Purchase Prediction System")
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
    sidebar = tk.Frame(
        window,
        bg=DARK
    )
    sidebar.place(
        x=0,
        y=0,
        width=210,
        height=650
    )

    # Logo
    logo = tk.Label(
        sidebar,
        text="RetailPredict",
        font=("Arial", 20, "bold"),
        bg=DARK,
        fg=WHITE
    )
    logo.place(
        x=25,
        y=35
    )

    # Main area
    main_area = tk.Frame(
        window,
        bg="#F4F6FA"
    )
    main_area.place(
        x=210,
        y=0,
        width=790,
        height=650
    )

    # Page title
    title = tk.Label(
        main_area,
        text="Products",
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    title.place(
        x=0,
        y=0,
        width=790,
        height=75
    )

    # Description
    description = tk.Label(
        main_area,
        text="Manage product information",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    )
    description.place(
        x=30,
        y=100
    )

    # Product form card
    form_card = tk.Frame(
        main_area,
        bg=WHITE
    )
    form_card.place(
        x=30,
        y=135,
        width=730,
        height=180
    )

    form_title = tk.Label(
        form_card,
        text="Add New Product",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    form_title.place(
        x=20,
        y=15
    )

    # Product ID
    tk.Label(
        form_card,
        text="Product ID",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=20,
        y=55
    )

    id_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    id_entry.place(
        x=20,
        y=80,
        width=130,
        height=32
    )

    # Product Name
    tk.Label(
        form_card,
        text="Product Name",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=170,
        y=55
    )

    name_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    name_entry.place(
        x=170,
        y=80,
        width=170,
        height=32
    )

    # Category
    tk.Label(
        form_card,
        text="Category",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=360,
        y=55
    )

    category_combo = ttk.Combobox(
        form_card,
        values=[
            "Electronics",
            "Mobile",
            "Computer",
            "Accessories",
            "Fashion",
            "Other"
        ],
        state="readonly"
    )
    category_combo.place(
        x=360,
        y=80,
        width=130,
        height=32
    )

    # Price
    tk.Label(
        form_card,
        text="Price",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=510,
        y=55
    )

    price_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    price_entry.place(
        x=510,
        y=80,
        width=100,
        height=32
    )

    # Add product function
    def add_product():
        product_id = id_entry.get().strip()
        product_name = name_entry.get().strip()
        category = category_combo.get()
        price = price_entry.get().strip()

        if product_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Product ID."
            )
            return

        if product_name == "":
            messagebox.showerror(
                "Error",
                "Please enter Product Name."
            )
            return

        if category == "":
            messagebox.showerror(
                "Error",
                "Please select Category."
            )
            return

        if price == "":
            messagebox.showerror(
                "Error",
                "Please enter Price."
            )
            return

        try:
            price_value = int(price)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Price must be a number."
            )
            return

        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO product
                (
                    Product_ID,
                    Product_Name,
                    Category,
                    Price
                )
                VALUES (%s, %s, %s, %s)
            """, (
                product_id,
                product_name,
                category,
                price_value
            ))

            conn.commit()

            cursor.close()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Product added successfully."
            )

            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            category_combo.set("")
            price_entry.delete(0, tk.END)

            load_products()

        except Exception as e:
            if conn:
                conn.rollback()
                conn.close()

            messagebox.showerror(
                "Database Error",
                f"Unable to add product.\n\n{e}"
            )

    # Add button
    add_button = tk.Button(
        form_card,
        text="Add Product",
        font=("Arial", 10, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=add_product
    )
    add_button.place(
        x=200,
        y=140,
        width=140,
        height=32
    )

    # Table card
    table_card = tk.Frame(
        main_area,
        bg=WHITE
    )
    table_card.place(
        x=30,
        y=335,
        width=730,
        height=275
    )

    # Table title
    tk.Label(
        table_card,
        text="Product Records",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )

    # Table columns
    columns = (
        "Product ID",
        "Product Name",
        "Category",
        "Price"
    )

    product_table = ttk.Treeview(
        table_card,
        columns=columns,
        show="headings",
        height=8
    )

    for column in columns:
        product_table.heading(
            column,
            text=column
        )

    product_table.column(
        "Product ID",
        width=100
    )

    product_table.column(
        "Product Name",
        width=200
    )

    product_table.column(
        "Category",
        width=160
    )

    product_table.column(
        "Price",
        width=120
    )

    product_table.pack(
        padx=15,
        fill="x"
    )

    # Load products from database
    def load_products():
        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    Product_ID,
                    Product_Name,
                    Category,
                    Price
                FROM product
            """)

            records = cursor.fetchall()

            for row in product_table.get_children():
                product_table.delete(row)

            for record in records:
                product_table.insert(
                    "",
                    tk.END,
                    values=record
                )

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                f"Unable to load products.\n\n{e}"
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

    # Load existing product records
    load_products()
