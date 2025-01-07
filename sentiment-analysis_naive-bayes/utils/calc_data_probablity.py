from models.naive_bayes import WordProbability
from models.preprocessed_data import PreprocessedData

# calculate the probability of positive, negative, and neutral sentence
def calc_prob(datas: list[PreprocessedData]) -> list[WordProbability]:

    # menggabungkan seluruh kata dari seluruh data -> membuatnya unik + mengurutkannya sesuai abjad
    whole_words: list[str] = list(dict.fromkeys( # membuatnya unik
        [word for data in datas for word in data.preprocessed_sentence] # menggabungkan seluruh kata
    ))

    # menghitung total kata dalam setiap kategori
    total_pos_words = sum(1 for data in datas if data.label == "positif")
    total_neg_words = sum(1 for data in datas if data.label == "negatif")
    total_neu_words = sum(1 for data in datas if data.label == "netral")

    # menentukan jumlah kata unik
    vocab_size = len(whole_words)

    # menghitung probabilitas tiap kata dan menghitung probabilitas munculnya dengan syarat positif, negatif dan netral
    words_prob_result: list[WordProbability] = []
    for word in whole_words:
        temp_word_pos: int = 0
        temp_word_neg: int = 0
        temp_word_neu: int = 0

        # menghitung frekuensi kata tiap kategori
        for data in datas:
            if word in data.sentence:
                if data.label == "positif": temp_word_pos += 1
                elif data.label == "negatif": temp_word_neg += 1
                elif data.label == "netral": temp_word_neu += 1

        # calculate probability
        """
            *dengan menggunakan laplace smoothing untuk menghindari zero probability
            P(w|C) = Count(w, C) + 1 / Total kata di C + V
            Di mana:
            - Count(w, C) adalah jumlah kemunculan kata w dalam kategori C
            - V adalah jumlah kata unik (vocabulary size) di seluruh dataset.
            - Total kata di C adalah jumlah total kaya di kategori C
        """
        pos_word_prob = (temp_word_pos + 1) / (total_pos_words + vocab_size)
        neg_word_prob = (temp_word_neg + 1) / (total_neg_words + vocab_size)
        neu_word_prob = (temp_word_neu + 1) / (total_neu_words + vocab_size)

        # store the probability of the word
        words_prob_result.append(WordProbability(word=word, label="positif", probability=pos_word_prob))
        words_prob_result.append(WordProbability(word=word, label="negatif", probability=neg_word_prob))
        words_prob_result.append(WordProbability(word=word, label="netral", probability=neu_word_prob))


    # mengembalikan hasil list masing-masing probabilitas kata
    return words_prob_result


