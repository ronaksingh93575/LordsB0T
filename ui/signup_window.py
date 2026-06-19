import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import tkinter as tk
from tkinter import messagebox
import re
from database.supabase_db import username_exists, email_exists, add_user

class SignupWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Sign Up")
        self.root.geometry("400x450")
        self.root.configure(bg="#201E1E")
        self.root.resizable(False, False)


        # Title
        title = tk.Label(
            root,
            text="SignUp Window",
            font=("Arial", 20, "bold"),
            fg=("#D5D5D5"),
            bg=("#201E1E")
        )
        title.pack(pady=20)

        #email

        tk.Label(
            root,
            text="Email",
            fg=("#D5D5D5"),
            bg=("#201E1E")
        ).pack(
            anchor= "w",
            padx =50
            )

        self.email_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB"),
            )
        self.email_entry.pack(pady=10)

        # username 

        tk.Label(
            root,
            text="Username",
            fg=("#D5D5D5"),
            bg=("#201E1E")
        ).pack(
            anchor= "w",
            padx =50
        )

        self.username_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB")
            )
        self.username_entry.pack(pady= 10)

        # password

        tk.Label(
            root,
            text="Password",
            fg=("#D5D5D5"),
            bg=("#201E1E")
        ).pack(
            anchor= "w",
            padx =50
            )

        self.password_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB"),
            show="*"
        )
        self.password_entry.pack(pady=10)

        tk.Label(
            root,
            text="Confirm Password",
            fg=("#D5D5D5"),
            bg=("#201E1E")
        ).pack(
            anchor= "w",
            padx =50
            )

        self.confirm_entry = tk.Entry(
            root,
            width=30,
            font=("Times new roman", 12),
            fg=("#323232"),
            bg=("#CBCBCB"),
            show="*"
        )
        self.confirm_entry.pack(pady = 10)

        # register

        tk.Button(
            root,
            text="Register",
            command=self.register
        ).pack(pady=15)

    #-----------------------------
    # registration button algo
    #-----------------------------

    def register(self):
        print("regitraion called")
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not email:
            messagebox.showerror(
                "Error",
                "Email is required"
            )
            return
        if not username:
            messagebox.showerror(
                "Error",
                "Username Required"
            )
            return
        if not password:
            messagebox.showerror(
                "Error",
                "Password is required"
            )

        if password != confirm:

            messagebox.showerror(
                "Error",
                "Passwords do not match"
            )
            return


        #--------------------------------------
        # email valiadation logic
        #--------------------------------------
        def valid_email(email):
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            return re.match(
                pattern,
                email
            )

        if not valid_email(email):
            messagebox.showerror(
                "Error",
                "Invalid email address"
            )
            return
        #--------------------------------------
        # uniqe username logic
        #--------------------------------------

        if username_exists(username):
        
            messagebox.showerror(
                "Error",
                "Username already exists"
            )

            return
        if email_exists(email):
        
            messagebox.showerror(
                "Error",
                "Email already exists"
            )
        
            return
        
        add_user(
            email,
            username,
            password
        )
        messagebox.showinfo(
            "Success",
            "Registration test successful"
        )
        self.root.destroy()



# Main execution block
# if __name__ == "__main__":
#     root = tk.Tk()  # Properly initialize the main window
#     app = SignupWindow(root)
#     root.mainloop()
