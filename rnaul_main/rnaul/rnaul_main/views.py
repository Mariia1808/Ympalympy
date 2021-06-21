from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
import csv
from vk_api import VkApi
from bs4 import BeautifulSoup
import math
from random import *
import sys, os, re, csv, codecs,  pandas as pd
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import pickle
import zipfile
from random import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def frontend(request): 
  return HttpResponse(render(request, 'vue_index.html'))

class PreProcessSome:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + list('``'))

    def processText(self, list_of_docs):
        processedDocs = []
        for doc in list_of_docs:
            processedDocs.append([doc[0], self.processDoc(doc[1]), doc[2], doc[3], doc[4], doc[5], doc[6], doc[7]])
        return processedDocs

    def processDoc(self, doc):
        doc = doc.lower()  # convert text to lower-case
        doc = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', doc)  # remove URLs
        doc = re.sub('@[^\s]+', 'AT_USER', doc)  # remove usernames
        doc = re.sub(r'#([^\s]+)', r'\1', doc)  # remove the # in #hashtag
        doc = word_tokenize(doc)  # remove repeated characters (helloooooooo into hello)
        return [word for word in doc if word not in self._stopwords]


def buildVocabulary(preprocessedTrainingData):
    all_words = []

    for docs in preprocessedTrainingData:
        all_words.extend(docs[1])
    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()
    return word_features


def extract_features(message, wf):
    message_words = set(message)
    features = {}
    for word in wf:
        features['contains(%s)' % word] = (word in message_words)
    return features

def pretrainNB():
    path = 'input/'
    train_data_file = f'{path}train.csv'
    trainx = pd.read_csv(train_data_file)
    train = trainx.values[:3000]
    ppr = PreProcessSome()
    ppr = ppr.processText(train)
    wf = buildVocabulary(ppr)
    tutu = []
    for i in ppr:
        tutu.append((extract_features(i[1], wf), "toxic" if i[2] == 1 else "untoxic"))
    random.shuffle(tutu)
    train_x = tutu[:2700]
    model = nltk.NaiveBayesClassifier.train(train_x)
    test_x = tutu[2700:]
    model.show_most_informative_features(20)
    acc = nltk.classify.accuracy(model, test_x)
    path = "output/"
    f = open(f'{path}my_classifier.pickle', 'wb')
    pickle.dump(model, f)
    f.close()
    print("Accuracy:", acc)

def classify(array_of_texts):
    return rate(array_of_texts)

def classify_with_modelling_NB(message):
    path = 'input/'
    train_data_file = f'{path}train.csv'
    trainx = pd.read_csv(train_data_file)
    train = trainx.values[:3000]
    ppr = PreProcessSome()
    ppr_vocab = ppr.processText(train)
    ppr_message = ppr.processDoc(message)
    wf = buildVocabulary(ppr_vocab)
    path = "output/"
    f = open(f'{path}my_classifier.pickle', 'rb')
    model = pickle.load(f)
    f.close()
    model.show_most_informative_features(20)
    t_features = extract_features(ppr_message, wf)
    r_prob = 0.0
    for i in range(5):
        r_prob += model.prob_classify(t_features).prob("toxic")
    r_prob /= 5
    return str("MESSAGE\r\n"+message + " : " +"\n\rNB classification RESULT is\n\r "
                       + str(r_prob) + " Toxic\n\r ")
def auth_handler():
    """Обработчик двухфакторной аутентификации (если включена)
    """
    key = input('Enter authentication code: ')
    return key, True

def stripper(array):
    # Обработчик полученного из vk массива строк, делаем его красивым
    return list(filter(bool, array))

def toxify(vk_link):
    vk_session = VkApi('+79829152150', 'з0ыеа0кз0ые')
    vk_session.auth()
    vk = vk_session.get_api()

    post = vk.wall.get(offset = 1, count = 100, filter = 'owner')['items']
    posts_strings = [post['text'] for post in post]
    out_of_strings = stripper(posts_strings)
    toxicity_level = classify(out_of_strings)
    return toxicity_level

def rate(array_of_texts):
    return randint(40, 90)/100

def toxicity_rate(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        toxicity_rating = toxify(data["vk_link"])
        print(toxicity_rating)
        responseData = {
            "score" : toxicity_rating
        }
        return JsonResponse(responseData, status=status.HTTP_200_OK)

