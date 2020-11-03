#!/usr/bin/env python
# encoding: utf-8
# Author - Lin Cheng


import tweepy  # https://github.com/tweepy/tweepy
import json
from twitter_api_credentials import *



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


'''  Test function about sending a new tweet on Twitter  '''


def send_tweet_test(tweet):

    api = authorize_and_initialize()

    # Post a tweet from Python
    api.update_status(tweet)


''' Test function about searching Twitter for recent tweets'''


def search_tweet_test():

    api = authorize_and_initialize()

    # Define the search term
    search_words = "#Covid"

    # Define the date_since date
    date_since = "2020-9-25"

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(5)
    tweet_list = []
    # Iterate and append tweets into a list
    for tweet in tweets:
        tweet_list.append(tweet.text)

    # print all tweets in list
    print(tweet_list)


if __name__ == '__main__':

    print("Test Start Here")

    # tweet = "hello from Boston"
    # send_tweet_test(tweet)

    # search tweet test
    # search_tweet_test()


