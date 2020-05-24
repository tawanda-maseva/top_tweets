from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . forms import RegisterForm
from ttweets_app.models import Access_Tokens
from ttweets_app.forms import TokensForm


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
				return redirect('/') # home

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

	return render(request = request,
				  template_name = 'users/register.html',
				  context = {'form':form}
				  )

@login_required
def account(request):
	'''Show the user's tokes info'''
	account_owner = User.objects.get(username = request.user)
	saved_tokens = True
	try:
		tokens = Access_Tokens.objects.get(owner_id = account_owner.id)
	except Access_Tokens.DoesNotExist:
		#return redirect('/')
		saved_tokens = False # user has not saved tokens yet
		return render(request, 'users/account.html', context ={'saved_tokens':saved_tokens})

	return render(request = request,
				  template_name = 'users/account.html',
				  context = {'tokens':tokens, 'saved_tokens':saved_tokens}
				  )

@login_required
def edit_tokens(request):
	'''Edit the username tokens'''
	account_owner = User.objects.get(username = request.user)
	tokens = Access_Tokens.objects.get(owner_id = account_owner.id)

	if request.method != 'POST':
		# display tokens	
		form = TokensForm(instance = tokens)
	else:
		#update instance and save
		form = TokensForm(instance = tokens ,data = request.POST)
		if form.is_valid():
			#form = form.save(commit = False)
			#form.owner = request.user
			form.save()
			return redirect('/users/account') # to home
	return render(request = request,
				  template_name = 'users/edit_tokens.html',
				  context = {'form':form}
				  )



