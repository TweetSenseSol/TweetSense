
import unittest
from tweetsense.sentiment_analysis import analyze_sentiment, label_sentiment

class TestTweetSense(unittest.TestCase):
    def test_analyze_sentiment(self):
        text = "I love using this new product!"
        polarity, subjectivity = analyze_sentiment(text)
        self.assertGreater(polarity, 0)
        self.assertGreaterEqual(subjectivity, 0)

    def test_label_sentiment(self):
        self.assertEqual(label_sentiment(0.5), "positive")
        self.assertEqual(label_sentiment(-0.5), "negative")
        self.assertEqual(label_sentiment(0), "neutral")

if __name__ == '__main__':
    unittest.main()

