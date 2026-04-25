import streamlit as st
import string
from collections import Counter
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

st.title("💬 Text Analyzer App")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        cleaned_text = clean_text(user_input)

        words = cleaned_text.split()

        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]

        word_count = Counter(filtered_words)
        keywords = word_count.most_common(3)

        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        negative_words = ["depressed", "sad", "tired", "upset", "angry"]

        if any(word in user_input.lower() for word in negative_words):
            sentiment = "😞 Negative"
        elif polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😞 Negative"
        else:
            sentiment = "😐 Neutral"

        st.subheader("Results")
        st.write("Cleaned Text:", cleaned_text)
        st.write("Top Keywords:", keywords)
        st.write("Sentiment:", sentiment)