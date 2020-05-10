import json
import pygal
from pygal.style import Style, DarkStyle

from . import data_processing

class User():
	'''Retrieve timeline tweets'''
	def __init__(self, credentials_file):
		'''Initialize parameters'''
		self.credentials_file = credentials_file
		self.new_tweets, self.likes, self.retweets = [],[],[]
		self.existing_data = {}
		self.history_limit = 30 # default history retrieved
		self.bchart = '' # hold likes or RTs plot data

		self.api = data_processing.api_login(self.credentials_file) # login and auth from json

	def update_history(self, filename):
		'''Load tweets to be plotted'''
		try:
			open(filename, 'r') # check if user exists
		except FileNotFoundError:
			# save user's first tweets to user file
			self.save_first_tweets(filename)
		else:
			self.save_history(filename)

	def extract_tweets(self, raw_tweets):
		'''Extract tweets data'''
		for data in raw_tweets:
			# extract tweet content
			tweet_data = data._json
			tweet_url = 'https://twitter.com/i/web/status/' + str(tweet_data['id_str'])

			likes_dict = {'value':tweet_data['favorite_count'], 'xlink': tweet_url, 'label':tweet_data['text']}
			retweets_dict = {'value':tweet_data['retweet_count'], 'xlink': tweet_url, 'label':tweet_data['text'] }

			# save to lists
			self.new_tweets.insert(0, tweet_data['created_at']) #tweet time
			self.likes.insert(0, likes_dict)
			self.retweets.insert(0, retweets_dict)


	def visualize_by(self, category):
		'''Pupulate plot by likes or retweets with default colour greeen'''
		config = data_processing.bar_config()
		styling = data_processing.bar_style()
		self.bchart = pygal.Bar(config, style = styling)

		self.bchart.x_labels = self.new_tweets[ :self.history_limit]
		if category == 'likes':
			self.bchart.add('Likes', self.likes[ :self.history_limit])
		elif category == 'retweets':
			self.bchart.add('Retweets', self.retweets[ :self.history_limit])

	def save_first_tweets(self, filename):
		'''Save user's first tweets'''
		self.existing_data['tweets'] = self.new_tweets
		self.existing_data['likes'] = self.likes
		self.existing_data['retweets'] = self.retweets

		with open(filename, 'w') as file:
			json.dump(self.existing_data, file, indent = 4)

	def save_history(self, filename):
		'''Get existing user's historical tweets data'''
		with open(filename, 'r') as file:
			self.existing_data = json.load(file) # get existing data

		# update likes and RTs of duplicate entries
		existing_tweets = self.existing_data['tweets'][: self.history_limit] # first 20 only
		for i in range(len(self.new_tweets)):
			if self.new_tweets[i] in existing_tweets:
				# update stats only: num of likes and tweets first
				target_update = self.existing_data['tweets'].index(self.new_tweets[i])
				self.existing_data['likes'][target_update]['value'] = self.likes[i]['value']
				self.existing_data['retweets'][target_update]['value'] = self.retweets[i]['value']
			else:
				# add the new tweets to existing tweets
				self.existing_data['tweets'].insert(0, self.new_tweets[i]) # update tweets
				self.existing_data['likes'].insert(0, self.likes[i]) # update likes
				self.existing_data['retweets'].insert(0, self.retweets[i]) # update likes

		# write back to json file
		with open(filename, 'w') as file:
			json.dump(self.existing_data, file, indent = 4)
