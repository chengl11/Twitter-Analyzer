# Twitter Sentiment Analyzer


### Product Mission

This product is aimed at people who want to know how people on Twitter feel about something, such as people's attitude and sentiment.

It is built based on the basic Twitter API application and Google Natural Language API application. It uses an analyzeSentiment request, which performs sentiment analysis on text. The sentiment analysis attempts to determine the overall attitude (positive or negative) and is represented by numerical score and magnitude values.

For more infomation, please visit 
1. https://cloud.google.com/natural-language/docs/sentiment-tutorial
2. https://developer.twitter.com/en/docs/tools-and-libraries


### Product Instruction
There are three inputs of this analyzer:
    1. search_words: The keyword that you want to search. It will appear in each tweet's content.
    2. date_since: What date do you want to start searching?
    3. The maximum number of tweets you want to search.


### Target User

1. For ordinary people who want to know what other people think about a news or product.

2. A product analyst at a company. They want to know what people think about their new product.


### User Stories

##### First User Story

To find out how people on Twitter felt about Coronavirus, Alice typed in the keyword ("#COVID"), start searching date ("2020-10-01") and number of tweets(1). Then, the Analyzer shows the following information:

#######################

Content of current tweet: 

RT @jaxtell123: @alizaslav EVERY Senator, #Democrat or #Republican SHOULD be required to have a negative #COVID test before returning to th… 

The 1 sentence: RT @jaxtell123: @alizaslav EVERY Senator, #Democrat or #Republican SHOULD be required to have a negative #COVID test before returning to th…
This sentence has a sentiment score of -0.699999988079071

Overall Sentiment of This Tweet: score of -0.699999988079071 with magnitude of 0.699999988079071

#######################

It first shows the content of current tweet. Secondly, it shows the content and sentiment score of each sentence of that tweet. Finally, it shows the overall sentiment of this tweet. Therefore, by looking at this result, Alice thinks that the mood towards Coronavirus is not optimistic.

##### Second User Story

Jack is a shoe company product analyst, he wants to know people’s attitude for their company's new shoes, he will use our analyzer.

