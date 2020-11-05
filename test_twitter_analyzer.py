import twitter_analyzer as analyzer

def test_wrongkey():
    
    # Define the search term
    search_words = "#COVID"
    # Define the date_since date
    date_since = "2020-9-25"
    # Define the date_since date
    max_number = 5

    # # get all tweets into a list
    # tweets_list = search_tweet(search_words, date_since, max_number)

    assert len(analyzer.search_tweet(search_words, date_since, max_number)) == 5

    max_number = 3
    
    assert len(analyzer.search_tweet(search_words, date_since, max_number)) == 3

    # # analyze all tweets
    # analyze(tweets_list)

test_wrongkey()

