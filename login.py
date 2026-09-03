import tkinter as tk
from tkinter import messagebox
import dashboard

def open_login():
    window = tk.Toplevel()
    window.title("Login - Retail Purchase Prediction System")
    window.geometry("500x550")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # Main heading
    title = tk.Label(
        window,
        text="Welcome Back",
        font=("Arial", 25, "bold"),
        bg="#F4F6FA",
        fg="#172033"
    )
    title.pack(pady=(55, 8))

    # Subtitle
    subtitle = tk.Label(
        window,
        text="Login to your account",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg="#667085"
    )
    subtitle.pack(pady=(0, 35))

    # Login card
    card = tk.Frame(
        window,
        bg="white"
    )
    card.place(
        x=50,
        y=160,
        width=400,
        height=285
    )

    # Username label
    username_label = tk.Label(
        card,
        text="Username",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#172033"
    )
    username_label.place(
        x=35,
        y=30
    )

    # Username input
    username_entry = tk.Entry(
        card,
        font=("Arial", 11),
        bd=1,
        relief="solid"
    )
    username_entry.place(
        x=35,
        y=55,
        width=330,
        height=38
    )

    # Password label
    password_label = tk.Label(
        card,
        text="Password",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#172033"
    )
    password_label.place(
        x=35,
        y=115
    )

    # Password input
    password_entry = tk.Entry(
        card,
        font=("Arial", 11),
        bd=1,
        relief="solid",
        show="*"
    )
    password_entry.place(
        x=35,
        y=140,
        width=330,
        height=38
    )

    # Login function
    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        # Check empty username
        if username == "":
            messagebox.showerror(
                "Error",
                "Please enter Username."
            )
            return

        # Check empty password
        if password == "":
            messagebox.showerror(
                "Error",
                "Please enter Password."
            )
            return

        # Check login details
        if username == "chandradeep" and password == "cb@7741":

            messagebox.showinfo(
                "Login Successful",
                "Welcome to Retail Purchase Prediction System."
            )

            # Close login window
            window.destroy()

            # Open dashboard
            dashboard.open_dashboard()

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password."
            )

    # Login button
    login_button = tk.Button(
        card,
        text="Login",
        font=("Arial", 10, "bold"),
        bg="#4F46E5",
        fg="white",
        activebackground="#3730A3",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=login
    )
    login_button.place(
        x=35,
        y=205,
        width=330,
        height=40
    )

    # Close button
    close_button = tk.Button(
        window,
        text="Close",
        font=("Arial", 10),
        bg="#172033",
        fg="white",
        activebackground="#252D42",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=window.destroy
    )
    close_button.place(
        x=190,
        y=475,
        width=120,
        height=35
    )
