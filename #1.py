# -*- coding: utf-8 -*-

#Installing dependencies
import tweepy
from textblob import TextBlob

#Accessing and extracting tweets from Twitter API
consumer_key = "xCGcOHVXQgIOP6YQ7nMbYvJK5"
consumer_secret = "u3LTUigU2xQOTHZAfbQhLAjSiJfrRMEqrpK2apU9drQwpixAuP"

access_token =  "940672481324683264-SVrfrabu9SYVB6XytTGUQg0ceMe1Bb7"
access_token_secret = "KSmdeKxKcZhLcGbYHUNGmdia3kKCuq2Wk4j5JIPgLm92i"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#Enter the TARGET for tweets(edit your target in the below line)
public_tweets = api.search("Putin")
#creating emoty lists for classes 
Pos = []
Nue = []
Neg = []
#pull tweets and convert them to textblob format and classify them as POSITIVE, NUETRAL or NEGATIVE based on sentiment polarity value
for tweet in public_tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    if(analysis.sentiment.polarity > 0):
        Pos.append(analysis)
    elif(analysis.sentiment.polarity == 0):
        Nue.append(analysis)
    else:
        Neg.append(analysis)
        
#printing the tweets under each class         
print("Positive tweets are:",Pos)
print("Nuetral tweets are:",Nue)
print("Negative tweets are:",Neg)
