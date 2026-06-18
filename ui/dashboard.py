import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import threading
import tkinter as tk
import queue
from tkinter import messagebox
from engine.farming_engine import FarmingEngine
from ui.launch_terminate import launch
from ui.launch_terminate import kill_process_by_name
from engine.task_manager import TaskManager
from ui.settings import SettingsWindow
from utils.logger import Logger
from database.db import get_shield_status


class Dashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username
        self.log_queue = queue.Queue()

        self.root.title("Farming Bot Dashboard")
        self.root.geometry("1024x576")
        self.root.resizable(True, True)
        self.root.configure(bg="#201E1E")

        self.bot_running = False

        self.engine = FarmingEngine(self.username)

        self.task_manager = TaskManager()

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # HEADER
        # ==========================
        # header = tk.Frame(self.root)
        # header.pack(fill="x", pady=10)

        # title = tk.Label(
        #     header,
        #     text="Farming Bot Dashboard",
        #     font=("Arial", 18, "bold"),
        #     fg=("#D5D5D5"),
        #     bg=("#2E2E2E")

        # )
        # title.pack()
        

        # ==========================
        # USER INFO
        # ==========================
        info_frame = tk.LabelFrame(
            self.root,
            text="User Information",
            fg=("#FFFFFF"),
            bg=("#201E1E")
        )
        info_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(
            info_frame,
            text=f"Username: {self.username}",
            font=("Arial", 11),
            fg=("#ffffff"),
            bg=("#201E1E")
        ).pack(anchor="w", padx=10, pady=5)

        # ==========================
        # BOT CONTROL
        # ==========================
        control_frame = tk.LabelFrame(
            self.root,
            text="Bot Controls",
            fg=("#ffffff"),
            bg=("#201E1E")
        )
        control_frame.pack(fill="x", padx=20, pady=10)

        self.status_label = tk.Label(
            control_frame,
            text="Status: Stopped",
            fg="red",
            bg=("#201E1E"),
            font=("Arial", 11, "bold")
        )
        self.status_label.pack(pady=10)

        self.shield_label = tk.Label(
            control_frame,
            text="Shield: Unknown",
            fg="cyan",
            bg="#000000",
            font=("Arial", 10)
        )
        self.shield_label.pack(pady=5)

        start_btn = tk.Button(
            control_frame,
            text="Start Bot",
            width=15,
            bg=("#ffffff"),
            command=self.start_bot
        )
        start_btn.pack(side="left", padx=20, pady=10)

        stop_btn = tk.Button(
            control_frame,
            text="Stop Bot",
            width=15,
            bg=("#ffffff"),
            command=self.stop_bot
        )
        stop_btn.pack(side="left", padx=10)

        # ==========================
        # AUTOMATIC TASKS
        # ==========================

        task_frame = tk.LabelFrame(
            self.root,
            text="Automatic Tasks",
            fg=("#ffffff"),
            bg=("#201E1E")
        )

        task_frame.pack(fill="x",padx=20,pady=10)

        auto_task_btn = tk.Button(
            task_frame,
            text = "Start Automatic Tasks",
            width = 20,
            bg=("#ffffff"),

            command=self.start_automatic_task
        ).pack(side = "left", padx=20, pady=10)

        # ==========================
        # FEATURES
        # ==========================
        feature_frame = tk.LabelFrame(
            self.root,
            text="Features",
            fg=("#ffffff"),
            bg=("#201E1E")
        )
        feature_frame.pack(fill="x", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Settings",
            width=20,
            bg=("#ffffff"),
            command=self.open_settings
        ).pack(side="left", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Logs",
            width=20,
            bg=("#ffffff"),
            command=self.open_logs
        ).pack(side="left", padx=10)

        # ==========================
        # ACTIVITY LOG
        # ==========================
        log_frame = tk.LabelFrame(
            self.root,
            text="Activity",
            fg=("#ffffff"),
            bg=("#201E1E")
        )
        log_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
            
        )

        self.log_box = tk.Text(
            log_frame,
            height=10,
            bg=("#ffffff"),

        )
        self.log_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        Logger.set_callback(
            self.log_queue.put
        )

        self.process_logs()

        Logger.log(
            "Welcome to the Farming Bot Dashboard!"
        )

        self.load_shield_status()

    def add_log(self, message):

        self.root.after(
            0,
            lambda: self._append_log(message)
        )

    def _append_log(self, message):
        self.log_box.insert(
            tk.END,
            f"{message}\n"
        )
        self.log_box.see(tk.END)

    def start_bot(self):

        if not self.bot_running:

            self.bot_running = True

            threading.Thread(
                target=launch,
                daemon=True
                ).start()

            self.status_label.config(
                text="Status: Running",
                fg="green"
            )

            Logger.log("Bot Started.")


    def stop_bot(self):

        if self.bot_running:

            self.bot_running = False
            self.engine.stop()

            kill_process_by_name()

            self.status_label.config(
                text="Status: Stopped",
                fg="red"
            )

            Logger.log("Bot Stopped.")

    def start_automatic_task(self):

        Logger.log("Starting Automatic Tasks...")

        # farming engine task
        # FarmingEngine().start()
        self.engine.start()



    def open_settings(self):

        settings_window = tk.Toplevel()
        SettingsWindow(
            settings_window,
            self.username
        )

    def open_logs(self):

        messagebox.showinfo(
            "Logs",
            "Logs window coming soon."
        )

    def process_logs(self):

        while not self.log_queue.empty():

            message = self.log_queue.get()

            self.log_box.insert(
                tk.END,
                f"{message}\n"
            )

            self.log_box.see(tk.END)

        self.root.after(
            100,
            self.process_logs
        )
    def load_shield_status(self):

        data = get_shield_status(
            self.username
        )
        if not data:
            return
        shield_active, shield_time = data

        if shield_active:
            self.shield_label.config(
                text = f"Shield : {shield_time}"
            )
        else:
            self.shield_label.config(
                text="Shield: Not Active"
            )