import tkinter as tk
import sqlite3
from database.db import DATABASE_PATH


class SettingsWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Bot Settings")
        self.root.geometry("400x300")
        

        self.auto_colosseum = tk.BooleanVar()
        self.auto_gathering = tk.BooleanVar()
        self.auto_training = tk.BooleanVar()
        self.auto_healing = tk.BooleanVar()
        self.auto_collecting = tk.BooleanVar()

        tk.Checkbutton(
            root,
            text="Auto Colosseum",
            variable=self.auto_colosseum
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Gathering",
            variable=self.auto_gathering
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Training",
            variable=self.auto_training
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Healing",
            variable=self.auto_healing
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Collecting",
            variable=self.auto_collecting
        ).pack(anchor="w", padx=20, pady=5)

        tk.Button(
            root,
            text="Save Settings",
            command=self.save_settings
        ).pack(pady=20)

    def save_settings(self):
        
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE settings
            SET
            auto_colosseum=?,
            auto_gathering=?,
            auto_training=?,
            auto_healing=?,
            auto_collecting=?
            WHERE username=?
            """,
            (
                self.auto_colosseum.get(),
                self.auto_gathering.get(),
                self.auto_training.get(),
                self.auto_healing.get(),
                self.auto_collecting.get(),
                self.username
            )
        )

        conn.commit()
        conn.close()

        print("Settings Saved")