import tkinter as tk
from tkinter import messagebox, ttk
from sklearn.linear_model import LinearRegression
from datetime import date

from database import get_connection


def open_prediction():

    window = tk.Toplevel()
    window.title("Purchase Prediction - Retail Purchase Prediction System")
    window.geometry("900x800")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # Colors
    DARK = "#172033"
    PRIMARY = "#4F46E5"
    WHITE = "#FFFFFF"
    TEXT = "#172033"
    GRAY = "#667085"

    # ==========================================
    # ML Training Data
    # ==========================================

    price = [100, 120, 150, 130, 110, 160, 140, 125, 180, 170]
    discount = [5, 10, 8, 12, 7, 15, 10, 6, 18, 14]
    previous_sales = [50, 60, 45, 70, 55, 80, 65, 52, 90, 75]
    demand = [48, 58, 43, 68, 53, 77, 63, 50, 87, 72]

    # Prepare ML input data
    X = list(zip(price, discount, previous_sales))

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, demand)

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
        height=800
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
        width=690,
        height=800
    )

    # Page title
    title = tk.Label(
        main_area,
        text="Purchase Prediction",
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    title.place(
        x=0,
        y=0,
        width=690,
        height=75
    )

    # Description
    description = tk.Label(
        main_area,
        text="Predict product demand using Machine Learning",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg=GRAY
    )
    description.place(
        x=30,
        y=105
    )

    # ==========================================
    # Prediction Card
    # ==========================================

    card = tk.Frame(
        main_area,
        bg=WHITE
    )
    card.place(
        x=30,
        y=140,
        width=630,
        height=390
    )

    # Card title
    card_title = tk.Label(
        card,
        text="Enter Product Details",
        font=("Arial", 17, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    card_title.place(
        x=30,
        y=20
    )

    # ==========================================
    # Customer ID
    # ==========================================

    customer_label = tk.Label(
        card,
        text="Customer ID",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    customer_label.place(
        x=30,
        y=60
    )

    customer_entry = tk.Entry(
        card,
        font=("Arial", 11),
        relief="solid"
    )
    customer_entry.place(
        x=30,
        y=82,
        width=250,
        height=35
    )

    # ==========================================
    # Price
    # ==========================================

    price_label = tk.Label(
        card,
        text="Price",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    price_label.place(
        x=330,
        y=60
    )

    price_entry = tk.Entry(
        card,
        font=("Arial", 11),
        relief="solid"
    )
    price_entry.place(
        x=330,
        y=82,
        width=250,
        height=35
    )

    # ==========================================
    # Discount
    # ==========================================

    discount_label = tk.Label(
        card,
        text="Discount (%)",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    discount_label.place(
        x=30,
        y=135
    )

    discount_entry = tk.Entry(
        card,
        font=("Arial", 11),
        relief="solid"
    )
    discount_entry.place(
        x=30,
        y=158,
        width=250,
        height=35
    )

    # ==========================================
    # Previous Sales
    # ==========================================

    sales_label = tk.Label(
        card,
        text="Previous Sales",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    sales_label.place(
        x=330,
        y=135
    )

    sales_entry = tk.Entry(
        card,
        font=("Arial", 11),
        relief="solid"
    )
    sales_entry.place(
        x=330,
        y=158,
        width=250,
        height=35
    )

    # ==========================================
    # Prediction Result
    # ==========================================

    result_title = tk.Label(
        card,
        text="Predicted Purchase Demand",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=GRAY
    )
    result_title.place(
        x=30,
        y=215
    )

    result_value = tk.Label(
        card,
        text="--",
        font=("Arial", 25, "bold"),
        bg=WHITE,
        fg=PRIMARY
    )
    result_value.place(
        x=30,
        y=238
    )

    # ==========================================
    # Generate Prediction ID
    # ==========================================

    def generate_prediction_id(cursor):

        number = 1

        while True:

            prediction_id = f"PR{number:03d}"

            cursor.execute(
                """
                SELECT Prediction_ID
                FROM prediction
                WHERE Prediction_ID = %s
                """,
                (prediction_id,)
            )

            existing = cursor.fetchone()

            if existing is None:
                return prediction_id

            number += 1

    # ==========================================
    # Load Prediction History
    # ==========================================

    def load_predictions():

        for item in history_tree.get_children():
            history_tree.delete(item)

        conn = get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            query = """
                SELECT
                    Prediction_ID,
                    Customer_ID,
                    Prediction_Date,
                    Predicted_Purchase,
                    Algorithm
                FROM prediction
                ORDER BY Prediction_Date DESC, Prediction_ID DESC
            """

            cursor.execute(query)

            records = cursor.fetchall()

            for row in records:

                history_tree.insert(
                    "",
                    tk.END,
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4]
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
                f"Unable to load prediction history.\n\n{e}"
            )

    # ==========================================
    # Prediction Function
    # ==========================================

    def predict_demand():

        customer_id = customer_entry.get().strip()
        price_input = price_entry.get().strip()
        discount_input = discount_entry.get().strip()
        sales_input = sales_entry.get().strip()

        # Validate Customer ID
        if customer_id == "":
            messagebox.showerror(
                "Invalid Input",
                "Please enter Customer ID."
            )
            return

        # Validate numeric values
        try:

            price_value = float(price_input)
            discount_value = float(discount_input)
            sales_value = float(sales_input)

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numeric values."
            )
            return

        if price_value <= 0:

            messagebox.showerror(
                "Invalid Input",
                "Price must be greater than 0."
            )
            return

        if discount_value < 0:

            messagebox.showerror(
                "Invalid Input",
                "Discount cannot be negative."
            )
            return

        if sales_value < 0:

            messagebox.showerror(
                "Invalid Input",
                "Previous Sales cannot be negative."
            )
            return

        # ==========================================
        # Check Customer in Database
        # ==========================================

        conn = get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT Customer_ID
                FROM customer
                WHERE Customer_ID = %s
                """,
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

            # ==========================================
            # Make Prediction
            # ==========================================

            prediction = model.predict(
                [[
                    price_value,
                    discount_value,
                    sales_value
                ]]
            )[0]

            prediction = round(prediction)

            if prediction < 0:
                prediction = 0

            # Show result
            result_value.config(
                text=str(prediction)
            )

            # ==========================================
            # Generate Prediction ID
            # ==========================================

            prediction_id = generate_prediction_id(cursor)

            prediction_date = date.today()

            algorithm = "Multiple Linear Regression"

            # ==========================================
            # Save Prediction to MySQL
            # ==========================================

            query = """
                INSERT INTO prediction
                (
                    Prediction_ID,
                    Customer_ID,
                    Prediction_Date,
                    Predicted_Purchase,
                    Algorithm
                )
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                prediction_id,
                customer_id,
                prediction_date,
                int(prediction),
                algorithm
            )

            cursor.execute(
                query,
                values
            )

            # Permanently save
            conn.commit()

            cursor.close()
            conn.close()

            # Refresh history table
            load_predictions()

            messagebox.showinfo(
                "Prediction Saved",
                f"Prediction generated successfully.\n\n"
                f"Prediction ID: {prediction_id}\n"
                f"Predicted Purchase: {prediction}"
            )

        except Exception as e:

            try:
                conn.rollback()
                conn.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                f"Unable to save prediction.\n\n{e}"
            )

    # ==========================================
    # Predict Button
    # ==========================================

    predict_button = tk.Button(
        card,
        text="Predict Demand",
        font=("Arial", 11, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        activebackground="#3730A3",
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=predict_demand
    )
    predict_button.place(
        x=330,
        y=225,
        width=250,
        height=45
    )

    # ==========================================
    # Clear Function
    # ==========================================

    def clear_fields():

        customer_entry.delete(
            0,
            tk.END
        )

        price_entry.delete(
            0,
            tk.END
        )

        discount_entry.delete(
            0,
            tk.END
        )

        sales_entry.delete(
            0,
            tk.END
        )

        result_value.config(
            text="--"
        )

    # ==========================================
    # Clear Button
    # ==========================================

    clear_button = tk.Button(
        card,
        text="Clear",
        font=("Arial", 11, "bold"),
        bg=DARK,
        fg=WHITE,
        activebackground="#252D42",
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=clear_fields
    )
    clear_button.place(
        x=330,
        y=285,
        width=250,
        height=40
    )

    # ==========================================
    # Model Information
    # ==========================================

    model_info = tk.Label(
        card,
        text="Machine Learning Model: Multiple Linear Regression",
        font=("Arial", 10),
        bg=WHITE,
        fg=GRAY
    )
    model_info.place(
        x=30,
        y=335
    )

    # ==========================================
    # Prediction History Card
    # ==========================================

    history_card = tk.Frame(
        main_area,
        bg=WHITE
    )
    history_card.place(
        x=30,
        y=550,
        width=630,
        height=220
    )

    # History title
    history_title = tk.Label(
        history_card,
        text="Prediction History",
        font=("Arial", 15, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    history_title.place(
        x=20,
        y=12
    )

    # ==========================================
    # Refresh Button
    # ==========================================

    refresh_button = tk.Button(
        history_card,
        text="Refresh",
        font=("Arial", 9, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        activebackground="#3730A3",
        activeforeground=WHITE,
        bd=0,
        cursor="hand2",
        command=load_predictions
    )
    refresh_button.place(
        x=530,
        y=10,
        width=80,
        height=30
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
    # Prediction History Table
    # ==========================================

    table_frame = tk.Frame(
        history_card,
        bg=WHITE
    )
    table_frame.place(
        x=15,
        y=50,
        width=600,
        height=155
    )

    columns = (
        "Prediction_ID",
        "Customer_ID",
        "Date",
        "Predicted",
        "Algorithm"
    )

    history_tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    history_tree.heading(
        "Prediction_ID",
        text="Prediction ID"
    )

    history_tree.heading(
        "Customer_ID",
        text="Customer ID"
    )

    history_tree.heading(
        "Date",
        text="Date"
    )

    history_tree.heading(
        "Predicted",
        text="Predicted"
    )

    history_tree.heading(
        "Algorithm",
        text="Algorithm"
    )

    history_tree.column(
        "Prediction_ID",
        width=95,
        anchor="center"
    )

    history_tree.column(
        "Customer_ID",
        width=90,
        anchor="center"
    )

    history_tree.column(
        "Date",
        width=90,
        anchor="center"
    )

    history_tree.column(
        "Predicted",
        width=80,
        anchor="center"
    )

    history_tree.column(
        "Algorithm",
        width=220,
        anchor="center"
    )

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=history_tree.yview
    )

    history_tree.configure(
        yscrollcommand=scrollbar.set
    )

    history_tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ==========================================
    # Load Existing Predictions
    # ==========================================

    load_predictions()

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
        y=740,
        width=160,
        height=35
    )
