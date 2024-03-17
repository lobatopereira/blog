from django.shortcuts import render
from main.models import Portfolio,Project

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


