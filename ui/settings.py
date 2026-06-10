import tkinter as tk


class SettingsWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Bot Settings")
        self.root.geometry("400x300")
        

        self.auto_gather = tk.BooleanVar()
        self.auto_heal = tk.BooleanVar()
        self.auto_training = tk.BooleanVar()

        tk.Checkbutton(
            root,
            text="Auto Gather",
            variable=self.auto_gather
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Heal",
            variable=self.auto_heal
        ).pack(anchor="w", padx=20, pady=5)

        tk.Checkbutton(
            root,
            text="Auto Training",
            variable=self.auto_training
        ).pack(anchor="w", padx=20, pady=5)

        tk.Button(
            root,
            text="Save Settings",
            command=self.save_settings
        ).pack(pady=20)

    def save_settings(self):

        print("Settings Saved")