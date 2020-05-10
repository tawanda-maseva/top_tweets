from . import timeline_tweets
from . import data_processing


class Timeline(timeline_tweets.User):
	'''Analyze tweets by Likes'''
	def __init__(self, username, credentials_file):
		'''Inherit data from parent class - User'''
		super().__init__(credentials_file)
		self.username = username
		self.history_file = 'output_files/' + self.username + '_timeline' + '.json'

		self.refresh_tweets() # get latest tweets

	def tweetsby(self, category):
		'''Plot default 20 tweets by likes or retweets with default colour green'''	
		self.visualize_by(category)
		self.bchart.title = 'Tweets from ' + self.username + '\'s Timeline by ' + category.title()
		#svg_filename = 'output_files/' + self.username + '_timeline_' + category + '.svg'
		#self.bchart.render_to_file(svg_filename)
		#self.bchart.render_in_browser()


	def refresh_tweets(self):
		'''Get the latest tweets and update historical search'''
		user_timeline = self.api.home_timeline(count = self.history_limit) # Get tweets from user's timeline
		self.extract_tweets(user_timeline)
		#self.update_history(self.history_file)

class Tweets_by(timeline_tweets.User):
	'''Visualize Tweets by any user'''
	def __init__(self, user_id, credentials_file):
		'''Inherit data from parent class - User'''
		super().__init__(credentials_file)
		self.user_id = user_id
		self.history_file = 'output_files/' + self.user_id + '_tweets' + '.json'

		self.refresh_tweets() # get latest tweets

	def refresh_tweets(self):
		'''Get the latest tweets and update historical search'''
		user_tweets = self.api.user_timeline(screen_name = self.user_id,
											count = self.history_limit) #Get tweets from user's timeline
		self.extract_tweets(user_tweets)
		self.update_history(self.history_file)

	def tweetsby(self, category):
		'''Plot default 20 tweets by likes or retweets with default colour green'''
		self.visualize_by(category)
		self.bchart.title = 'Tweets from @' + self.user_id + ' by ' + category.title()
		svg_filename = 'output_files/' + self.user_id + '_tweets_' + category + '.svg'
		self.bchart.render_to_file(svg_filename)

class Hashtag(timeline_tweets.User):
	'''Visualize Corona tweets'''
	def __init__(self, hashtag, credentials_file):
		super().__init__(credentials_file)
		self.hashtag = hashtag
		self.history_file = 'output_files/' + self.hashtag + '_tweets' + '.json'

		self.refresh_tweets()

	def tweetsby(self,category):
		'''Plot default 20 tweets by likes or retweets with default colour green'''
		self.visualize_by(category)
		self.bchart.title = self.hashtag + ' Tweets by ' + category.title()
		svg_filename = 'output_files/' + self.hashtag + '_tweets_' + category + '.svg'
		self.bchart.render_to_file(svg_filename)

	def refresh_tweets(self):
		'''Get the latest tweets and update historical search'''
		hashtag_tweets = self.api.search(q = self.hashtag, lang = 'en')
		self.extract_tweets(hashtag_tweets)
		self.update_history(self.history_file)

