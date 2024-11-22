import tkinter as tk
from navigation import show_page


class ContactsPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):

        label_font = ("Arial", 14)

        tk.Label(self, text="Contact Us", font=("Arial", 20, "bold"), fg="#90c237").pack(pady=10)

        contact_info = """You can reach us through the following channels:

Email: thisyera@gmail.cpm
Phone: +7 707 137 37 05
Address: Satbayev 2, Astana, Kazakhstan

Our team is always available to assist you!"""

        tk.Label(self, text=contact_info, font=label_font, justify="left", padx=20).pack(pady=10)

        tk.Label(self, text="Send us a message:", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self, text="Your Message:", font=label_font).pack(pady=5)
        self.message_entry = tk.Text(self, height=6, width=40, font=("Arial", 14))
        self.message_entry.pack(pady=5)

        button_style = {"bg": "#90c237", "fg": "white", "font": ("Arial", 14, "bold")}
        tk.Button(self, text="Send Message", command=self.send_message, **button_style).pack(pady=10)

        tk.Button(self, text="Back", command=lambda: show_page(self.root, 'main'), **button_style).pack(pady=10)

    def send_message(self):
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            tk.messagebox.showerror("Error", "Please enter a message before sending.")
            return
        tk.messagebox.showinfo("Success", "Your message has been sent!")
        self.message_entry.delete("1.0", tk.END)
