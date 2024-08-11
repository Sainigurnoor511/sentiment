import streamlit as st
from transformers import pipeline

st.title("😊 😐 😠  Sentiment Analysis")
st.title("Sentiment Analysis")
st.write("An app to analyse your reviews")


user_input = st.text_input("Please enter your review >>: ")

specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")


if (specific_model(user_input)[0]['label']) == 0:
    st.write(" ")
elif (specific_model(user_input)[0]['label']) == "POS" :
    st.write("# 😊 Positive")
elif (specific_model(user_input)[0]['label']) == "NEU" :
    st.write("# 😐 Neutral")
elif (specific_model(user_input)[0]['label']) == "NEG" :
    st.write("# 😠 Negative")
else :
    st.write("# ☠️ Error ☠️")