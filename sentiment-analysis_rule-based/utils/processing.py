from models.sentiment_response import SentimentResponse
from utils.preprocessing import clean_text, grading_word, merging_word, counting_grade


def handle_negation(words: list[str], positive_words: list[str], negative_words: list[str]) -> tuple[int, int]:
    # menangani kata negasi
    positive_count = 0
    negative_count = 0

    i = 0
    while i < len(words):
        # menentukan kata setelah "tidak"
        if words[i] == "tidak" and i+1 < len(words):
            next_word = words[i + 1]
            if next_word in positive_words:
                print("tidak " + next_word + " => negative")
                negative_count += 1
            elif next_word in negative_words:
                print("tidak " + next_word + " => positive")
                positive_count += 1
            # lewati kata berikutnya
            i += 2
        else:
            if words[i] in positive_words:
                print(words[i] + " => positive")
                positive_count += 1
            elif words[i] in negative_words:
                print(words[i] + " => negative")
                negative_count += 1
            i += 1

    return positive_count, negative_count


def analyze_sentiment(text: str, positive_words: list[str], negative_words: list[str]) -> SentimentResponse:
    """Menganalisis sentimen teks berdasarkan kata positif dan negatif."""
    # Membersihkan teks
    cleaned_text = clean_text(text)

    print(cleaned_text)

    # Memisahkan teks menjadi kata-kata
    words = cleaned_text.split()

    # Menghitung jumlah kata positif dan negatif dengan negasi
    positive_count, negative_count = handle_negation(words=words, positive_words=positive_words, negative_words=negative_words)

    # Menentukan sentimen
    if positive_count > negative_count:
        return SentimentResponse(text=text, sentiment="Positif", p_point=positive_count, n_point=negative_count)
    elif negative_count > positive_count:
        return SentimentResponse(text=text, sentiment="Negative", p_point=positive_count, n_point=negative_count)
    else:
        return SentimentResponse(text=text, sentiment="Netral", p_point=positive_count, n_point=negative_count)



"""V2"""
import asyncio

from utils.preprocessing import tokenize
from utils.preprocessing import stemming_words

def analyze_sentiment_v2(text: str, positive_words: list[str], negative_words: list[str]) -> SentimentResponse:
    # 1. Tokenisasi antar text
    tokenized_text: list[str] = tokenize(text=text)
    print(f"tokenized text: {tokenized_text}")
    # 2. Stemmer
    stemmed_words: list[str] = stemming_words(words=tokenized_text)
    print(f"stemmed words: {stemmed_words}")
    # 3. Tentukan Nilai Positif masing masing elemen menggunakan tuple
    graded_words: list[tuple[str, int]] = grading_word(words=stemmed_words, positive_words=positive_words, negative_words=negative_words)
    # graded_words: list[tuple[str, int]] = asyncio.run(grading_word_blob(words=stemmed_words))
    print(f"graded words: {graded_words}")
    # 4. Atasi dan satukan elemen positif/negatif yang bersebelahan
    merged_words: list[tuple[str, int]] = merging_word(tuple_words=graded_words)
    print(f"merged words: {merged_words}")
    # 5. Hitung Nilai yang didapat dengan menjumlahkan semua value
    positive_count, negative_count = counting_grade(words=merged_words)

    # Menentukan sentimen
    if positive_count > negative_count:
        return SentimentResponse(text=text, sentiment="Positif", p_point=positive_count, n_point=negative_count)
    elif negative_count > positive_count:
        return SentimentResponse(text=text, sentiment="Negative", p_point=positive_count, n_point=negative_count)
    else:
        return SentimentResponse(text=text, sentiment="Netral", p_point=positive_count, n_point=negative_count)