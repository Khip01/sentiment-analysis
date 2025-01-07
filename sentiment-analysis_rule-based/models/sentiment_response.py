
class SentimentResponse:
    def __init__(self, text: str, sentiment: str, p_point: int, n_point: int):
        self.text: str = text
        self.sentiment: str = sentiment
        self.p_point: int = p_point
        self.n_point: int = n_point

    @property
    def p_point(self):
        return self._p_point

    @p_point.setter
    def p_point(self, value: int):
        self._p_point = value

    @property
    def n_point(self):
        return self._n_point

    @n_point.setter
    def n_point(self, value: int):
        self._n_point = value