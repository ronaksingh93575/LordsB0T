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
from database.supabase_db import get_user_settings, save_settings
from logs.logger import Logger
from tkinter import ttk


class SettingsWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("Bot Settings")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#201E1E")
        
        self.check_shield       = tk.BooleanVar()
        self.auto_colosseum     = tk.BooleanVar()
        self.auto_gathering     = tk.BooleanVar()
        self.auto_healing       = tk.BooleanVar()
        self.auto_collecting    = tk.BooleanVar()
        self.auto_training      = tk.BooleanVar()
        self.auto_merge         = tk.BooleanVar()
        self.auto_darkness      = tk.BooleanVar()

        #--------------------------------------
        # shield
        #--------------------------------------
        
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

        #--------------------------------------
        # colosseum
        #--------------------------------------

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


        #--------------------------------------------------
        # creating a frame to train troops
        #--------------------------------------------------

        #--------------------------------------
        # auto train
        #--------------------------------------

        train_frame = tk.LabelFrame(
            self.root,
            text="Training",
            fg="#FFFFFF",
            bg=("#515151")
        )
        train_frame.pack(
            anchor="w",
            fill="x",
            padx=20,
            pady=(5,0)
            )
        
        self.train_troop= tk.StringVar()

        tk.Checkbutton(
            train_frame,
            text="Auto Training",
            fg="#FFFFFF",
            bg="#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_training
        ).pack(side="left", padx=20, pady=5)
        
        self.train_troop = ttk.Combobox(
            train_frame,
            textvariable= self.train_troop,
            state="readonly",
            width = 20,
            values=[
                "T1 Infantry",
                "T1 Ranged",
                "T1 Cavalry",
                "T1 Siege",

                "T2 Infantry",
                "T2 Ranged",
                "T2 Cavalry",
                "T2 Siege",

                "T3 Infantry",
                "T3 Ranged",
                "T3 Cavalry",
                "T3 Siege",

                "T4 Infantry",
                "T4 Ranged",
                "T4 Cavalry",
                "T4 Siege",
                
                
                ]
        )
        self.train_troop.pack(
            padx=20,
            pady=5,
            side="right"
        )
        #--------------------------------------
        # auto gather
        #--------------------------------------
        

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


        
        #----------------------------------------
        # auto heal
        #----------------------------------------

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

        #--------------------------------------
        # collect rewards
        #--------------------------------------

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


        #--------------------------------------
        # creating a frame for merge
        #--------------------------------------
        
        merge_frame = tk.LabelFrame(
            self.root,
            text="Merge",
            fg = "#FFFFFF",
            bg = "#515151"
        )
        merge_frame.pack(
            anchor="w",
            fill="x",
            padx =20,
            pady= (5,0)
        )

        #--------------------------------------
        # auto merge
        #--------------------------------------

        self.pack_lv = tk.StringVar()
        tk.Checkbutton(
            merge_frame,
            text = "Auto Merge",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable= self.auto_merge
        ).pack(side="left", padx= 20, pady=5)

        self.pack_lv = ttk.Combobox(
            merge_frame,
            textvariable= self.pack_lv,
            state = "readonly",
            width = 20,
            values=[
                "Pack 1A",
                "Pack 1B",
                "Pack 2A",
                "Pack 2B",
                "Pack 3",
                "Pack 4"
            ]
        )
        self.pack_lv.pack(
            padx =20,
            pady = 5,
            side = "right"
        )

        #--------------------------------------
        # creating frame for rally darkness
        #--------------------------------------

        darkness_frame = tk.LabelFrame(
            self.root,
            text = "Darkness",
            fg = "#FFFFFF",
            bg = "#515151"
        )
        darkness_frame.pack(
            anchor="w",
            fill="x",
            padx =20,
            pady = (5,0)
        )

        #--------------------------------------
        # auto join
        #--------------------------------------

        tk.Checkbutton(
            darkness_frame,
            text = "Auto Join",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable = self.auto_darkness
        ).pack(side="left", padx=20, pady= 5)


        #--------------------------------------
        # save settings
        #--------------------------------------

        tk.Button(
            root,
            text="Save Settings",
            command=self.save
        ).pack(pady=20)

        self.load_settings()

    def load_settings(self):
        settings = get_user_settings(self.username)
        if settings:
            self.check_shield.set(settings["check_shield"])
            self.auto_colosseum.set(settings["auto_colosseum"])
            self.auto_gathering.set(settings["auto_gathering"])
            self.auto_training.set(settings["auto_training"])
            self.auto_healing.set(settings["auto_healing"])
            self.auto_collecting.set(settings["auto_collecting"])

            self.train_troop.set(settings.get("train_troop",
                                          "T1 Infantry"))

            self.auto_merge.set(settings["auto_merge"])

            self.pack_lv.set(settings.get("pack_lv",
                                             "Pack 1A"))
            self.auto_darkness.set(settings["auto_darkness"])

    def save(self):
        save_settings(
            username            =   self.username,
            check_shield        =   self.check_shield.get(),
            auto_colosseum      =   self.auto_colosseum.get(),
            auto_gathering      =   self.auto_gathering.get(),
            auto_training       =   self.auto_training.get(),
            auto_healing        =   self.auto_healing.get(),
            auto_collecting     =   self.auto_collecting.get(),
            train_troop         =   self.train_troop.get(),
            auto_merge          =   self.auto_merge.get(),
            pack_lv             =   self.pack_lv.get(),
            auto_darkness       =   self.auto_darkness.get(),
        )

        Logger.log("Settings saved successfully!")