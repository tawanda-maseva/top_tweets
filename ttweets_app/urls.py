'''URLs for ttweets_app'''

from django.urls import path, include

from . import views

app_name = 'ttweets_app'
urlpatterns = [
    # Home page
    path('', views.home, name = 'home'),

    # page to request login credentials
    path('credentials', views.credentials, name = 'credentials'),

    # page to show the tweet plots
    path('timeline/', views.timeline, name = 'timeline'),

    #path('timeline/credentials/', views.get_credentials, name = 'get_credentials'),

]