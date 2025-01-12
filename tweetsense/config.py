
import os

# In practice, set these via environment variables or a secure vault
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "YOUR_TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "YOUR_TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "YOUR_TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "YOUR_TWITTER_ACCESS_SECRET")

# Additional configuration constants
SEARCH_KEYWORDS = ["solana", "web3", "crypto"]  # Change whatever you want
MAX_TWEETS = 100  # Example number of tweets to fetch

