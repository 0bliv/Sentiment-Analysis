import sqlite3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string
import heapq
import matplotlib.pyplot as plt  # Importe o matplotlib para visualização do gráfico

nltk.download("punkt")
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Entrada do usuário
user_text = input("Enter the text for sentiment analysis: ")

# Texto de exemplo para análise (usado se a entrada do usuário estiver vazia)
if not user_text.strip():
    user_text = """
    As an English learner, you will likely want to tell others that English is not your first language. You will also need to ask native speakers to repeat phrases and words or to speak slower.
    """

# Tokenizar o texto em frases e palavras
sentences = sent_tokenize(user_text)
words = word_tokenize(user_text)

# Remover stopwords e pontuação
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Análise de Sentimento
analyzer = SentimentIntensityAnalyzer()
sentiment_score = analyzer.polarity_scores(user_text)

# Extração de Palavras-chave (Top 5)
word_freq = FreqDist(filtered_words)
top_keywords = heapq.nlargest(5, word_freq, key=word_freq.get)

# Sumarização (Primeiras 2 frases)
summary = TreebankWordDetokenizer().detokenize(sentences[:2])

# Armazenar dados no banco de dados SQLite
conn = sqlite3.connect("analysis_results.db")
cursor = conn.cursor()

# Criar uma tabela para armazenar os resultados, se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS analysis_results (
        sentiment_score REAL,
        top_keywords TEXT,
        summary TEXT
    )
''')

# Inserir os resultados no banco de dados
cursor.execute("INSERT INTO analysis_results (sentiment_score, top_keywords, summary) VALUES (?, ?, ?)",
               (sentiment_score['compound'], ', '.join(top_keywords), summary))

conn.commit()
conn.close()

# Exibir Resultados
print("Sentiment Analysis:")
print(sentiment_score)
print("\nTop Keywords:")
print(top_keywords)
print("\nSummary:")
print(summary)

# Opção para mostrar a visualização do gráfico
show_graph = input("Do you want to show sentiment analysis as a graph? (yes/no): ")

if show_graph.lower() == "yes":
    # Criar um gráfico de barras para visualizar a pontuação de sentimento
    labels = ['Negative', 'Neutral', 'Positive', 'Compound']
    values = [sentiment_score['neg'], sentiment_score['neu'], sentiment_score['pos'], sentiment_score['compound']]
    
    plt.bar(labels, values)
    plt.title('Sentiment Analysis')
    plt.ylabel('Score')
    plt.show()
