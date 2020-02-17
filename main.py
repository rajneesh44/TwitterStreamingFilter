import tweepy
import datetime
import json 

file_path = 'api.json'

with open(file_path) as f:
	twitter_api = json.loads(f.read())

consumer_key = twitter_api['consumer_key']
consumer_secret = twitter_api['consumer_secret']
access_token = twitter_api['access_token']
access_token_secret = twitter_api['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
	def on_status(self,status):

		if('RT @' not in status.text):
			tweet_item={
			'id_str':status.id_str,
			'text':status.text,
			'username':status.user.screen_name,
			'name':status.user.name,
			'profile_image_url':status.user.profile_image_url,
			'received_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			}
			print(tweet_item)

	def on_error(self,status_code):
		if status_code==420:
			return False

stream_Listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener = stream_Listener)
stream.filter(track=["@WarbyParker", "@Bonobos", "@Casper","@Glossier", "@DollarShaveClub", "@Allbirds","pizza"])

	

