from models.sentiment_response import SentimentResponse
from utils.load_words import load_words
from utils.processing import analyze_sentiment

# List kata-kata positif dan negatif
positive_words, negative_words = load_words("words.txt")

# Contoh teks
texts = [
    "Hari ini saya merasa sangat bahagia dan puas!",
    "Saya sangat sedih karena pekerjaan saya berantakan.",
    "Kegiatan hari ini biasa saja, tidak ada yang istimewa.",
    "Git pull ini membuat saya kesal karena itu menghapus seluruh kodinganku di main",
    "barang berbahan plastik, tidak mudah patah",
    "Barang ini sangat buruk, sangat gampang rusak ketika digunakan",
    "Barang ini sangat rusak, buruk, jelek, gagal, susah, tidak",
]

def display_result(r: SentimentResponse):
    print(f"Teks: {r.text}")
    print(f"Sentimen: {r.sentiment}")
    print(f"Poin Positif: {r.p_point}")
    print(f"Poin Negatif: {r.n_point}\n")

# Menganalisis sentimen untuk setiap teks
for text in texts:
    response: SentimentResponse = analyze_sentiment(text=text, positive_words=positive_words, negative_words=negative_words)
    display_result(r=response)

print("-----=================== V2 ==================-----")

from utils.processing import analyze_sentiment_v2

for text in texts:
    response: SentimentResponse = analyze_sentiment_v2(text=text, positive_words=positive_words, negative_words=negative_words)
    display_result(r=response)