# import packages
import pip
import tweepy
import time




# Authenticate to twitter
consumer_key='ix8Mywxx2Bu78uhoShXgHaPS4'
consumer_secret='Ev9RmCYb5TsREIgggsId5rBok9LvTZ0v3DawG2NrapLqEH5sq3'
access_key='1416025590830927879-KOKA64KZIug6Ipg2p9azwYWdEbZosA'
access_secret='Qe5cn9H7RZMmAiVOym0CpeZ5algBhkdMY883qggaqlP4B'

# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit_ =True, wait_on_rate_limit_notify=True)

user = api.me()
search= 'womenintech'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search,search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
