from datetime import datetime
import plotly.express as px
import streamlit as st
import re
import nltk
import pandas as pd
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

dict_to_df ={}
dict_to_df["neg"] = []
dict_to_df["neu"] = []
dict_to_df["pos"] = []
dict_to_df["compound"] = []

dict_to_df["date"] = []

for i in range(21,28):
    with open(f"diary/2023-10-{i}.txt") as file:
        diary = file.read()
    score = analyzer.polarity_scores(diary)
    dict_to_df["neg"].append(score["neg"])
    dict_to_df["neu"].append(score["neu"])
    dict_to_df["pos"].append(score["pos"])
    dict_to_df["compound"].append(score["compound"])

    date_string = f"2023 10 {i}"
    date = datetime.strptime(date_string, "%Y %m %d").date()
    dict_to_df["date"].append(date)
    # date could be directly appended as an f-string (doesn't need to be a specific date format)

df = pd.DataFrame(dict_to_df)

figure_1 = px.line(x=df["date"], y=df["pos"], labels={"x":"Date","y":"Positivity Score"})
figure_2 = px.line(x=df["date"], y=df["neu"], labels={"x":"Date","y":"Neutrality Score"})
figure_3 = px.line(x=df["date"], y=df["neg"], labels={"x":"Date","y":"Negativity Score"})
figure_4 = px.line(x=df["date"], y=df["compound"], labels={"x":"Date","y":"Compound Score"})


st.title("Diary Tone")
with st.expander("Positivity Graph"):
    st.plotly_chart(figure_1, key="figure_1_expander")


st.subheader("Positivity Graph")
st.plotly_chart(figure_1, key = "figure_1_non_expander")
# since figure_1 is being plot at multiple locations each st.plotly_chart() needs a unique "key"

st.subheader("Neutrality Graph")
st.plotly_chart(figure_2)

st.subheader("Negativity Graph")
st.plotly_chart(figure_3)

st.subheader("Compound Score Graph")
st.plotly_chart(figure_4)

figure_5 = px.line(x=df["date"],
                   y=[df["pos"],df["neu"],df["neg"],df["compound"]],
                   labels={"x":"Date","y":"Scores"})
# ok so it's difficult to change the legend names on the plot
# a plot for of multiple plots superpositioned

st.subheader("All Scores")
st.plotly_chart(figure_5)