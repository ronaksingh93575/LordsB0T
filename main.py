import tkinter as tk

from ui.login_window import LoginWindow
from database.db import create_database

create_database()

root = tk.Tk()

app = LoginWindow(root)

root.mainloop()