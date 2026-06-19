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
import sqlite3
# from database.supabase_db import DATABASE_PATH
from database.supabase_db import get_user_settings, save_settings
from logs.logger import Logger


class SettingsWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("Bot Settings")
        self.root.geometry("500x350")
        self.root.resizable(True, True)
        self.root.configure(bg="#201E1E")
        
        self.check_shield = tk.BooleanVar()
        self.auto_colosseum = tk.BooleanVar()
        self.auto_gathering = tk.BooleanVar()
        self.auto_training = tk.BooleanVar()
        self.auto_healing = tk.BooleanVar()
        self.auto_collecting = tk.BooleanVar()

        self.load_settings()
        
        tk.Checkbutton(
            root,
            text="Check Shield",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
            variable=self.check_shield
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Colosseum",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
            variable=self.auto_colosseum
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Gathering",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
            variable=self.auto_gathering
        ).pack(anchor="w", padx=20, pady=5)

        #--------------------------------------------------
        # creating a frame to train troops
        #--------------------------------------------------

        train_frame = tk.LabelFrame(
            self.root,
            text="Training",
            bg=("#FFFFFF")
        )
        train_frame.pack(pady=10)
        
        tk.Checkbutton(
            train_frame,
            text="Auto Training",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
            variable=self.auto_training
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Healing",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
            variable=self.auto_healing
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Collecting",
            fg="#FFFFFF",
            bg="#201E1E",
            selectcolor="#201E1E",
            activebackground="#201E1E",
            activeforeground="#FFFFFF",
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
            self.check_shield.set(settings["check_shield"])
            self.auto_colosseum.set(settings["auto_colosseum"])
            self.auto_gathering.set(settings["auto_gathering"])
            self.auto_training.set(settings["auto_training"])
            self.auto_healing.set(settings["auto_healing"])
            self.auto_collecting.set(settings["auto_collecting"])

    def save(self):
        save_settings(
            self.username,
            self.check_shield.get(),
            self.auto_colosseum.get(),
            self.auto_gathering.get(),
            self.auto_training.get(),
            self.auto_healing.get(),
            self.auto_collecting.get()
        )

        Logger.log("Settings saved successfully!")