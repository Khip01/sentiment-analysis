
from models.data import Data
from models.naive_bayes import NaiveBayes
from models.preprocessed_data import PreprocessedData
from models.sentiment_response import SentimentResponse
from utils.preprocessing_data import sentence_preprocessing

# Pada apply model ini akan dilakukan prediksi
# terhadap data testing yang telah di preprocessing
# dengan menggunakan models yang telah dibuat pada naive bayes
# 1. Melakukan Preprocessing pada data testing, 
#    sehingga data testing menjadi lebih mudah diolah
# 2. Melakukan prediksi terhadap data testing 
#    dengan menggunakan models yang telah dibuat
# 3. Mengembalikan hasil prediksi
def apply_model(source, model: NaiveBayes) -> list[SentimentResponse]:
    result: list[SentimentResponse] = []

    if isinstance(source, Data):
        data = source
        # preprocessing pada data
        preprocessed_data: PreprocessedData = sentence_preprocessing(data=data)
        # melakukan prediksi pada data
        sentiment_response: SentimentResponse = predict_data(preprocessed_data=preprocessed_data, model=model)
        # menyimpan ke result
        result.append(sentiment_response)
    elif isinstance(source, list):
        datas = source
        # loop setiap data yang ada
        for data in datas:
            # preprocessing pada data
            preprocessed_data: PreprocessedData = sentence_preprocessing(data=data)
            # melakukan prediksi pada data
            sentiment_response: SentimentResponse = predict_data(preprocessed_data=preprocessed_data, model=model)
            # menyimpan ke result
            result.append(sentiment_response)

    return result


def predict_data(preprocessed_data: PreprocessedData, model: NaiveBayes) -> SentimentResponse:
    pos_words: list[tuple[str, float]] = []
    neg_words: list[tuple[str, float]] = []
    neu_words: list[tuple[str, float]] = []

    # stores the probability of words that have been found
    for word in preprocessed_data.preprocessed_sentence:
        for word_prob in model.list_word_prob:
            if word == word_prob.word:
                if word_prob.label == "positif": pos_words.append((word_prob.word, word_prob.probability))
                elif word_prob.label == "negatif": neg_words.append((word_prob.word, word_prob.probability))
                elif word_prob.label == "netral": neu_words.append((word_prob.word, word_prob.probability))

    # calculate the probability
    calc_prob_pos_data: float = calc_words_prob(category_words=pos_words) * model.positive_prob
    calc_prob_neg_data: float = calc_words_prob(category_words=neg_words) * model.negative_prob
    calc_prob_neu_data: float = calc_words_prob(category_words=neu_words) * model.neutral_prob

    # summarize the predicted labels/category from the probabilities
    predicted_label: str = ""
    if calc_prob_pos_data > calc_prob_neg_data and calc_prob_pos_data > calc_prob_neu_data:
        predicted_label = "positif"
    elif calc_prob_neg_data > calc_prob_pos_data and calc_prob_neg_data > calc_prob_neu_data:
        predicted_label = "negatif"
    else:
        predicted_label = "netral"

    # return the result of the sentiment analys
    return SentimentResponse(
        sentence=preprocessed_data.sentence,
        predicted_label=predicted_label,
        pos_words=pos_words,
        neg_words=neg_words,
        neu_words=neu_words
    )


def calc_words_prob(category_words: list[tuple[str, float]]):
    temp_calc: float = 1
    if not category_words: # if empty
        return 0
    else:
        for _, prob_value in category_words:
            temp_calc *= prob_value
        return temp_calc