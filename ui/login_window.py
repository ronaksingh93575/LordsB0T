import tkinter as tk
from tkinter import messagebox
from database.db import authenticate_user
from ui.dashboard import Dashboard


class LoginWindow:

    def __init__(self, root):

        self.root = root
        self.root.title("Farming Bot Login")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")

        # Title
        title = tk.Label(
            root,
            text="Farming Bot",
            font=("Arial", 20, "bold"),
            fg=("#D5D5D5"),
            bg=("#2E2E2E")
        )
        title.pack(pady=20)

        # Username Label
        username_label = tk.Label(
            root,
            text="Username",
            font=("Times new roman", 12),
            fg=("#D5D5D5"),
            bg=("#2E2E2E")
        )
        username_label.pack()

        # Username Entry
        self.username_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB")
        )
        self.username_entry.pack(pady=5)

        # Password Label
        password_label = tk.Label(
            root,
            text="Password",
            font=("Times new roman", 12),
            fg=("#D0D0D0"),
            bg=("#2E2E2E")
        )
        password_label.pack()

        # Password Entry
        self.password_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB"),
            show="*"
        )
        self.password_entry.pack(pady=5)

        # Login Button
        login_btn = tk.Button(
            root,
            text="Login",
            width=15,
            command=self.login
        )
        login_btn.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(
            root,
            text="Please Login",
            font=("Arial", 11, "bold"),
            fg=("#D5D5D5"),
            bg=("#2E2E2E")
        )
        self.status_label.pack()

    def login(self):
        
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
    
        if authenticate_user(username, password):
        
            self.status_label.config(
                text="Login Successful",
                fg="green"
            )
    
            # Open dashboard here later
            self.root.destroy()
            dashboard_root = tk.Tk()
            Dashboard(dashboard_root, username)

        else:
        
            self.status_label.config(
                text="Invalid Credentials",
                fg="red"
            )
    
            