from tkinter import Frame

def show_page(root, page_name):
    for widget in root.winfo_children():
        widget.destroy()

    if page_name == 'main':
        from main_page import MainPage
        page = MainPage(root)
    elif page_name == 'registration':
        from registration import RegistrationPage
        page = RegistrationPage(root)
    elif page_name == 'login':
        from login import LoginPage
        page = LoginPage(root)
    elif page_name == 'contacts':
        from contacts import ContactsPage
        page = ContactsPage(root)
    elif page_name == 'about':
        from about import AboutPage
        page = AboutPage(root)
    elif page_name == 'model_info':
        from model_info import ModelInfoPage
        page = ModelInfoPage(root)
    elif page_name == 'spam_check':
        from spam_check import SpamCheckPage
        page = SpamCheckPage(root)

    page.pack()
