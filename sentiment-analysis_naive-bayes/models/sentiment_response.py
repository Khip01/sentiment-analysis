class SentimentResponse:
    def __init__(
            self,
            sentence: str,
            predicted_label: str,
            pos_words: list[tuple[str, float]],
            neg_words: list[tuple[str, float]],
            neu_words: list[tuple[str, float]]
    ):
        self.sentence = sentence
        self.predicted_label = predicted_label
        self.pos_words = pos_words
        self.neg_words = neg_words
        self.neu_words = neu_words
