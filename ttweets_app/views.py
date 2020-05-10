from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import API_Credentials
from . import tw_visualizations as twv
from . import get_tweets as gt
from . forms import API_loginForm

# Create your views here.

def home(request):
	'''Load the home page'''
	return render(request, 'ttweets_app/home.html')

def credentials(request):
	'''Get the user's API credentials'''
	form = API_loginForm()
	context = {'form': form}
	return render(request, 'ttweets_app/credentials.html', context)
	# if this is a POST request we need to process the form data
	#if request.method == 'POST':
		# create a form instance and populate it with data from the request:
	#	form = Credentials(request.POST)
		# check whether it's valid:
	#	if form.is_valid():
			# log into the tweeter API and extract the data
	#		return HttpResponseRedirect('')
    # if a GET (or any other method) we'll create a blank form
	#else:
	#	form = Credentials()
	#	context = {'form': form}

	#return render(request, 'ttweets_app/timeline.html', context)

def timeline(request):
	'''Get tweets from my timeline'''
	#if request.user.is_authenticated:
	#	return HttpResponseRedirect(reverse('ttweets_app:credentials'))

	#if logged in:
	user_cred = API_Credentials.objects.get(id=7) # foreign key with user needed
	api = gt.authenticate(user_cred)
	new_tweets, likes, retweets = gt.timeline(api, limit = 30)
	likes_plot = gt.plot_by('likes', new_tweets, likes)
	retweets_plot = gt.plot_by('retweets', new_tweets, retweets) 

	# render
	likes_plot = likes_plot.render_data_uri()
	retweets_plot = retweets_plot.render_data_uri()

	context = {'likes_plot': likes_plot, 'retweets_plot': retweets_plot}
	return render(request, 'ttweets_app/timeline.html', context)












