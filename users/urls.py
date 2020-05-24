'''URLs for users app'''

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
				path('login/', views.login_request, name = 'login'),
				path('logout/', views.logout_request, name = 'logout'),
				path('register/', views.register, name = 'register'),
    			path('account/', views.account, name = 'account'),
    			path('account/edit_tokens', views.edit_tokens, name = 'edit_tokens'),
				]