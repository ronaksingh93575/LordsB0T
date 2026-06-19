import tkinter as tk
from tkinter import messagebox
from database.supabase_db import authenticate_user
from ui.dashboard import Dashboard
from ui.signup_window import SignupWindow

class LoginWindow:

    def __init__(self, root):

        self.root = root
        self.root.title("Farming Bot Login")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#201E1E")

        # Title
        title = tk.Label(
            root,
            text="Farming Bot",
            font=("Arial", 20, "bold"),
            fg=("#D5D5D5"),
            bg=("#201E1E")
        )
        title.pack(pady=20)

        # Username Label
        username_label = tk.Label(
            root,
            text="Username",
            font=("Times new roman", 12),
            fg=("#D5D5D5"),
            bg=("#201E1E")
        )
        username_label.pack(
            anchor= "w",
            padx =100
        )

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
            bg=("#201E1E")
        )
        password_label.pack(
            anchor= "w",
            padx =100
        )

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

        #-------------------------------
        # creating a frame for login and signup
        #-------------------------------

        button_frame = tk.Frame(
            root,
            bg="#201E1E"
        )
        button_frame.pack(pady=15)

        # Login Button
        login_btn = tk.Button(
            button_frame,
            text="Login",
            width=15,
            command=self.login
        )
        login_btn.pack(
            side ="left",
            padx=10
        )

        #signup Button
        sign_up_btn = tk.Button(
            button_frame,
            text="Sign Up",
            width= 15,
            command = self.sign_up
        )
        sign_up_btn.pack(
            side = "right",
            padx = 10
        )

        # Status Label
        self.status_label = tk.Label(
            root,
            text="Please Login",
            font=("Arial", 11, "bold"),
            fg=("#D5D5D5"),
            bg=("#201E1E")
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
    
    def sign_up(self):

        signup_root = tk.Toplevel(
            self.root
        )
        SignupWindow(
            signup_root
        )