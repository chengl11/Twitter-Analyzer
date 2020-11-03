# Twitter-GoogleNLP_API_Test

## Description
This phase 01 is to write test programs to exercise different twitter APIs and Google BLP APIs.


## By using twitter_api_test.py file, you'll have to have four Twitter API credentials
1. consumer_key
2. consumer_secret
3. access_key
4. access_secret

### This project contains three important functions.

### authorize_and_initialize()

This is the function to authorize twitter and initialize tweepy. I've separated it to make it easier to call and to avoid repeating calls in each subsequent function。

### send_tweet_test(tweet)

This is the function about sending a new tweet on Twitter. The utility of this function is to post a tweet from Python. Its input is the content that you want to post on Twitter. After calling this function, you could see your tweet on Twitter.

### search_tweet_test()

This is the function about searching Twitter for recent tweets. You could search Twitter for recent tweets by calling this function. Start by finding recent tweets that use the #keyword hashtag (e.g. #Covid). You will use the .Cursor method to get an object containing tweets containing the hashtag #keyword. There is a .Cursor() to search twitter for tweets containing the search term #keyword. You can restrict the number of tweets returned by specifying a number in the .items() method. .items(5) will return 5 of the most recent tweets. It returns an object that you can iterate or loop over to access the data collected. There is a list to collect all items.


# google_api_test.py


### This is only a test file that following the Google Sentiment Analysis Tutorial on "https://cloud.google.com/natural-language/docs/sentiment-tutorial"

1.Imports the libraries necessary to run the application
2.Takes a text file and passes it to the main() function
3.Reads the text file and makes a request to the service
4.Parses the response from the service and displays it to the user


## This tutorial has several prerequisites:

1. You've set up a Cloud Natural Language API project in the Google Cloud Console.
2. You've set up your environment using Application Default Credentials.
3. You have basic familiarity with Python programming.
4. You have set up your Python development environment. It is recommended that you have the latest version of Python, pip, and virtualenv installed on your system. For instructions, see the Python Development Environment Setup Guide for Google Cloud Platform.
5. You've installed the Google Cloud Client Library for Python


## print_result(annotations)

This function walks through the response to extract the sentiment score values for each sentence, and the overall score and magnitude values for the entire review, and display those to the user.


## analyze(movie_review_filename)

This code snippet performs the following tasks:

* Instantiates a LanguageServiceClient instance as the client.
* Reads the filename containing the text data into a variable.
* Instantiates a Document object with the contents of the file.
* Calls the client's analyze_sentiment method.

## Test And Result

### Below is the test case and result.

#### Run "python google_api_test.py bladerunner-pos.txt" in command line

### Result

Sentence 0 has a sentiment score of 0.699999988079071
Sentence 1 has a sentiment score of 0.20000000298023224
Sentence 2 has a sentiment score of 0.699999988079071
Sentence 3 has a sentiment score of -0.10000000149011612
Sentence 4 has a sentiment score of 0.0
Sentence 5 has a sentiment score of -0.6000000238418579
Sentence 6 has a sentiment score of -0.10000000149011612
Sentence 7 has a sentiment score of 0.5
Sentence 8 has a sentiment score of 0.4000000059604645
Sentence 9 has a sentiment score of 0.8999999761581421
Overall Sentiment: score of 0.20000000298023224 with magnitude of 4.599999904632568




