#!/usr/bin/env python
# encoding: utf-8
# Author - Lin Cheng

# Twitter-API-Import-Files

import tweepy  # https://github.com/tweepy/tweepy
import json
from twitter_api_credentials import *

# Google-API-Import-Files
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/Lin/Desktop/BU_Courses/EC601/my_google_key.json"


# Twitter API credentials

consumer_key = my_consumer_key
consumer_secret = my_consumer_secret
access_key = my_access_key
access_secret = my_access_secret


''' Authorize twitter and initialize tweepy '''


def authorize_and_initialize():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


'''
This function is about searching Twitter for recent tweets. It returns a list of tweets.
There are three inputs:
    1. search_words: The keyword that you want to search. It will in each tweet's content after searching.
    2. date_since: What date do you want to start searching?
    3. The maximum number of tweets you want to search.
'''


def search_tweet(search_words, date_since, max_number):

    api = authorize_and_initialize()

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(max_number)
    tweet_list = []
    # Iterate and append tweets into a list
    for tweet in tweets:
        tweet_list.append(tweet.text)

    # print all tweets in list
    return tweet_list


'''
This function walks through the response to extract the sentiment score 
values for each sentence, and the overall score and magnitude values 
for the entire review, and display those to the user.
There are two inputs:
    1. content: Content of the current tweet
    2. annotations: The data processed by the analyzer
'''

def print_result(content, annotations):

    print("Content of current tweet:", "\n")
    print(content, "\n")


    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        print('The {} sentence: {}'.format(
            index+1, sentence.text.content))
        sentence_sentiment = sentence.sentiment.score
        print('This sentence has a sentiment score of {}'.format(
            sentence_sentiment))
        print()

    print('Overall Sentiment of This Tweet: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

'''
This function is about making the analyze.
There is one input:
    1. tweets_list: A list of all tweets
'''

def analyze(tweets_list):

    print()
    print("#######################")
    print()

    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    for tweet in tweets_list:
        content = tweet

        # Instantiates a Document object with the contents of the file.
        document = types.Document(
            content=content,
            type=enums.Document.Type.PLAIN_TEXT)

        # Calls the client's analyze_sentiment method.
        annotations = client.analyze_sentiment(document=document)
        # Print the results
        print_result(content, annotations)
        print()
        print("#######################")
        print()


if __name__ == '__main__':

    print("Social Media Analyzer")

    # Define the search term
    search_words = "#COVID"

    # Define the date_since date
    date_since = "2020-9-25"

    # Define the date_since date
    max_number = 1

    # get all tweets into a list
    tweets_list = search_tweet(search_words, date_since, max_number)

    # analyze all tweets
    analyze(tweets_list)
