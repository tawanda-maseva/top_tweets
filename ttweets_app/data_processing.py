import pygal
from pygal.style import Style #, DarkStyle
import json

import tweepy as tw

def welcome_msg():
	'''Pring welcome message and lead user'''
	print('\nHi there!\n\nWhat would you like to do? (1,2, or 3?)')
	print('1. See tweets from your timeline')
	print('2. See tweets by someone')
	print('3. Search tweets by a hashtag')
	print('Press q to quit\n')

def verify_user_input():
	'''Check user input'''
	user_input = input().lower()
	expected_response = ['1','2','3','q']
	while user_input not in expected_response:
		user_input = input('Please choose 1,2,3 or q to quit. \n').lower()
	return user_input

def api_login(credentials_file):
	'''Retrieve user credentials saved on json file and login'''

	# Retrieve details
	with open(credentials_file, 'r') as filename:
		file = json.load(filename)
		api_key = file['api_key']
		api_secret_key = file['api_secret_ket']
		access_token = file['access_token']
		access_token_secret = file['access_token_secret']

	#Log into user's twitter account and api account
	auth = tw.OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	api = tw.API(auth)

	return api

def bar_config():
	'''Display settings of bar graph'''
	chart_config = pygal.Config()
#	chart_config.style = DarkStyle
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

	
