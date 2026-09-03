import tkinter as tk
from tkinter import ttk, messagebox
from database import get_connection


def open_history():
    window = tk.Toplevel()
    window.title("Purchase History - Retail Purchase Prediction System")
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
    tk.Label(
        sidebar,
        text="RetailPredict",
        font=("Arial", 20, "bold"),
        bg=DARK,
        fg=WHITE
    ).place(x=25, y=35)

    # Main area
    main_area = tk.Frame(window, bg="#F4F6FA")
    main_area.place(x=210, y=0, width=790, height=650)

    # Page title
    tk.Label(
        main_area,
        text="Purchase History",
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(x=0, y=0, width=790, height=75)

    # Description
    tk.Label(
        main_area,
        text="View previous purchase transactions",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    ).place(x=30, y=100)

    # History card
    history_card = tk.Frame(
        main_area,
        bg=WHITE
    )
    history_card.place(
        x=30,
        y=135,
        width=730,
        height=430
    )

    # Card title
    tk.Label(
        history_card,
        text="Purchase Transaction History",
        font=("Arial", 16, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )

    # Table columns
    columns = (
        "Purchase ID",
        "Customer ID",
        "Product ID",
        "Quantity",
        "Price",
        "Total"
    )

    history_table = ttk.Treeview(
        history_card,
        columns=columns,
        show="headings",
        height=14
    )

    # Table headings
    for column in columns:
        history_table.heading(
            column,
            text=column
        )

    # Column widths
    history_table.column(
        "Purchase ID",
        width=100
    )

    history_table.column(
        "Customer ID",
        width=100
    )

    history_table.column(
        "Product ID",
        width=100
    )

    history_table.column(
        "Quantity",
        width=80
    )

    history_table.column(
        "Price",
        width=100
    )

    history_table.column(
        "Total",
        width=100
    )

    history_table.pack(
        padx=15,
        fill="x"
    )

    # ==========================================
    # Load Purchase History From MySQL
    # ==========================================

    def load_history():

        # Clear old records
        for item in history_table.get_children():
            history_table.delete(item)

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
                    Quantity,
                    Purchase_Amount
                FROM purchase
                ORDER BY Purchase_ID
            """)

            records = cursor.fetchall()

            for record in records:

                purchase_id = record[0]
                customer_id = record[1]
                product_id = record[2]
                quantity = record[3]
                total = record[4]

                # Calculate price from total amount
                if quantity and quantity != 0:
                    price = float(total) / int(quantity)
                else:
                    price = 0

                history_table.insert(
                    "",
                    tk.END,
                    values=(
                        purchase_id,
                        customer_id,
                        product_id,
                        quantity,
                        price,
                        total
                    )
                )

            cursor.close()
            conn.close()

        except Exception as e:

            try:
                conn.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                f"Unable to load purchase history.\n\n{e}"
            )

    # Close button
    tk.Button(
        sidebar,
        text="Close",
        font=("Arial", 10, "bold"),
        bg="#252D42",
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=window.destroy
    ).place(
        x=25,
        y=590,
        width=160,
        height=35
    )

    # ==========================================
    # Load Existing History When Page Opens
    # ==========================================

    load_history()
