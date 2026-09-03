import tkinter as tk
import registration
import login

# Create main window
window = tk.Tk()
window.title("Retail Purchase Prediction System")
window.geometry("1100x700")
window.resizable(False, False)
window.configure(bg="#F4F6FA")

# ==========================================
# Project Title
# ==========================================

title = tk.Label(
    window,
    text="Retail Purchase Prediction System",
    font=("Arial", 26, "bold"),
    bg="#F4F6FA",
    fg="#172033"
)
title.pack(pady=100)

# ==========================================
# Project Description
# ==========================================

description = tk.Label(
    window,
    text="Manage Customers, Products, Purchases and Predict Demand",
    font=("Arial", 12),
    bg="#F4F6FA",
    fg="#667085"
)
description.pack()

# ==========================================
# Open Registration Page
# ==========================================

def open_registration():

    registration.open_registration()

# ==========================================
# Open Login Page
# ==========================================

def open_login():

    login.open_login()

# ==========================================
# Registration Button
# ==========================================

registration_button = tk.Button(
    window,
    text="Registration",
    font=("Arial", 11, "bold"),
    bg="#4F46E5",
    fg="white",
    activebackground="#3730A3",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=open_registration
)

registration_button.pack(
    pady=20,
    ipadx=30,
    ipady=10
)

# ==========================================
# Login Button
# ==========================================

login_button = tk.Button(
    window,
    text="Login",
    font=("Arial", 11, "bold"),
    bg="#172033",
    fg="white",
    activebackground="#252D42",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=open_login
)

login_button.pack(
    pady=5,
    ipadx=42,
    ipady=10
)

# ==========================================
# Start Application
# ==========================================

window.mainloop()
