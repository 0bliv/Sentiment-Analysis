import sqlite3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string
import heapq

nltk.download("punkt")
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Sample text for analysis
text = """
   As an English learner, you will likely want to tell others that English is not your first language. You will also need to ask native speakers to repeat phrases and words or to speak slower.
"""

# Tokenize the text into sentences and words
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Remove stopwords and punctuation
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()
sentiment_score = analyzer.polarity_scores(text)

# Keyword Extraction (Top 5)
word_freq = FreqDist(filtered_words)
top_keywords = heapq.nlargest(5, word_freq, key=word_freq.get)

# Summarization (First 2 sentences)
summary = TreebankWordDetokenizer().detokenize(sentences[:2])

# Store data in SQLite database
conn = sqlite3.connect("analysis_results.db")
cursor = conn.cursor()

# Create a table to store the results
cursor.execute('''
    CREATE TABLE IF NOT EXISTS analysis_results (
        sentiment_score REAL,
        top_keywords TEXT,
        summary TEXT
    )
''')

# Insert the results into the database
cursor.execute("INSERT INTO analysis_results (sentiment_score, top_keywords, summary) VALUES (?, ?, ?)",
               (sentiment_score['compound'], ', '.join(top_keywords), summary))

conn.commit()
conn.close()

# Display Results
print("Sentiment Analysis:")
print(sentiment_score)
print("\nTop Keywords:")
print(top_keywords)
print("\nSummary:")
print(summary)
