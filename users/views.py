from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from . forms import RegisterForm


# Create your views here.

def login_request(request):
	'''Login users'''
	if request.method != 'POST':	
		form = AuthenticationForm()
	else:
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/') # home for quick loading

	return render(request = request,
				  template_name = 'users/login.html',
				  context = {'form': form}
				  )

def logout_request(request):
	'''Logout user'''
	logout(request)
	return redirect('/') # home for now

def register(request):
	'''Register new users'''
	if request.method != 'POST':
		form = RegisterForm()
	else:
		form = RegisterForm(request.POST)
		if form.is_valid():
			# save details and authenticate user
			new_user = form.save()
			user = authenticate(username=new_user.username, 
								password=request.POST['password1'])
			if user is not None:
				login(request, user)
				return redirect('/tokens') # page for getting tokens

			#return login_request(request)
	return render(request = request,
				  template_name = 'users/register.html',
				  context = {'form':form}
				  )




