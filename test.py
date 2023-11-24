# Install required packages
# pip install streamlit nltk

import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Download NLTK data if not already downloaded
import nltk
nltk.download('punkt')

def extract_ngrams(text, n):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Generate n-grams
    n_grams = list(ngrams(words, n))

    return n_grams

# Streamlit web app
def main():
    st.title("N-gram Extractor")

    # User input: Text passage
    text_input = st.text_area("Enter your text passage:")

    # User input: N for n-grams
    n_value = st.slider("Select the value of N for n-grams:", 1, 5, 2)

    if st.button("Extract N-grams"):
        if text_input:
            # Extract n-grams
            n_grams = extract_ngrams(text_input, n_value)

            # Display n-grams
            st.subheader(f"{n_value}-grams:")
            st.write(n_grams)
        else:
            st.warning("Please enter a text passage.")

if __name__ == "__main__":
    main()
