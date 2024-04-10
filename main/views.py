from django.shortcuts import render,redirect
from main.models import Portfolio,Project

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from main.forms import PortfolioForm

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


@login_required
def AdminPortfolio(request):
	objects = Portfolio.objects.all()
	context = {
		'objects':objects
	}
	return render(request,'adminpage/portfolio.html',context)

@login_required
def AdminPortfolioAdd(request):
	if request.method == "POST":
		form = PortfolioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Portfolio Rejistadu ho Susesu!')
			return redirect('admin-portfolio')
	else:
		form = PortfolioForm()
	context = {
		'page':"Formulario Rejistu Portfolio",
		'form':form,
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPortfolioUpdate(request,id):
	dataPortfolio = Portfolio.objects.get(id=id)
	if request.method == "POST":
		form = PortfolioForm(request.POST, request.FILES,instance=dataPortfolio)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Portfolio Atualizadu ho Susesu!')
			return redirect('admin-portfolio')
	else:
		form = PortfolioForm(instance=dataPortfolio)
	context = {
		'page':"Formulario Atualiza Portfolio",
		'form':form,
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPortfolioDelete(request,id):
	dataPortfolio = Portfolio.objects.get(id=id)
	dataPortfolio.delete()
	messages.error(request,f'Dadus Portfolio {dataPortfolio.titulu} Hamoos ho Susesu!')
	return redirect('admin-portfolio')


	