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
        self.root.geometry("780x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#201E1E")
        
        self.check_shield       = tk.BooleanVar()
        self.daily_task         = tk.BooleanVar()
        self.auto_colosseum     = tk.BooleanVar()
        self.auto_gathering     = tk.BooleanVar()
        self.auto_healing       = tk.BooleanVar()
        self.auto_collecting    = tk.BooleanVar()
        self.auto_training      = tk.BooleanVar()
        self.auto_crafting      = tk.BooleanVar()
        self.auto_merge         = tk.BooleanVar()
        self.auto_darkness      = tk.BooleanVar()
        self.auto_hunting       = tk.BooleanVar()


        #--------------------------------------
        # frame for overall tasks
        #--------------------------------------
        lords = tk.LabelFrame(
            self.root,
            text = "Quests",
            fg="#FFFFFF",
            bg=("#2E2E2E")
        )
        lords.pack(
            anchor="w",
            fill = "x",
            padx=20,
            pady=(5,0)
        )
        #--------------------------------------
        # frame for truf tasks
        #--------------------------------------
        truf_frame = tk.LabelFrame(
            lords,
            text = "Truf Quests",
            fg = ("#FFFFFF"),
            bg = ("#515151")
        )
        truf_frame.pack(
            side= "left",
            fill = tk.Y,
            padx= 20,
            pady= (20)
        )

        #--------------------------------------
        # shield
        #--------------------------------------
        
        tk.Checkbutton(
            truf_frame,
            text="Check Shield",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.check_shield
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            truf_frame,
            text = "Daily Task",
            fg="#FFFFFF",
            bg="#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable= self.daily_task
        ).pack(anchor="w", padx=20, pady=5)

        #--------------------------------------
        # colosseum
        #--------------------------------------

        tk.Checkbutton(
            truf_frame,
            text="Auto Colosseum",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_colosseum
        ).pack(anchor="w", padx=20, pady=5)

        #----------------------------------------
        # Infimary
        #----------------------------------------

        tk.Checkbutton(
            truf_frame,
            text="Auto Healing",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_healing
        ).pack(anchor="w", padx=20, pady=5)

        #--------------------------------------
        # collect rewards
        #--------------------------------------

        tk.Checkbutton(
            truf_frame,
            text="Auto Collecting",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_collecting
        ).pack(anchor="w", padx=20, pady=5)


        #--------------------------------------
        # auto merge
        #--------------------------------------

        self.pack_lv = tk.StringVar()
        tk.Checkbutton(
            truf_frame,
            text = "Auto Merge",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable= self.auto_merge
        ).pack(side="left", padx= 20, pady=5)

        self.pack_lv = ttk.Combobox(
            truf_frame,
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
        # frame for darkness rally
        #--------------------------------------
        darkness = tk.LabelFrame(
            self.root,
            text = "Darkness",
            fg="#FFFFFF",
            bg=("#515151")           
        )
        darkness.pack(
            anchor= "w",
            fill= "x",
            padx = 20,
            pady = (5,0)
        )
        #--------------------------------------
        # auto join
        #--------------------------------------

        tk.Checkbutton(
            darkness,
            text = "Auto Join",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable = self.auto_darkness
        ).pack(anchor="w", padx=20, pady= 5)


        #--------------------------------------------------
        # creating a frame to train troops
        #--------------------------------------------------

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

        #--------------------------------------
        # auto train
        #--------------------------------------
        
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
        
        tk.Checkbutton(
            train_frame,
            text="Craft Lunite",
            fg = ("#FFFFFF"),
            bg = ("#515151"),
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_crafting        
        ).pack(anchor="w", padx=20, pady= 5)


        #--------------------------------------
        # frame for Kingdom tasks
        #--------------------------------------
        kingdom_frame = tk.LabelFrame(
            lords,
            text = "Kingdom Quests",
            fg = ("#FFFFFF"),
            bg = ("#515151")
        )
        kingdom_frame.pack(
            side = "left",
            fill = tk.Y,
            padx= 20,
            pady= (20)
        )

        #--------------------------------------
        # auto gather
        #--------------------------------------
        

        tk.Checkbutton(
            kingdom_frame,
            text="Auto Gathering",
            fg="#FFFFFF",
            bg="#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_gathering
        ).pack(anchor="w", padx=20, pady=5)


        #--------------------------------------
        # auto hunt
        #--------------------------------------
        self.hunt_lv = tk.StringVar()

        tk.Checkbutton(
            kingdom_frame,
            text="Auto Hunt",
            fg ="#ffffff",
            bg = "#515151",
            selectcolor="#515151",
            activebackground="#515151",
            activeforeground="#FFFFFF",
            variable=self.auto_hunting
        ).pack(side ="left", padx=20, pady=5)

        self.hunt_lv = ttk.Combobox(
            kingdom_frame,
            textvariable= self.hunt_lv,
            state="readonly",
            width= 5,
            values = [
                "Lv 1",
                "Lv 2",
                "Lv 3",
                "Lv 4",
                "Lv 5"
            ]
        )
        self.hunt_lv.pack(
            padx = 20,
            pady= 5,
            side = "right"
        )
        
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
            self.daily_task.set(settings["daily_task"])
            self.auto_colosseum.set(settings["auto_colosseum"])
            self.auto_gathering.set(settings["auto_gathering"])
            self.auto_training.set(settings["auto_training"])
            self.auto_crafting.set(settings["auto_crafting"])
            self.auto_healing.set(settings["auto_healing"])
            self.auto_collecting.set(settings["auto_collecting"])

            self.train_troop.set(settings.get("train_troop",
                                          "T1 Infantry"))

            self.auto_merge.set(settings["auto_merge"])
            self.pack_lv.set(settings.get("pack_lv",
                                             "Pack 1A"))
            
            self.auto_darkness.set(settings["auto_darkness"])

            self.auto_hunting.set(settings["auto_hunting"])
            self.hunt_lv.set(settings.get("hunt_lv",
                                      "Lv 2"))

    def save(self):
        save_settings(
            username            =   self.username,
            check_shield        =   self.check_shield.get(),
            daily_task          =   self.daily_task.get(),
            auto_colosseum      =   self.auto_colosseum.get(),
            auto_gathering      =   self.auto_gathering.get(),
            auto_training       =   self.auto_training.get(),
            auto_crafting       =   self.auto_crafting.get(),
            auto_healing        =   self.auto_healing.get(),
            auto_collecting     =   self.auto_collecting.get(),
            train_troop         =   self.train_troop.get(),
            auto_merge          =   self.auto_merge.get(),
            pack_lv             =   self.pack_lv.get(),
            auto_darkness       =   self.auto_darkness.get(),
            auto_hunting        =   self.auto_hunting.get(),
            hunt_lv             =   self.hunt_lv.get(),
        )

        Logger.log("Settings saved successfully!")