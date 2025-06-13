import re
import pandas as pd
import plotly.express as px
import streamlit as st

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")


with open("miracle_in_the_andes.txt", "r", encoding="utf-8") as file:
    book = file.read()

pattern = re.compile("[A-Za-z]+")
findings = re.findall(pattern, book.lower())

dict_word_rep = {}
partial_findings = findings

dict_to_df = {}
dict_to_df["word"] = []
dict_to_df["repetition"] = []

##### method 1 for filling up dict_word_rep (very unoptimized and takes very long)
#for word in partial_findings:
#    dict_word_rep[word]=partial_findings.count(word)
#print(dict_word_rep)

for word in findings:
    if word in dict_word_rep.keys():
        dict_word_rep[word] = dict_word_rep[word] + 1
    else:
        dict_word_rep[word] = 1
print(dict_word_rep)

list_rep_word = [(value,key) for (key, value) in dict_word_rep.items()]
sorted_list_rep_word = sorted(list_rep_word, reverse = True)

### dict_word_rep.items() is of type "dict_items".
# It is a tuple containing a list of tuples.
# Each tuple within that list contains (key, value) in that order
# The above command creates a new list in with tuple are made. Each tuple contains (value, key) in that order
# This is done so that the new list can be sorted with respect to the number of times a word has been repeated (value)

# list_rep_word.sort() modifies the original list
# sorted(list_rep_word) modified a copy of that list

# this part is purely for fun and learning
for (value, key) in list_rep_word:
    dict_to_df["word"].append(key)
    dict_to_df["repetition"].append(value)

print(dict_to_df)

df = pd.DataFrame(dict_to_df)
df_sorted = df.sort_values(by = "repetition", ascending = [False])

figure_1 = px.bar(x=df["word"][:100],
                  y= df["repetition"][:100],
                  labels = {"x":"Word", "y":"Repetitions"})

figure_2 = px.bar(x=df_sorted["word"][:100],
                  y= df_sorted["repetition"][:100],
                  labels = {"x":"Word (Sorted)", "y":"Repetitions"})


figure_3 = px.histogram(data_frame=df, x=df["word"], y=df["repetition"])
figure_4 = px.histogram(data_frame=df_sorted, x=df_sorted["word"], y=df_sorted["repetition"])

st.plotly_chart(figure_1)
st.plotly_chart(figure_2)
st.plotly_chart(figure_3)
st.plotly_chart(figure_4)


filtered_list = []
for (count,word) in sorted_list_rep_word:
    if word not in english_stopwords:
        filtered_list.append((count,word))
print(filtered_list)

