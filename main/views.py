from django.shortcuts import render,redirect
from main.models import Portfolio,Project

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
	context = {
		'title':"Home Page",
		'home_active':"active",
	}

	return render(request,'index.html',context)

def about(request):
	context = {
		'title':"Kona-ba Ha'u",
		'about_active':"active",
	}
	return render(request,'about.html',context)

@login_required
def portfolio(request):
	dados_portfolio = Portfolio.objects.all()
	context = {
		'title':"Porfolio",
		'portfolio_active':"active",
		'dados':dados_portfolio,
	}
	return render(request,'portfolio.html',context)

def posts(request):
	context = {
		'title':"Posts",
		'posts_active':"active",
	}
	return render(request,'posts.html',context)

def partnership(request):
	context = {
		'title':"Partnership",
		'partnership_active':"active",
	}
	return render(request,'partnership.html',context)

def gallery(request):
	context = {
		'title':"gallery",
		'gallery_active':"active",
	}
	return render(request,'gallery.html',context)

def contact(request):
	context = {
		'title':"contact",
		'contact_active':"active",
	}
	return render(request,'contact.html',context)

def detailPost(request):
	context = {
		'title':"Post Detail",
		'posts_active':"active",
	}
	return render(request,'postDetail.html',context)

@login_required
def IndexAdmin(request):
	return render(request,'adminpage/index.html')


def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('IndexAdmin')
		else:
			messages.error(request,'Username ou Password la loos! Favor Prense fali!')
	context = {
		"title":"Pajina Login",
	}
	return render(request,'auth/login.html',context)

@login_required
def logoutPage(request):
	logout(request)
	return render(request,'auth/logout.html')

