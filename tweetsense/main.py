
import time
import streamlit as st
from .twitter_stream import create_twitter_client, fetch_recent_tweets
from .sentiment_analysis import analyze_sentiment, label_sentiment
from .dashboard import display_dashboard

def run_tweetsense_app():
    # Create the Twitter client
    api = create_twitter_client()

    # This is a simple loop to fetch & display tweets regularly.
    # For a production app, consider a more efficient scheduling approach.
    st.write("Fetching tweets and analyzing sentiment. Please wait...")

    while True:
        # Fetch tweets
        tweets = fetch_recent_tweets(api)

        # Analyze sentiment
        for tweet in tweets:
            polarity, _ = analyze_sentiment(tweet["text"])
            tweet["sentiment_score"] = polarity
            tweet["sentiment_label"] = label_sentiment(polarity)

        # Display on the dashboard
        display_dashboard(tweets)

        # Sleep for a short interval before refreshing
        time.sleep(30)

if __name__ == "__main__":
    run_tweetsense_app()

