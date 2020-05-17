'''URLs for ttweets_app'''

from django.urls import path, include

from . import views

app_name = 'ttweets_app'
urlpatterns = [
    # Home page
    path('', views.home, name = 'home'),

    # page to request login credentials
    path('tokens/', views.tokens, name = 'tokens'),

    # page to show the tweet plots
    path('timeline/', views.timeline, name = 'timeline'),

    # page to search tweets by hashtag
    path('hashtag/', views.hashtag, name = 'hashtag'),

    # page to search tweets by someone
    path('someone/', views.someone, name = 'someone')

]