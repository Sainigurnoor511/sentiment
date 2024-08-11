import streamlit as st

st.title("😊 😐 😠  Sentiment Analysis")
st.title("Sentiment Analysis")
st.write("An app to analyse your reviews")


user_input = st.text_input("Please enter your review >>: ")

specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")


if (specific_model(user_input)[0]['label']) == "POS" :
    print("Positive")
elif (specific_model(user_input)[0]['label']) == "NEU" :
    print("Neutral")
elif (specific_model(user_input)[0]['label']) == "NEG" :
    print("Negative")
else :
    print("Error")


if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")