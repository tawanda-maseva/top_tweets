from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . models import App_Credentials, Access_Tokens
from . import get_tweets as gt
from . forms import TokensForm, HashtagForm, SomeoneForm

# Create your views here.

def home(request):
	'''Load the home page'''
	return render(request, 'ttweets_app/home.html')

def tokens(request):
	'''Get the user's API tokens'''
	if request.method != 'POST':
		form = TokensForm()
	else:
		form = TokensForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False) # format to database headers
			form.owner = request.user
			form.save()
			return redirect('/') # to home

	context = {'form': form}
	return render(request, 'ttweets_app/tokens_form.html', context)

def timeline(request):
	'''Get tweets from user's timeline'''
	if request.user.is_authenticated:
		account = User.objects.get(username = request.user)
		tokens = Access_Tokens.objects.get(owner_id = account.id)
		api = gt.private_auth(
							  key = tokens.api_key,
							  secret_key = tokens.api_secret_key,
							  access_token = tokens.access_token,
							  access_token_secret = tokens.access_token_secret
							  )
	else:
		if request.method != 'POST':
			# Give form for access tokens
			form = TokensForm()
			context = {'form': form}
			return render(request, 'ttweets_app/tokens_form.html', context)
		else:
			form = TokensForm(request.POST)
			if form.is_valid():
				try:	
					api = gt.private_auth(
								key = form.cleaned_data['api_key'],
								secret_key = form.cleaned_data['api_secret_key'],
								access_token = form.cleaned_data['access_token'],
								access_token_secret = form.cleaned_data['access_token_secret'],
								)
				except Exception:
					return redirect('/')
				else:
					pass

	new_tweets, likes, retweets = gt.timeline(api, limit = 30)
	# plot data
	likes_plot = gt.plot_by('likes', new_tweets, likes)
	likes_plot.title = 'Tweets from User' + '\'s Timeline by Likes'
	retweets_plot = gt.plot_by('retweets', new_tweets, retweets)
	retweets_plot.title = 'Tweets from User' + '\'s Timeline by Retweets'
	# render
	likes_plot = likes_plot.render_data_uri()
	retweets_plot = retweets_plot.render_data_uri()

	context = {'likes_plot': likes_plot, 'retweets_plot': retweets_plot}
	return render(request, 'ttweets_app/timeline.html', context)


def hashtag(request): # This is still buggy
	'''Plot tweets by hashtag'''
	if request.method != 'POST':
		# Create an input form
		form = HashtagForm()
		context = {'form': form}
		return render(request, 'ttweets_app/hashtag_form.html', context)
	else:
		form = HashtagForm(request.POST)
		if form.is_valid():
			hashtag = form.cleaned_data['hashtag']
			# get data
			app_cred = App_Credentials.objects.get(id=1) # modify to admin owner
			api = gt.public_auth(app_cred)
			new_tweets, likes, retweets = gt.hashtag(api, hashtag, limit = 30)
			# plot data
			likes_plot = gt.plot_by('likes', new_tweets, likes)
			likes_plot.title = hashtag + ' tweets by Likes'
			retweets_plot = gt.plot_by('retweets', new_tweets, retweets)
			retweets_plot.title = hashtag + ' tweets by Retweets'
			# render
			likes_plot = likes_plot.render_data_uri()
			retweets_plot = retweets_plot.render_data_uri()

			context = {'likes_plot': likes_plot, 'retweets_plot': retweets_plot}
			return render(request, 'ttweets_app/hashtag.html', context)

def someone(request):
	'''Plot tweets by someone'''
	if request.method != 'POST':
		# Create an input form
		form = SomeoneForm()
		context = {'form': form}
		return render(request, 'ttweets_app/someone_form.html', context)
	else:
		form = SomeoneForm(request.POST)
		if form.is_valid():
			handle = form.cleaned_data['handle']
			# get data
			app_cred = App_Credentials.objects.get(id=1) # modify to admin owner
			api = gt.public_auth(app_cred)
			new_tweets, likes, retweets = gt.account(api, handle, limit = 30)
			# plot data
			likes_plot = gt.plot_by('likes', new_tweets, likes)
			likes_plot.title = handle + ' tweets by Likes'
			retweets_plot = gt.plot_by('retweets', new_tweets, retweets)
			retweets_plot.title = handle + ' tweets by Retweets'
			# render
			likes_plot = likes_plot.render_data_uri()
			retweets_plot = retweets_plot.render_data_uri()

			context = {'likes_plot': likes_plot, 'retweets_plot': retweets_plot}
			return render(request, 'ttweets_app/someone.html', context)















