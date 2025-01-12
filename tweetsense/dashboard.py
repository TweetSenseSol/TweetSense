
import streamlit as st
import pandas as pd
from typing import List, Dict

def display_dashboard(tweets: List[Dict]):
    """
    Display Streamlit-based dashboard for tweets and their sentiment.
    """

    st.title("TweetSense: Real-Time Twitter Sentiment Dashboard")

    if not tweets:
        st.write("No tweets to display at the moment.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(tweets)

    # Show table
    st.subheader("Recent Tweets")
    st.dataframe(df[["user", "text", "sentiment_label", "sentiment_score"]])

    # Basic stats
    sentiment_counts = df["sentiment_label"].value_counts()
    st.subheader("Sentiment Distribution")
    st.bar_chart(sentiment_counts)

    # If you want to show average sentiment, etc.
    avg_polarity = df["sentiment_score"].mean()
    st.subheader("Average Polarity Score")
    st.metric("Polarity (mean)", f"{avg_polarity:.2f}")

