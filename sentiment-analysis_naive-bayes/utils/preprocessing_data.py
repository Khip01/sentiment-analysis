import string

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

from models.data import Data
from models.preprocessed_data import PreprocessedData


# preprocessing step
# 1. menghapus tanda baca
# 2. membuat sentence ke lowercase
# 3. tokenisasi
# 4. menghapus stopword
# 5. stemming tiap kata
def sentence_preprocessing(data: Data) -> PreprocessedData:
    sentence = data.sentence

    # menghapus tanda baca
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    # mengubah sentence ke lowercase
    sentence = sentence.lower()

    # tokenisasi sentence
    words = sentence.split()

    # menghapus stopwords
    stopword_factory = StopWordRemoverFactory()
    stopwords = set(stopword_factory.get_stop_words())
    # # Exclude kata 'tidak' dari stopwords
    # stopwords.discard('tidak')
    filtered_words = [word for word in words if word not in stopwords]

    # melakukan stemming tiap kata
    stemming_factory = StemmerFactory()
    stemmer = stemming_factory.create_stemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    return PreprocessedData(sentence=data.sentence, label=data.label, preprocessed_sentence=stemmed_words)