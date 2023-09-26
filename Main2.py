import tkinter as tk
from tkinter import messagebox
import sqlite3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string
import heapq
import matplotlib.pyplot as plt

nltk.download("punkt")
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Função para realizar a análise de sentimento
def analyze_sentiment():
    user_text = text_input.get("1.0", "end-1c")  # Obter o texto da caixa de entrada

    if not user_text.strip():
        messagebox.showinfo("Aviso", "Por favor, insira um texto para análise de sentimento.")
        return

    sentences = sent_tokenize(user_text)
    words = word_tokenize(user_text)

    stop_words = set(stopwords.words("english"))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(user_text)

    word_freq = FreqDist(filtered_words)
    top_keywords = heapq.nlargest(5, word_freq, key=word_freq.get)

    summary = TreebankWordDetokenizer().detokenize(sentences[:2])

    conn = sqlite3.connect("analysis_results.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            sentiment_score REAL,
            top_keywords TEXT,
            summary TEXT
        )
    ''')

    cursor.execute("INSERT INTO analysis_results (sentiment_score, top_keywords, summary) VALUES (?, ?, ?)",
                   (sentiment_score['compound'], ', '.join(top_keywords), summary))

    conn.commit()
    conn.close()

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Análise de Sentimento:\n")
    result_text.insert(tk.END, f"Pontuação: {sentiment_score}\n\n")
    result_text.insert(tk.END, "Palavras-chave Principais:\n")
    result_text.insert(tk.END, f"{', '.join(top_keywords)}\n\n")
    result_text.insert(tk.END, "Resumo:\n")
    result_text.insert(tk.END, summary)
    result_text.config(state=tk.DISABLED)

    show_graph = messagebox.askquestion("Exibir Gráfico", "Deseja exibir a análise de sentimento como um gráfico?")
    
    if show_graph == "yes":
        labels = ['Negativo', 'Neutro', 'Positivo', 'Composto']
        values = [sentiment_score['neg'], sentiment_score['neu'], sentiment_score['pos'], sentiment_score['compound']]
    
        plt.bar(labels, values)
        plt.title('Análise de Sentimento')
        plt.ylabel('Pontuação')
        plt.show()

# Configuração da janela
root = tk.Tk()
root.title("Análise de Sentimento")

# Caixa de entrada de texto
text_label = tk.Label(root, text="Insira o texto para análise :")
text_label.pack()

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Botão de análise
analyze_button = tk.Button(root, text="Analisar", command=analyze_sentiment)
analyze_button.pack()

# Resultados
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()

root.mainloop()
