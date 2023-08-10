#----------------STREAMLIT----------------------#
# import pickle
# import string
# import streamlit as st
# from nltk.corpus import stopwords
# import nltk
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()


# tfidf = pickle.load(open('vecotizor.pkl','rb'))
# mnb = pickle.load(open('mnb.pkl','rb'))

# st.title("Email spam classifier")

# def transfrom_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)

#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i) 

#     text = y[:]
#     y.clear()

#     for i in text:
#         y.append(lemmatizer.lemmatize(i))

#     return " ".join(y)


# input_mail = st.text_input("Enter your mail here: ")

# if st.button("Predict"):
#     transfrom_mail = transfrom_text(input_mail)

#     vector_input = tfidf.transform([transfrom_mail])

#     result = mnb.predict((vector_input)[0])

#     if result == 1:
#         st.header("Spam")
#     if result == 0:
#         st.header("Not spam")

#--------------FLASK----------------------#
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = 