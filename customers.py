import tkinter as tk
from tkinter import ttk, messagebox
from database import get_connection

def open_customers():
    window = tk.Toplevel()
    window.title("Customers - Retail Purchase Prediction System")
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
        text="Customers",
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
        text="Manage customer information",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    )
    description.place(
        x=30,
        y=100
    )

    # Customer form card
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
        text="Add New Customer",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    form_title.place(
        x=20,
        y=15
    )

    # Customer ID
    tk.Label(
        form_card,
        text="Customer ID",
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
        width=140,
        height=32
    )

    # Customer Name
    tk.Label(
        form_card,
        text="Customer Name",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=180,
        y=55
    )

    name_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    name_entry.place(
        x=180,
        y=80,
        width=180,
        height=32
    )

    # Age
    tk.Label(
        form_card,
        text="Age",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=400,
        y=55
    )

    age_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    age_entry.place(
        x=400,
        y=80,
        width=80,
        height=32
    )

    # Gender
    tk.Label(
        form_card,
        text="Gender",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=500,
        y=55
    )

    gender_combo = ttk.Combobox(
        form_card,
        values=["Male", "Female", "Other"],
        state="readonly"
    )
    gender_combo.place(
        x=500,
        y=80,
        width=110,
        height=32
    )

    # Location
    tk.Label(
        form_card,
        text="Location",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).place(
        x=20,
        y=125
    )

    location_entry = tk.Entry(
        form_card,
        font=("Arial", 10),
        relief="solid"
    )
    location_entry.place(
        x=20,
        y=145,
        width=200,
        height=28
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
        text="Customer Records",
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
        "Customer ID",
        "Customer Name",
        "Age",
        "Gender",
        "Location"
    )

    customer_table = ttk.Treeview(
        table_card,
        columns=columns,
        show="headings",
        height=8
    )

    for column in columns:
        customer_table.heading(
            column,
            text=column
        )

    customer_table.column(
        "Customer ID",
        width=100
    )

    customer_table.column(
        "Customer Name",
        width=170
    )

    customer_table.column(
        "Age",
        width=60
    )

    customer_table.column(
        "Gender",
        width=100
    )

    customer_table.column(
        "Location",
        width=150
    )

    customer_table.pack(
        padx=15,
        fill="x"
    )

    # Load customers from database
    def load_customers():
        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT Customer_ID,
                       Customer_Name,
                       Age,
                       Gender,
                       Location
                FROM customer
            """)

            records = cursor.fetchall()

            for row in customer_table.get_children():
                customer_table.delete(row)

            for record in records:
                customer_table.insert(
                    "",
                    tk.END,
                    values=record
                )

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                f"Unable to load customers.\n\n{e}"
            )

    # Add customer function
    def add_customer():
        customer_id = id_entry.get().strip()
        customer_name = name_entry.get().strip()
        age = age_entry.get().strip()
        gender = gender_combo.get()
        location = location_entry.get().strip()

        if customer_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Customer ID."
            )
            return

        if customer_name == "":
            messagebox.showerror(
                "Error",
                "Please enter Customer Name."
            )
            return

        if age == "":
            messagebox.showerror(
                "Error",
                "Please enter Age."
            )
            return

        if gender == "":
            messagebox.showerror(
                "Error",
                "Please select Gender."
            )
            return

        if location == "":
            messagebox.showerror(
                "Error",
                "Please enter Location."
            )
            return

        try:
            age_value = int(age)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Age must be a number."
            )
            return

        conn = get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO customer
                (
                    Customer_ID,
                    Customer_Name,
                    Age,
                    Gender,
                    Location
                )
                VALUES (%s, %s, %s, %s, %s)
            """, (
                customer_id,
                customer_name,
                age_value,
                gender,
                location
            ))

            conn.commit()

            cursor.close()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Customer added successfully."
            )

            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            gender_combo.set("")
            location_entry.delete(0, tk.END)

            load_customers()

        except Exception as e:
            if conn:
                conn.rollback()
                conn.close()

            messagebox.showerror(
                "Database Error",
                f"Unable to add customer.\n\n{e}"
            )

    # Add button
    add_button = tk.Button(
        form_card,
        text="Add Customer",
        font=("Arial", 10, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        cursor="hand2",
        command=add_customer
    )
    add_button.place(
        x=250,
        y=140,
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

    # Load existing customer records
    load_customers()
