import tkinter as tk

import customers
import products
import purchases
import history
import prediction
import report

from database import get_connection


def get_total_count(table_name):
    """
    Get total number of records from MySQL table.
    """

    db = None
    cursor = None

    try:
        db = get_connection()

        if db is None:
            return 0

        cursor = db.cursor()

        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)

        result = cursor.fetchone()

        return result[0] if result else 0

    except Exception as e:
        print("Error fetching count:", e)
        return 0

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


def open_dashboard():

    window = tk.Toplevel()

    window.title("Dashboard - Retail Purchase Prediction System")
    window.geometry("1100x700")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # ==========================================
    # Colors
    # ==========================================

    DARK = "#172033"
    PRIMARY = "#4F46E5"
    WHITE = "#FFFFFF"
    TEXT = "#172033"
    GRAY = "#667085"

    # ==========================================
    # Get Data From Database
    # ==========================================

    total_customers = get_total_count("customer")
    total_products = get_total_count("product")
    total_purchases = get_total_count("purchase")

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
        width=230,
        height=700
    )

    # ==========================================
    # Logo
    # ==========================================

    tk.Label(
        sidebar,
        text="RetailPredict",
        font=("Arial", 22, "bold"),
        bg=DARK,
        fg=WHITE
    ).place(
        x=30,
        y=35
    )

    # ==========================================
    # Dashboard Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Dashboard",
        font=("Arial", 11, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2"
    ).place(
        x=10,
        y=110,
        width=210,
        height=42
    )

    # ==========================================
    # Customers Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Customers",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=customers.open_customers
    ).place(
        x=10,
        y=160,
        width=210,
        height=42
    )

    # ==========================================
    # Products Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Products",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=products.open_products
    ).place(
        x=10,
        y=210,
        width=210,
        height=42
    )

    # ==========================================
    # Purchases Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Purchases",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=purchases.open_purchases
    ).place(
        x=10,
        y=260,
        width=210,
        height=42
    )

    # ==========================================
    # Purchase Prediction Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Purchase Prediction",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=prediction.open_prediction
    ).place(
        x=10,
        y=310,
        width=210,
        height=42
    )

    # ==========================================
    # Purchase History Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Purchase History",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=history.open_history
    ).place(
        x=10,
        y=360,
        width=210,
        height=42
    )

    # ==========================================
    # Reports Button
    # ==========================================

    tk.Button(
        sidebar,
        text="Reports",
        font=("Arial", 11),
        bg=DARK,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=report.open_report
    ).place(
        x=10,
        y=410,
        width=210,
        height=42
    )

    # ==========================================
    # Logout
    # ==========================================

    def logout():
        window.destroy()

    tk.Button(
        sidebar,
        text="Logout",
        font=("Arial", 11, "bold"),
        bg="#252D42",
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=logout
    ).place(
        x=20,
        y=620,
        width=190,
        height=40
    )

    # ==========================================
    # Main Area
    # ==========================================

    main_area = tk.Frame(
        window,
        bg="#F4F6FA"
    )

    main_area.place(
        x=230,
        y=0,
        width=870,
        height=700
    )

    # ==========================================
    # Top Bar
    # ==========================================

    topbar = tk.Frame(
        main_area,
        bg=WHITE
    )

    topbar.place(
        x=0,
        y=0,
        width=870,
        height=80
    )

    tk.Label(
        topbar,
        text="Dashboard",
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=30,
        y=22
    )

    # ==========================================
    # Welcome Message
    # ==========================================

    tk.Label(
        main_area,
        text="Welcome to Retail Purchase Prediction System",
        font=("Arial", 19, "bold"),
        bg="#F4F6FA",
        fg=TEXT
    ).place(
        x=30,
        y=120
    )

    tk.Label(
        main_area,
        text="Manage customers, products, purchases and demand prediction.",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    ).place(
        x=30,
        y=155
    )

    # ==========================================
    # Dashboard Card Function
    # ==========================================

    def create_card(title, value, x):

        card = tk.Frame(
            main_area,
            bg=WHITE
        )

        card.place(
            x=x,
            y=220,
            width=240,
            height=130
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 10),
            bg=WHITE,
            fg=GRAY
        ).place(
            x=20,
            y=20
        )

        tk.Label(
            card,
            text=str(value),
            font=("Arial", 26, "bold"),
            bg=WHITE,
            fg=TEXT
        ).place(
            x=20,
            y=55
        )

    # ==========================================
    # Summary Cards
    # ==========================================

    create_card(
        "Total Customers",
        total_customers,
        30
    )

    create_card(
        "Total Products",
        total_products,
        300
    )

    create_card(
        "Total Purchases",
        total_purchases,
        570
    )

    # ==========================================
    # Quick Actions Heading
    # ==========================================

    tk.Label(
        main_area,
        text="Quick Actions",
        font=("Arial", 17, "bold"),
        bg="#F4F6FA",
        fg=TEXT
    ).place(
        x=30,
        y=390
    )

    # ==========================================
    # Manage Customers
    # ==========================================

    tk.Button(
        main_area,
        text="Manage Customers",
        font=("Arial", 10, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=customers.open_customers
    ).place(
        x=30,
        y=435,
        width=200,
        height=45
    )

    # ==========================================
    # Manage Products
    # ==========================================

    tk.Button(
        main_area,
        text="Manage Products",
        font=("Arial", 10, "bold"),
        bg=DARK,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=products.open_products
    ).place(
        x=250,
        y=435,
        width=200,
        height=45
    )

    # ==========================================
    # Purchase Prediction
    # ==========================================

    tk.Button(
        main_area,
        text="Purchase Prediction",
        font=("Arial", 10, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=prediction.open_prediction
    ).place(
        x=470,
        y=435,
        width=200,
        height=45
    )
