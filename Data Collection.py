
# API keys
api_key="********************************"
api_secret="********************************"
access_token="********************************"
access_token_secret="********************************"

#imprt library
import tweepy
import pandas as pd

#Authenticat to Twitter
auth=tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#number of tweets retrieving
tweetsNo=200
tweets=[]
time=[]
for i in tweepy.Cursor(api.search_tweets, q="  ",tweet_mode='extends').items(tweetsNo):
    tweets.append(i.text)
    
#create DataFrame
df=pd.DataFrame({'Tweets':tweets})
print(df)

# Export to excel
df.to_excel('fileName.xlsx')

