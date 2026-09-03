import tkinter as tk
from tkinter import ttk, messagebox

from database import get_connection


def open_report():

    window = tk.Toplevel()
    window.title("Reports - Retail Purchase Prediction System")
    window.geometry("1000x650")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # Colors
    DARK = "#172033"
    PRIMARY = "#4F46E5"
    WHITE = "#FFFFFF"
    TEXT = "#172033"
    GRAY = "#667085"

    # ==========================================
    # Sidebar
    # ==========================================

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

    # ==========================================
    # Main Area
    # ==========================================

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

    # ==========================================
    # Page Title
    # ==========================================

    title = tk.Label(
        main_area,
        text="Reports",
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
        text="View purchase summary and transaction records",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    )
    description.place(
        x=30,
        y=100
    )

    # ==========================================
    # Summary Values
    # ==========================================

    total_purchases_value = tk.Label(
        main_area,
        text="0",
        font=("Arial", 21, "bold"),
        bg=WHITE,
        fg=TEXT
    )

    total_quantity_value = tk.Label(
        main_area,
        text="0",
        font=("Arial", 21, "bold"),
        bg=WHITE,
        fg=TEXT
    )

    total_amount_value = tk.Label(
        main_area,
        text="₹0",
        font=("Arial", 21, "bold"),
        bg=WHITE,
        fg=TEXT
    )

    # ==========================================
    # Summary Card Function
    # ==========================================

    def summary_card(title_text, value_label, x):

        card = tk.Frame(
            main_area,
            bg=WHITE
        )
        card.place(
            x=x,
            y=135,
            width=230,
            height=105
        )

        label = tk.Label(
            card,
            text=title_text,
            font=("Arial", 10),
            bg=WHITE,
            fg=GRAY
        )
        label.place(
            x=20,
            y=18
        )

        value_label.place(
            in_=card,
            x=20,
            y=48
        )

    # Summary cards
    summary_card(
        "Total Purchases",
        total_purchases_value,
        30
    )

    summary_card(
        "Total Quantity",
        total_quantity_value,
        280
    )

    summary_card(
        "Total Amount",
        total_amount_value,
        530
    )

    # ==========================================
    # Report Table Card
    # ==========================================

    table_card = tk.Frame(
        main_area,
        bg=WHITE
    )
    table_card.place(
        x=30,
        y=270,
        width=730,
        height=300
    )

    # ==========================================
    # Table Title
    # ==========================================

    table_title = tk.Label(
        table_card,
        text="Purchase Report",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    table_title.place(
        x=20,
        y=15
    )

    # ==========================================
    # Refresh Button
    # ==========================================

    refresh_button = tk.Button(
        table_card,
        text="Refresh",
        font=("Arial", 9, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        activebackground="#3730A3",
        activeforeground=WHITE,
        bd=0,
        cursor="hand2"
    )
    refresh_button.place(
        x=620,
        y=10,
        width=90,
        height=30
    )

    # ==========================================
    # Table Frame
    # ==========================================

    table_frame = tk.Frame(
        table_card,
        bg=WHITE
    )
    table_frame.place(
        x=15,
        y=55,
        width=700,
        height=225
    )

    # ==========================================
    # Table Columns
    # ==========================================

    columns = (
        "Purchase ID",
        "Customer ID",
        "Product ID",
        "Date",
        "Quantity",
        "Amount"
    )

    report_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    # ==========================================
    # Table Headings
    # ==========================================

    for column in columns:

        report_table.heading(
            column,
            text=column
        )

    # ==========================================
    # Column Widths
    # ==========================================

    report_table.column(
        "Purchase ID",
        width=105,
        anchor="center"
    )

    report_table.column(
        "Customer ID",
        width=105,
        anchor="center"
    )

    report_table.column(
        "Product ID",
        width=105,
        anchor="center"
    )

    report_table.column(
        "Date",
        width=105,
        anchor="center"
    )

    report_table.column(
        "Quantity",
        width=80,
        anchor="center"
    )

    report_table.column(
        "Amount",
        width=110,
        anchor="center"
    )

    # ==========================================
    # Scrollbar
    # ==========================================

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=report_table.yview
    )

    report_table.configure(
        yscrollcommand=scrollbar.set
    )

    report_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ==========================================
    # Load Report from MySQL
    # ==========================================

    def load_report():

        # Clear old table records
        for item in report_table.get_children():

            report_table.delete(item)

        # Connect to database
        conn = get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            # Get purchase records
            query = """
                SELECT
                    Purchase_ID,
                    Customer_ID,
                    Product_ID,
                    Purchase_Date,
                    Quantity,
                    Purchase_Amount
                FROM purchase
                ORDER BY Purchase_ID
            """

            cursor.execute(query)

            records = cursor.fetchall()

            # Summary calculations
            total_purchases = len(records)
            total_quantity = 0
            total_amount = 0

            # Insert records into table
            for row in records:

                purchase_id = row[0]
                customer_id = row[1]
                product_id = row[2]
                purchase_date = row[3]
                quantity = row[4]
                amount = row[5]

                # Handle NULL values
                if quantity is None:
                    quantity = 0

                if amount is None:
                    amount = 0

                total_quantity += quantity
                total_amount += amount

                report_table.insert(
                    "",
                    tk.END,
                    values=(
                        purchase_id,
                        customer_id,
                        product_id,
                        purchase_date,
                        quantity,
                        "₹" + str(amount)
                    )
                )

            # Update summary cards
            total_purchases_value.config(
                text=str(total_purchases)
            )

            total_quantity_value.config(
                text=str(total_quantity)
            )

            total_amount_value.config(
                text="₹" + str(total_amount)
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
                f"Unable to load purchase report.\n\n{e}"
            )

    # ==========================================
    # Refresh Command
    # ==========================================

    refresh_button.config(
        command=load_report
    )

    # ==========================================
    # Treeview Style
    # ==========================================

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        "Treeview",
        font=("Arial", 9),
        rowheight=28,
        background=WHITE,
        foreground=TEXT,
        fieldbackground=WHITE
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 9, "bold"),
        background=DARK,
        foreground=WHITE
    )

    # ==========================================
    # Load Data When Page Opens
    # ==========================================

    load_report()

    # ==========================================
    # Close Button
    # ==========================================

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
