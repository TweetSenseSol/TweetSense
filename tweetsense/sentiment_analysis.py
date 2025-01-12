

from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob.
    Returns polarity (float from -1.0 to 1.0) and subjectivity.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

def label_sentiment(polarity):
    """
    Convert polarity score to a label (e.g., negative, neutral, positive).
    """
    if polarity < -0.1:
        return "negative"
    elif polarity > 0.1:
        return "positive"
    else:
        return "neutral"

