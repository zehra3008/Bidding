from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ActiveList, UserBid, UserComment, WatchList
from .forms import CreateListForm, UserBidForm, CreateUserForm, UserCommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, username + ', your account have successfully created.')
				return redirect('index')
	context = {
		'form' : form
	}
	return render(request, 'auction/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is wrong')
		context = {}
		return render(request, 'auction/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	messages.info(request, 'You have been logout.')
	return redirect('login')

@login_required(login_url='login')
def index(request):
	product = ActiveList.objects.all()
	context = {
		'product' : product,
		'title' : 'Active Listing'
	}
	return render(request, 'auction/index.html', context)

@login_required(login_url='login')
def createList(request):
	form = CreateListForm()
	if request.method == 'POST':
		form = CreateListForm(request.POST)
		if form.is_valid():
			owner = form.cleaned_data['owner']
			name = form.cleaned_data['name']
			bid = form.cleaned_data['bid']
			category = form.cleaned_data['category']
			note = form.cleaned_data['note']
			#form.save()
			return redirect('index')
	context = {
		'form' : form
	}
	return render(request, 'auction/createlist.html', context)

@login_required(login_url='login')
def detail(request, pk):
	item = ActiveList.objects.get(id=pk)
	comments = UserComment.objects.filter(item=item)
	currentbid = item.bid
	user = request.user
	form = UserBidForm()
	commentform = UserCommentForm()
	if request.method == 'POST':
		form = UserBidForm(request.POST)
		commentform = UserCommentForm(request.POST)
		if commentform.is_valid():
			comment = commentform.cleaned_data['comment']
			commentset = UserComment(item=item, commenter=user, comment=comment)
			commentset.save()
			context = {
				'item' : item,
				'comments' : comments,
				'form' : form,
				'commentform' : commentform
			}
			return render(request, 'auction/detail.html', context) 

		if form.is_valid():
			bid = form.cleaned_data['userbid']
			if bid <= currentbid:
				messages.warning(request, 'Bid should be greater than current bid.')
				context = {
					'item' : item,
					'comments' : comments,
					'form' : form,
					'commentform' : commentform
				}
				return render(request, 'auction/detail.html', context) 
			else:
				try:
					formset = UserBid(product=item, userbid=bid, bider=user)
					formset.save()
					messages.success(request, 'Your bid has successfully saved, result will declared in bit.')
					return redirect('index')
				except:
					messages.info(request, 'Sorry, something went wrong. Please try to bid again.')
					context = {
					'item' : item,
					'form' : form,
					'commentform' : commentform
				}
				return render(request, 'auction/detail.html', context)
	else:
		context = {
			'item' : item,
			'comments' : comments,
			'form' : form,
			'commentform' : commentform
		}
		return render(request, 'auction/detail.html', context)

def categories(request, category):
	product = ActiveList.objects.filter(category=category)
	context = {
		'product' : product,
		'title' : category,
	}
	return render(request, 'auction/index.html', context)

def watchlist(request, pk=None):
	print("WatchList")
	user_list, created = WatchList.objects.get_or_create(user_watchlist=request.user)
	if request.method == 'GET':
		try:
			item = ActiveList.objects.get(id=pk)

			if WatchList.objects.filter(user_watchlist=request.user, watchlist=item).exists():
				messages.info(request, 'You already have item in your watchlist.')
				return redirect('index')
			else:
				user_list, created = WatchList.objects.get_or_create(user_watchlist=request.user)
				item = ActiveList.objects.get(id=pk)
				item.save()
				user_list.watchlist.add(item)
				messages.success(request, "Successfully added to your watchlist.")
				context = {
					'product' : ActiveList.objects.all()
				}
				return render(request, "auction/index.html",context)
		except:
			product = user_list.watchlist.all()
			context = {
				'product' : product,
				'title' : 'Watchlist'
			}
			return render(request, 'auction/index.html', context)