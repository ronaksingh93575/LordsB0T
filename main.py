import tkinter as tk
import pygetwindow as gw

from ui.login_window import LoginWindow
# from database.supabase_db import create_database

# create_database()

root = tk.Tk()

app = LoginWindow(root)

root.mainloop()
