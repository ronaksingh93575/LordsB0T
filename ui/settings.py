import tkinter as tk
import sqlite3
from database.db import DATABASE_PATH
from database.db import get_user_settings, save_settings
from utils.logger import Logger


class SettingsWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("Bot Settings")
        self.root.geometry("400x300")
        

        self.auto_colosseum = tk.BooleanVar()
        self.auto_gathering = tk.BooleanVar()
        self.auto_training = tk.BooleanVar()
        self.auto_healing = tk.BooleanVar()
        self.auto_collecting = tk.BooleanVar()

        self.load_settings()

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
            command=self.save
        ).pack(pady=20)

    def load_settings(self):
        settings = get_user_settings(self.username)
        if settings:
            self.auto_colosseum.set(settings["auto_colosseum"])
            self.auto_gathering.set(settings["auto_gathering"])
            self.auto_training.set(settings["auto_training"])
            self.auto_healing.set(settings["auto_healing"])
            self.auto_collecting.set(settings["auto_collecting"])

    def save(self):
        save_settings(
            self.username,
            self.auto_colosseum.get(),
            self.auto_gathering.get(),
            self.auto_training.get(),
            self.auto_healing.get(),
            self.auto_collecting.get()
        )

        Logger.log("Settings saved successfully!")



