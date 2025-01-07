# Sentiment Analysis 
Contains 2 simple projects which have the same goal, which is to analyze sentiment, whether the sentiment is positive, negative or neutral. **The sentiment analyzed is Indonesian sentiment.** 

## Rule Based
Rule-based sentiment analysis here is a sentiment analysis method using predefined logic rules. The rules are determined according to the **list of keywords** that have been given in the `words.txt` file whether they are negative or positive words **without using data training**. 

## Naive Bayes
Sentiment analysis Naive Bayes here is a technique for analyzing sentiment using the Naive Bayes machine learning method. This method **uses data training to learn the probability of each word appearing in a positive, negative or neutral**. 
Which later from the results of the Naive Bayes model will **produce a probability that can later identify a word** including positive or negative or neutral words.

# Instruction 
To run either of the projects, we have the same steps:
- go to one of the naive_bayes or rule_based projects with `cd "folder_project_name"`
- create a virtual environment from python first using `python -m venv .venv`
- activate the virtual environment according to your Operating System
- install all the requirement libraries needed by running `pip install requirements.txt`
- run the main.py file with `python -m main`
