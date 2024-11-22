import tkinter as tk
from navigation import show_page

root = tk.Tk()
root.geometry('2000x980')
root.title('Spam Detection Project')

show_page(root, 'main')

root.mainloop()



