
from models.data import Data
from models.naive_bayes import NaiveBayes, WordProbability
from models.preprocessed_data import PreprocessedData
from utils.calc_data_probablity import calc_prob
from utils.preprocessing_data import sentence_preprocessing


# Jadi pada naive bayes akan dilakukan beberapa stage
# 1. Melakukan Preprocessing pada data training, 
#    sehingga data training menjadi lebih mudah diolah
# 2. Membuat models peluang munculnya sentimen negatif, positif, ataupun netral
#    Ex: P(negatif), P(positif), P(netral)
# 3. Membuat models peluang pada setiap kata(yg sudah di filter di preprocessing) 
#    yang ada pada sentimen negatif, positif, ataupun netral
#    Ex: P(kata|negatif), P(kata|positif), P(kata|netral)
# 4. Mengembalikan models yang telah dibuat dari data training
def use_naive_bayes(datas: list[Data]) -> NaiveBayes:
    # melakukan preprocessing data pada tiap tiap data training
    preprocessed_datas: list[PreprocessedData] = [sentence_preprocessing(data=data) for data in datas]

    # menghitung probabilitas sentence negatif, positif dan netral
    positive_prob: float = len([data for data in preprocessed_datas if data.label == "positif"])
    negative_prob: float = len([data for data in preprocessed_datas if data.label == "negatif"])
    neutral_prob: float = len([data for data in preprocessed_datas if data.label == "netral"])

    # menghitung probabilitas masing - masing kata dalam seluruh data
    # Ex: P(kata|negatif), P(kata|positif), P(kata|netral)
    words_prob: list[WordProbability] = calc_prob(preprocessed_datas)

    # memasukkan/menyimpan models yang telah dibuat
    naive_bayes_model: NaiveBayes = NaiveBayes(
        positive_prob=positive_prob,
        negative_prob=negative_prob,
        neutral_prob=neutral_prob,
        list_word_prob=words_prob
    )

    # mengembalikan model yang telah dibuat dari data training
    return naive_bayes_model