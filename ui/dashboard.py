import tkinter as tk
from tkinter import messagebox
from bot.farming_engine import FarmingEngine


class Dashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("Farming Bot Dashboard")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.bot_running = False

        self.engine = FarmingEngine()

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
            font=("Arial", 18, "bold")
        )
        title.pack()

        # ==========================
        # USER INFO
        # ==========================
        info_frame = tk.LabelFrame(
            self.root,
            text="User Information"
        )
        info_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(
            info_frame,
            text=f"Username: {self.username}",
            font=("Arial", 11)
        ).pack(anchor="w", padx=10, pady=5)

        # ==========================
        # BOT CONTROL
        # ==========================
        control_frame = tk.LabelFrame(
            self.root,
            text="Bot Controls"
        )
        control_frame.pack(fill="x", padx=20, pady=10)

        self.status_label = tk.Label(
            control_frame,
            text="Status: Stopped",
            fg="red",
            font=("Arial", 11, "bold")
        )
        self.status_label.pack(pady=10)

        start_btn = tk.Button(
            control_frame,
            text="Start Bot",
            width=15,
            command=self.start_bot
        )
        start_btn.pack(side="left", padx=20, pady=10)

        stop_btn = tk.Button(
            control_frame,
            text="Stop Bot",
            width=15,
            command=self.stop_bot
        )
        stop_btn.pack(side="left", padx=10)

        # ==========================
        # FEATURES
        # ==========================
        feature_frame = tk.LabelFrame(
            self.root,
            text="Features"
        )
        feature_frame.pack(fill="x", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Settings",
            width=20,
            command=self.open_settings
        ).pack(side="left", padx=20, pady=10)

        tk.Button(
            feature_frame,
            text="Logs",
            width=20,
            command=self.open_logs
        ).pack(side="left", padx=10)

        # ==========================
        # ACTIVITY LOG
        # ==========================
        log_frame = tk.LabelFrame(
            self.root,
            text="Activity"
        )
        log_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.log_box = tk.Text(
            log_frame,
            height=10
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

            self.engine.start()

            self.status_label.config(
                text="Status: Running",
                fg="green"
            )

        self.add_log("Bot Started.")
    def stop_bot(self):

        if self.bot_running:

            self.bot_running = False

            self.engine.stop()

            self.status_label.config(
                text="Status: Stopped",
                fg="red"
            )

            self.add_log("Bot Stopped.")    


    def open_settings(self):

        messagebox.showinfo(
            "Settings",
            "Settings window coming soon."
        )

    def open_logs(self):

        messagebox.showinfo(
            "Logs",
            "Logs window coming soon."
        )