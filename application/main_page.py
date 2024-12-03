import tkinter as tk
from PIL import Image, ImageTk  # Importing PIL for image handling
from navigation import show_page

class MainPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.configure(bg="#edf2f4")
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        button_style = {
            "bg": "#90c237",
            "fg": "white",
            "font": ("Arial", 14, "bold"),
            "width": 15,
            "height": 2,
        }

        # Button frame and buttons
        button_frame = tk.Frame(self, bg="#edf2f4")
        button_frame.pack(pady=50)

        # Grid buttons
        tk.Button(button_frame, text="Sign in", command=lambda: show_page(self.root, 'registration'), **button_style).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Log in", command=lambda: show_page(self.root, 'login'), **button_style).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Contacts", command=lambda: show_page(self.root, 'contacts'), **button_style).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(button_frame, text="About us", command=lambda: show_page(self.root, 'about'), **button_style).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(button_frame, text="About Model", command=lambda: show_page(self.root, 'model_info'), **button_style).grid(row=0, column=4, padx=10, pady=10)
        tk.Button(button_frame, text="Spam prediction", command=lambda: show_page(self.root, 'spam_check'), **button_style).grid(row=0, column=5, padx=10, pady=10)

        # Load the image using Pillow
        original_image = Image.open("mains.png")  # Ensure correct path
        resized_image = original_image.resize((900, 600))  # Resize to desired dimensions (width, height)
        self.photo = ImageTk.PhotoImage(resized_image)  # Convert to a Tkinter-compatible image

        # Display resized image below the buttons
        image_label = tk.Label(self, image=self.photo, bg="#edf2f4")
        image_label.pack(pady=20)  # Add some padding between the buttons and the image

