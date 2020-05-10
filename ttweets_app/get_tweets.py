'''Functions for extraction and processing of tweets'''
import pygal
from pygal.style import Style

import tweepy as tw

def authenticate(credentials):
	'''Function to get credentials'''
	# extract credentials
	key = credentials.api_key
	secret_key = credentials.api_secret_key
	token = credentials.access_token
	token_secret = credentials.access_token_secret

	# login
	auth = tw.OAuthHandler(key, secret_key)
	auth.set_access_token(token, token_secret)
	api = tw.API(auth)

	return api

def timeline(api, limit):
	'''Get tweets from user's timeline'''
	raw_timeline = api.home_timeline(count = limit)
	new_tweets, likes, retweets = extract_tweets(raw_timeline)
	return new_tweets, likes, retweets

def extract_tweets(raw_tweets):
	'''Extract tweets data'''
	new_tweets, likes, retweets = [],[],[]
	for data in raw_tweets:
		# extract tweet content
		tweet_data = data._json
		tweet_url = 'https://twitter.com/i/web/status/' + str(tweet_data['id_str'])

		likes_dict = {'value':tweet_data['favorite_count'], 'xlink': tweet_url, 'label':tweet_data['text']}
		retweets_dict = {'value':tweet_data['retweet_count'], 'xlink': tweet_url, 'label':tweet_data['text'] }

		# save to lists
		new_tweets.insert(0, tweet_data['created_at']) #tweet time
		likes.insert(0, likes_dict)
		retweets.insert(0, retweets_dict)

	return new_tweets, likes, retweets 

def plot_by(category, time_posted, likes_retweets):
	'''Pupulate plot by likes or retweets with default colour greeen'''
	config = bar_config()
	styling = bar_style()
	bchart = pygal.Bar(config, style = styling)

	bchart.x_labels = time_posted
	bchart.add(category.title(), likes_retweets)
	bchart.title = 'Tweets from User' + '\'s Timeline by ' + category.title()
	return bchart

def bar_config():
	'''Display settings of bar graph'''
	chart_config = pygal.Config()
	chart_config.x_label_rotation = 45
	chart_config.truncate_label = 17
	chart_config.width = 1000
	chart_config.x_title = 'Time tweeted'
	return chart_config

def bar_style():
	'''Style settings'''
	custom_style = Style(legend_font_size = 12,
						label_font_size = 12,
						title_font_size = 15,
						value_font_size = 12,
						value_label_font_size = 12,
						plot_background = 'grey',
						major_label_font_size = 12,
						tooltip_font_size = 8
						)
	return custom_style