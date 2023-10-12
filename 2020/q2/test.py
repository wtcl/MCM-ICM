import random
import re
import string
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag, pos_tag_sents
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import word_tokenize


def fenci(file):
    return twitter_samples.tokenized(file)


def cleaned_list_func(evert_tweet):
    new_text = []
    cixing_list = pos_tag(evert_tweet)
    for word, cixing in cixing_list:
        word = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:[0-9a-fA-F][0-9a-fA-F]))+', '', word)
        word = re.sub('(@[A-Za-z0-9_]+)', '', word)
        if cixing.startswith('NN'):
            pos = 'n'
        elif cixing.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        new_word = lemmatizer.lemmatize(word, pos)
        if len(new_word) > 0 and new_word not in string.punctuation and new_word.lower() not in stopwords.words(
                'english'):
            new_text.append(new_word.lower())
    return new_text


def get_all_words(clean_tokens_list):
    for tokens in clean_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(clean_tokens_list, tag):
    li = []
    for every_tweet in clean_tokens_list:
        data_dict = dict([token, True] for token in every_tweet)
        li.append((data_dict, tag))
    return li


def train_model(train_data, test_data):

    model = NaiveBayesClassifier.train(train_data)
    return model


def test(model, test_text):
    custom_tokens = cleaned_list_func(word_tokenize(test_text))
    result = dict([token, True] for token in custom_tokens)


if __name__ == '__main__':
    po_file_path = 'positive_tweets.json'
    ne_file_path = 'negative_tweets.json'

    positive_tweets = twitter_samples.strings(po_file_path)
    negative_tweets = twitter_samples.strings(ne_file_path)

    po_fenci_res = fenci(po_file_path)
    be_fenci_res = fenci(ne_file_path)
    positive_cleaned_list = []
    negative_cleaned_list = []
    for i in po_fenci_res:
        positive_cleaned = cleaned_list_func(i)
        positive_cleaned_list.append(positive_cleaned)
for j in be_fenci_res:
    negative_cleaned = cleaned_list_func(j)
    negative_cleaned_list.append(negative_cleaned)
po_for_model = get_tweets_for_model(positive_cleaned_list, 'Positive')
ne_for_model = get_tweets_for_model(negative_cleaned_list, 'Negative')

model_data = po_for_model + ne_for_model
random.shuffle(model_data)

train_data = model_data[:7000]
test_data = model_data[7000:]

model = train_model(train_data, test_data)
test_list = [
    "I was sad on the day you went away,I'm not the man your heart is missing,that's why you go away I know.",
    "My heart is being cut by the knife that is called MISSING YOU. NOthing in the world can destroy me except losing you. My memory of you devours every cell of my blood",
    "I will always be there for you.",
    'I fuck you fuck your mother fuck your father fuck your family',
    "Don't worry when you are not recognized, but strive to be worthy of recognition.",
    "The power of imagination makes us infinite.",
    "The glow of one warm thought is to me worth more than money."
]
for i in test_list:
    test(model, i)