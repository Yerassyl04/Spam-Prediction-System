import tkinter as tk
from tkinter import messagebox
from navigation import show_page
from database import connect_db
from hashlib import sha256

class LoginPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Arial", 14)
        button_style = {"bg": "#90c237", "fg": "white", "font": ("Arial", 14, "bold")}

        # Title label for the page
        tk.Label(self, text="Login", font=("Arial", 20, "bold"), fg="#90c237").pack(pady=10)

        tk.Label(self, text="Email:", font=label_font).pack(pady=5)
        self.email_entry = tk.Entry(self, font=label_font)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=label_font).pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=label_font)
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.login_user, **button_style).pack(pady=10)

        tk.Button(self, text="Back", command=lambda: show_page(self.root, 'main'), **button_style).pack(pady=10)

    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        hashed_password = sha256(password.encode('utf-8')).hexdigest()

        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM userdata WHERE email = %s AND password = %s", (email, hashed_password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "You have successfully logged in!")
                show_page(self.root, 'spam_check')
            else:
                messagebox.showerror("Error", "Invalid email or password.")
        except Exception as e:
            messagebox.showerror("Error", f"Login error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

