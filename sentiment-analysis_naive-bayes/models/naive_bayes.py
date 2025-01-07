class WordProbability:
    def __init__(self, word: str, label: str, probability: float):
        self.word = word
        self.label = label
        self.probability = probability

class NaiveBayes:
    def __init__(
            self,
            positive_prob: float,
            negative_prob: float, 
            neutral_prob: float, 
            list_word_prob: list[WordProbability]):
        self.positive_prob = positive_prob
        self.negative_prob = negative_prob
        self.neutral_prob = neutral_prob
        self.list_word_prob = list_word_prob
        