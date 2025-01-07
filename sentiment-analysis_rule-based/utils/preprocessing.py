from typing import Tuple

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

# membuat stemmer sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stopwords bahasa indonesia
STOPWORDS = set([
    "yang", "untuk", "dan", "di", "ke", "dari", "ini", "itu", "pada", "dengan",
    "adalah", "juga", "akan", "atau", "saja", "sudah", "lebih", "karena",
    "hanya", "oleh", "seperti", "apa", "mereka", "kita", "saya", "anda"
])

def clean_text(text: str) -> str:
    """
    Membersihkan teks dari tanda baca, mengubahnya menjadi huruf kecil,
    menghapus stopwords, dan melakukan stemming menggunakan Sastrawi.
    """
    # Menghapus tanda baca
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Mengubah text menjadi huruf kecil
    text = text.lower()

    # # menghapus stopwords
    words = text.split()
    # filtered_words = [word for word in words if word not in STOPWORDS]

    # stemming
    stemmed_words = [stemmer.stem(word) for word in words]

    return " ".join(stemmed_words)



"""V2"""

import re

def tokenize(text: str) -> list[str]:
    # memisahkan kata dan tanda baca
    tokens = re.findall(r'\b\w+\b|[.,!?;()]', text)
    return tokens

def stemming_words(words: list[str]) -> list[str]:
    # stem masing masing list yang ada
    stemmed_words: list = [stemmer.stem(word) for word in words]
    return stemmed_words

def grading_word(words: list[str], positive_words: list[str], negative_words: list[str]) -> list[tuple[str, int]]:
    # memberikan nilai pada masing-masing kata
    graded_words: list[tuple[str, int]] = []

    for word in words:
        if word in positive_words:
            graded_words.append((word, 1))
        elif word in negative_words:
            graded_words.append((word, -1))
        else:
            graded_words.append((word, 0))

    return graded_words

def merging_word(tuple_words: list[tuple[str, int]]) -> list[tuple[str, int]]:
    # menggabungkan kata positif/negatif yang bersebelahan
    merged_words: list[tuple[str, int]] = []

    temp_word: list[str] = []
    temp_grade: int = -2

    i: int = 0
    while i < len(tuple_words):
        if tuple_words[i][1] != 0:
            # merging words
            temp_word.append(tuple_words[i][0])
            # calculate grade
            temp_grade = tuple_words[i][1] if temp_grade == -2 else temp_grade * tuple_words[i][1]
            # langsung lanjut ke kata berikutnya jika mengandung graded word
            if i+1 < len(tuple_words) and tuple_words[i+1][1] != 0:
                i += 1
                continue
            else:
                merged_words.append((" ".join(temp_word), temp_grade))
                # reset temporary variable
                temp_word = []
                temp_grade = -2
                i+=1
        else:
            merged_words.append((tuple_words[i][0], tuple_words[i][1]))
            i+=1

    return merged_words


def counting_grade(words: list[tuple[str, int]]) -> tuple[int, int]:
    positive_count: int = 0
    negative_count: int = 0

    for word in words:
        current_grade = word[1]
        if current_grade == 1:
            positive_count += 1
        elif current_grade == -1:
            negative_count += 1

    return positive_count, negative_count




# from textblob import TextBlob
# from googletrans import Translator

# async def grading_word_blob(words: list[str]) -> list[tuple[str, int]]:
#     # memberikan nilai pada masing-masing kata
#     graded_words: list[tuple[str, int]] = []

#     # google translate
#     translator = Translator()

#     for word in words:
#         # translate kata ke english
#         translated = await translator.translate(word, src='id', dest='en')
#         translated_word: str = translated.text
#         # tentukan polaritas menggunakan blob
#         blob = TextBlob(translated_word)
#         polarity = blob.sentiment.polarity
#         # tentukan nilai berdasarkan skor polaritas
#         if polarity > 0:
#             graded_words.append((word, 1))
#         elif polarity < 0:
#             graded_words.append((word, -1))
#         else:
#             graded_words.append((word, 0))

#     return graded_words
