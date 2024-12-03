import tkinter as tk
from tkinter import messagebox
from navigation import show_page
from database import connect_db
from hashlib import sha256
from datetime import datetime
from tkcalendar import DateEntry

class RegistrationPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Registration", font=("Arial", 20, "bold"), fg="#90c237").pack(pady=10)

        tk.Label(self, text="First Name:", font=("Arial", 14)).pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Last Name:", font=("Arial", 14)).pack(pady=5)
        self.lastname_entry = tk.Entry(self, font=("Arial", 14))
        self.lastname_entry.pack(pady=5)

        tk.Label(self, text="Date of Birth:", font=("Arial", 14)).pack(pady=5)
        # Create a DateEntry widget for date selection
        self.bod_entry = DateEntry(self, font=("Arial", 14), date_pattern='yyyy-mm-dd')  # Use the format you prefer
        self.bod_entry.pack(pady=5)

        tk.Label(self, text="Gender:", font=("Arial", 14)).pack(pady=5)
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(self, text="Male", variable=self.gender_var, value="Male", font=("Arial", 14)).pack()
        tk.Radiobutton(self, text="Female", variable=self.gender_var, value="Female", font=("Arial", 14)).pack()

        tk.Label(self, text="Password:", font=("Arial", 14)).pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=5)

        tk.Label(self, text="Email:", font=("Arial", 14)).pack(pady=5)
        self.email_entry = tk.Entry(self, font=("Arial", 14))
        self.email_entry.pack(pady=5)

        button_style = {"bg": "#90c237", "fg": "white", "font": ("Arial", 14, "bold")}

        tk.Button(self, text="Register", command=self.register_user, **button_style).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: show_page(self.root, 'main'), **button_style).pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        lastname = self.lastname_entry.get()
        bod = self.bod_entry.get_date()
        gender = self.gender_var.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        if not username or not lastname or not bod or not password or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        hashed_password = sha256(password.encode('utf-8')).hexdigest()


        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO userdata (username, lastname, bod, gender, password, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (username, lastname, bod, gender, hashed_password, email))
            conn.commit()
            messagebox.showinfo("Success", "Registration completed successfully!")
            show_page(self.root, 'login')
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
        finally:
            cursor.close()
            conn.close()
