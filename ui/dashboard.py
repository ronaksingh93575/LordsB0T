import threading
import tkinter as tk
from tkinter import messagebox
from engine.farming_engine import FarmingEngine
from ui.launch_terminate import launch
from ui.launch_terminate import kill_process_by_name
from engine.task_manager import TaskManager
from ui.settings import SettingsWindow

class Dashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("Farming Bot Dashboard")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#2E2E2E")

        self.bot_running = False

        self.engine = FarmingEngine()

        self.task_manager = TaskManager()

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # HEADER
        # ==========================
        header = tk.Frame(self.root)
        header.pack(fill="x", pady=10)

        title = tk.Label(
            header,
            text="Farming Bot Dashboard",
            font=("Arial", 18, "bold"),
            fg=("#D5D5D5"),
            bg=("#2E2E2E")

        )
        title.pack()
        

        # ==========================
        # USER INFO
        # ==========================
        info_frame = tk.LabelFrame(
            self.root,
            text="User Information",
            fg=("#CBCBCB"),
            bg=("#323232")
        )
        info_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(
            info_frame,
            text=f"Username: {self.username}",
            font=("Arial", 11),
            fg=("#CBCBCB"),
            bg=("#323232")
        ).pack(anchor="w", padx=10, pady=5)

        # ==========================
        # BOT CONTROL
        # ==========================
        control_frame = tk.LabelFrame(
            self.root,
            text="Bot Controls",
            fg=("#CBCBCB"),
            bg=("#323232")
        )
        control_frame.pack(fill="x", padx=20, pady=10)

        self.status_label = tk.Label(
            control_frame,
            text="Status: Stopped",
            fg="red",
            bg=("#323232"),
            font=("Arial", 11, "bold")
        )
        self.status_label.pack(pady=10)

        start_btn = tk.Button(
            control_frame,
            text="Start Bot",
            width=15,
            bg=("#CBCBCB"),
            command=self.start_bot
        )
        start_btn.pack(side="left", padx=20, pady=10)

        stop_btn = tk.Button(
            control_frame,
            text="Stop Bot",
            width=15,
            bg=("#CBCBCB"),
            command=self.stop_bot
        )
        stop_btn.pack(side="left", padx=10)

        # ==========================
        # AUTOMATIC TASKS
        # ==========================

        task_frame = tk.LabelFrame(
            self.root,
            text="Automatic Tasks",
            fg=("#CBCBCB"),
            bg=("#323232")
        )

        task_frame.pack(fill="x",padx=20,pady=10)

        auto_task_btn = tk.Button(
            task_frame,
            text = "Start Automatic Tasks",
            width = 20,
            bg=("#CBCBCB"),

            command=self.start_automatic_task
        ).pack(side = "left", padx=20, pady=10)

        # ==========================
        # FEATURES
        # ==========================
        feature_frame = tk.LabelFrame(
            self.root,
            text="Features",
            fg=("#CBCBCB"),
            bg=("#323232")
        )
        feature_frame.pack(fill="x", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Settings",
            width=20,
            bg=("#CBCBCB"),
            command=self.open_settings
        ).pack(side="left", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Logs",
            width=20,
            bg=("#CBCBCB"),
            command=self.open_logs
        ).pack(side="left", padx=10)

        # ==========================
        # ACTIVITY LOG
        # ==========================
        log_frame = tk.LabelFrame(
            self.root,
            text="Activity",
            fg=("#CBCBCB"),
            bg=("#323232")
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
            bg=("#CBCBCB"),

        )
        self.log_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.add_log("Dashboard loaded.")

    def add_log(self, message):

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


        self.add_log("Bot Started.")
    def stop_bot(self):

        if self.bot_running:

            self.bot_running = False

            kill_process_by_name()

            self.status_label.config(
                text="Status: Stopped",
                fg="red"
            )

            self.add_log("Bot Stopped.")

    def start_automatic_task(self):

        self.add_log(
            "Automatic Task Started."
        )

        print(
            "Automatic Task Running..."
        )


    def open_settings(self):

        settings_window = tk.Toplevel()
        SettingsWindow(
            settings_window
        )

    def open_logs(self):

        messagebox.showinfo(
            "Logs",
            "Logs window coming soon."
        )