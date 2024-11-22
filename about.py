import tkinter as tk
from navigation import show_page


class AboutPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Arial", 14)

        tk.Label(self, text="About This Project", font=("Arial", 20, "bold"), fg="#90c237").pack(pady=10)

        about_text = """This project is a spam detection system that allows users to:
- Register and login to the platform
- Check emails for potential spam
- Stay informed on spam detection methods

The system uses machine learning models to classify emails as spam or not. 
Our goal is to make email communication safer for users by identifying malicious or unwanted content.

For more information, please contact us."""

        tk.Label(self, text=about_text, font=label_font, justify="left", padx=20).pack(pady=10)

        button_style = {"bg": "#90c237", "fg": "white", "font": ("Arial", 14, "bold")}
        tk.Button(self, text="Back", command=lambda: show_page(self.root, 'main'), **button_style).pack(pady=10)
