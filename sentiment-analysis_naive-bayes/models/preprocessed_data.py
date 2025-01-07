class PreprocessedData:
    def __init__(self, sentence: str, label: str, preprocessed_sentence: list[str]):
        self.sentence = sentence
        self.label = label
        self.preprocessed_sentence = preprocessed_sentence