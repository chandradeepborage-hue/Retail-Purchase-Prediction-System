# ============================================================
# REGISTRATION PAGE
# ============================================================

import tkinter as tk
from tkinter import messagebox
import re
import dashboard

def open_registration():

    # Create registration window
    window = tk.Toplevel()
    window.title("Registration - Retail Purchase Prediction System")
    window.geometry("500x550")
    window.resizable(False, False)
    window.configure(bg="#F4F6FA")

    # Main heading
    title = tk.Label(
        window,
        text="Create Account",
        font=("Arial", 25, "bold"),
        bg="#F4F6FA",
        fg="#172033"
    )
    title.pack(pady=(45, 8))

    # Subtitle
    subtitle = tk.Label(
        window,
        text="Register to access the system",
        font=("Arial", 11),
        bg="#F4F6FA",
        fg="#667085"
    )
    subtitle.pack(pady=(0, 30))

    # Registration card
    card = tk.Frame(
        window,
        bg="white"
    )
    card.place(
        x=50,
        y=140,
        width=400,
        height=330
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
        y=25
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
        y=50,
        width=330,
        height=38
    )

    # Email label
    email_label = tk.Label(
        card,
        text="Email Address",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#172033"
    )
    email_label.place(
        x=35,
        y=105
    )

    # Email input
    email_entry = tk.Entry(
        card,
        font=("Arial", 11),
        bd=1,
        relief="solid"
    )
    email_entry.place(
        x=35,
        y=130,
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
        y=185
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
        y=210,
        width=330,
        height=38
    )

    # Registration function
    def register():

        username = username_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        # Username validation
        if username == "":
            messagebox.showerror(
                "Error",
                "Please enter Username."
            )
            return

        # Email validation
        if email == "":
            messagebox.showerror(
                "Error",
                "Please enter Email Address."
            )
            return

        if not re.match(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            email
        ):
            messagebox.showerror(
                "Error",
                "Please enter a valid Email Address."
            )
            return

        # Password validation
        if password == "":
            messagebox.showerror(
                "Error",
                "Please enter Password."
            )
            return

        if len(password) < 6:
            messagebox.showerror(
                "Error",
                "Password must contain at least 6 characters."
            )
            return

        # Show successful registration message
        messagebox.showinfo(
            "Registration Successful",
            "Account created successfully."
        )

        # Close registration page
        window.destroy()

        # Open dashboard
        dashboard.open_dashboard()

    # Create Account button
    register_button = tk.Button(
        card,
        text="Create Account",
        font=("Arial", 10, "bold"),
        bg="#4F46E5",
        fg="white",
        activebackground="#3730A3",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=register
    )
    register_button.place(
        x=35,
        y=270,
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
        y=490,
        width=120,
        height=35
    )
