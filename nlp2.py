import re
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib as mpl

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()




with open("miracle_in_the_andes.txt", "r", encoding="utf-8") as file:
    book = file.read()

pattern = re.compile("[A-Za-z]+") # pattern to search for words
findings = re.findall(pattern, book.lower()) # the actual search

dict_word_rep = {}
for word in findings:
    if word in dict_word_rep.keys():
        dict_word_rep[word] = dict_word_rep[word] + 1
    else:
        dict_word_rep[word] = 1
print(dict_word_rep)

list_rep_word = [(value,key) for (key, value) in dict_word_rep.items()]
sorted_list_rep_word = sorted(list_rep_word, reverse = True)

dict_to_df = {}
dict_to_df["word"] = []
dict_to_df["repetition"] = []

for (value, key) in list_rep_word:
    dict_to_df["word"].append(key)
    dict_to_df["repetition"].append(value)

filtered_list = []
for (count,word) in sorted_list_rep_word:
    if word not in english_stopwords:
        filtered_list.append((count,word))
df2 = pd.DataFrame(filtered_list)

print(df2)
