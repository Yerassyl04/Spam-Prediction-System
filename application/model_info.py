import tkinter as tk
from PIL import Image, ImageTk
from navigation import show_page

class ModelInfoPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        accuracy_label = tk.Label(self, text="Model Accuracy", font=("Arial", 16), bg="white")
        accuracy_label.pack(pady=10)

        img_path = 'modeperfomance.png'
        img = Image.open(img_path)
        img = img.resize((600, 600), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        image_label = tk.Label(self, image=img_tk)
        image_label.img = img_tk
        image_label.pack(pady=20)

        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

        back_button = tk.Button(button_frame, text="Back", bg="#90c237", fg="white", font=("Arial", 14),
                                command=lambda: show_page(self.parent, 'main'))
        back_button.pack()

        self.pack(fill=tk.BOTH, expand=True)

