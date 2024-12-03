import numpy as np
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
import tkinter as tk
from tkinter import messagebox
#this code works

#stemming
def simple_kazakh_stemmer(word):
    suffixes = [
        'лар', 'лер', 'дар', 'дер', 'тар', 'тер',
        'ым', 'ім', 'мыз', 'міз', 'ымыз', 'іміз', 'ың', 'ің', 'ыңыз', 'іңіз', 'ныкі', 'нікі', 'дікі', 'тікі',
        'ның', 'нің', 'дың', 'дің', 'тың', 'тің', 'ға', 'ге', 'қа', 'ке', 'на', 'не', 'ны', 'ні', 'ды', 'ді',
        'ты', 'ті', 'да', 'де', 'та', 'те', 'нда', 'нде', 'нан', 'нен', 'дан', 'ден', 'тан', 'тен', 'мен', 'бен',
        'пен', 'менен', 'пенен', 'бенен',
        'ған', 'ген', 'қан', 'кен', 'ып', 'іп', 'мақ', 'мек', 'бақ', 'бек', 'пақ', 'пек', 'йық', 'йік', 'пыз', 'піз',
        'сыз', 'сіз', 'шы', 'ші', 'лық', 'лік', 'тық', 'тік', 'дық', 'дік', 'тай', 'тей', 'дас', 'дес', 'тас', 'тес',
        '!', ',', '.', '?', ':', ';'
    ]

    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


#stopwords
kazakh_stopwords = [
    'және', 'бір', 'мен', 'барлық', 'ол', 'бұл', 'біз', 'сіз', 'олар', 'ішінде',
    'бірақ', 'сондай-ақ', 'болып', 'соcын', 'ау', 'та', 'бізде', 'арқылы', 'өзі',
    'үшін', 'менің', 'сенің', 'олардың', 'бізді', 'болады', 'кім', 'не', 'қайда',
    'қашан', 'неге', 'немесе', 'әлде', 'бұрын', 'соң', 'сіздер', 'сосын', 'бәрі',
    'әрбір', 'әртүрлі', 'тек', 'бақыт', 'сонымен', 'мұнда', 'онда', 'белгілі',
    'айту', 'көп', 'жаңа', 'бұл', 'әрі', 'жақсы', 'жаман', 'дегенмен', 'ондай',
    'жол', 'параметр', 'негізінде', 'жүзінде', 'осы', 'сияқты', 'тағы', 'осылай',
    'себеп', 'бар', 'келген', 'кезде', 'ша', 'ше', 'да', 'де', 'та', 'те'
]


# preprocessingF
def preprocess_text_kazakh(text):
    text = text.lower()
    tokens = text.split()
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in kazakh_stopwords]
    tokens = [simple_kazakh_stemmer(word) for word in tokens]
    return " ".join(tokens)


df = pd.read_csv(r"C:\Users\asus\OneDrive\Рабочий стол\MOIS Zhukabayeva T.K\kazspamart.csv", encoding='utf-8')

df = df[['label', 'message']]
df.dropna(inplace=True)

# Apply Kazakh text preprocessing
df['message'] = df['message'].apply(preprocess_text_kazakh)

# Feature extraction using TfidfVectorizer
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['message']).toarray()
y = df['label'].values
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)
# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print(f"Model Precision: {precision:.4f}")
print(f"Model Recall: {recall:.4f}")

# Classification report (precision, recall, f1-score)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

# Function to predict spam or ham for new input
def predict_spam(message):
    processed_message = preprocess_text_kazakh(message)
    print(f"Preprocessed Message: {processed_message}")

    vectorized_message = tfidf.transform([processed_message])
    print(f"Vectorized Message (TF-IDF Features):\n{vectorized_message.toarray()}")

    prediction_prob = model.predict_proba(vectorized_message)
    print(f"Prediction Probability: {prediction_prob}")  # Show the probability for each class (not spam vs spam)

    # Step 4: Make the final prediction
    prediction = model.predict(vectorized_message)[0]
    return "Spam" if prediction == 1 else "Not Spam"


#button click event
def on_predict():
    message = message_entry.get("1.0", tk.END)
    result = predict_spam(message.strip())
    messagebox.showinfo("Prediction Result", f"The message is: {result}")


# tkinter GUI
root = tk.Tk()
root.title("Kazakh Spam Detection")

tk.Label(root, text="Enter your message:").pack(pady=10)
message_entry = tk.Text(root, height=10, width=60)
message_entry.pack(pady=10)

predict_button = tk.Button(root, text="Predict", command=on_predict)
predict_button.pack(pady=20)

root.mainloop()
