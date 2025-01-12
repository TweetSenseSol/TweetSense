
import tweepy
from .config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
    SEARCH_KEYWORDS,
    MAX_TWEETS
)

def create_twitter_client():
    """
    Create and authenticate a Tweepy client.
    """
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def fetch_recent_tweets(api, query=SEARCH_KEYWORDS, count=MAX_TWEETS):
    """
    Fetch recent tweets for given keywords.
    Returns a list of tweet objects.
    """
    if isinstance(query, list):
        query = " OR ".join(query)

    fetched_tweets = api.search_tweets(q=query, lang="en", count=count, tweet_mode="extended")
    tweets_data = []

    for tweet in fetched_tweets:
        # Some tweets store text in 'full_text' instead of 'text'
        text = tweet.full_text if hasattr(tweet, "full_text") else tweet.text

        tweets_data.append({
            "id": tweet.id_str,
            "user": tweet.user.screen_name,
            "text": text,
            "created_at": tweet.created_at
        })

    return tweets_data

