# load data json from data.json
from apply_model.apply_model import apply_model
from models.data import Data
from models.naive_bayes import NaiveBayes
from models.sentiment_response import SentimentResponse
from naive_bayes_classifier.naive_bayes import use_naive_bayes
from utils.load_json_data import load_data_from_json

# load the data
datas: list[Data] = load_data_from_json("./data/data_training.json")

# make the models from the data using naive bayes
naive_bayes_model: NaiveBayes = use_naive_bayes(datas=datas)

# load data test
test_datas: list[Data] = load_data_from_json("./data/data_testing.json")

# calculate data test using naive bayes model
list_sentiment_response: list[SentimentResponse] = apply_model(source=test_datas, model=naive_bayes_model)

for sentiment_response in list_sentiment_response:
    print(sentiment_response.sentence)
    print(sentiment_response.predicted_label)
