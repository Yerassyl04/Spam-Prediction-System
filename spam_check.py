import tkinter as tk
from tkinter import messagebox
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
from navigation import show_page

nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    tokens = [word for word in tokens if word.isalnum()]  # Remove special characters
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    tokens = [ps.stem(word) for word in tokens]  # Perform stemming
    return " ".join(tokens)


# Load the model and the vectorizer
df = pd.read_csv('spame.csv', encoding='ISO-8859-1')
df = df[['v1', 'v2']]  # Only keep relevant columns
df.columns = ['label', 'message']  # Rename columns
df.dropna(inplace=True)  # Drop missing values
df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Convert labels to 0 and 1

df['message'] = df['message'].apply(preprocess_text)

tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['message']).toarray()
y = df['label'].values

# Train the model
model = MultinomialNB()
model.fit(X, y)


def predict_spam():
    message = entry.get()
    if message:
        processed_message = preprocess_text(message)  # Preprocess the input text
        message_vector = tfidf.transform([processed_message]).toarray()  # Vectorize the message
        prediction = model.predict(message_vector)  # Predict spam or ham

        # Show result in a messagebox
        if prediction[0] == 1:
            messagebox.showinfo("Prediction", "This message is Spam!")
        else:
            messagebox.showinfo("Prediction", "This message is Ham (Not Spam).")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to check.")


# Define the SpamCheckPage class
class SpamCheckPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        # Center the frame
        self.grid(row=0, column=0, sticky="nsew")

        # Define the standard label font and button style
        label_font = ("Arial", 14)
        button_style = {"bg": "#90c237", "fg": "white", "font": ("Arial", 14, "bold")}

        # Title Label with standard font
        label = tk.Label(self, text="Spam Message Checker", font=label_font, bg="white")
        label.grid(row=0, column=0, pady=20)

        # Text Entry Field for the user input
        global entry
        entry = tk.Entry(self, width=70, font=("Arial", 14))
        entry.grid(row=1, column=0, pady=10, padx=20)


        predict_button = tk.Button(self, text="Check Spam", command=predict_spam, **button_style)
        predict_button.grid(row=2, column=0, pady=20, padx=10, sticky="w")

        back_button = tk.Button(self, text="Back", command=lambda: show_page(self.parent, 'main'), **button_style)
        back_button.grid(row=2, column=0, pady=20, padx=10, sticky="e")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
