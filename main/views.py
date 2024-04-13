from django.shortcuts import render,redirect,get_object_or_404
from main.models import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from main.forms import PortfolioForm,ProjectForm,CategoriaForm

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
		'objects':objects,
		'title':"Lista Portfolio",
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
		'title':"Formulario Rejistu Portfolio",
		'form':form,
		'page':"form_portfolio",
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
		'title':"Formulario Atualiza Portfolio",
		'form':form,
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPortfolioDelete(request,id):
	dataPortfolio = Portfolio.objects.get(id=id)
	dataPortfolio.delete()
	messages.error(request,f'Dadus Portfolio {dataPortfolio.titulu} Hamoos ho Susesu!')
	return redirect('admin-portfolio')

@login_required
def AdminProject(request):
	objects = Project.objects.all()
	context = {
		'objects':objects,
		'title':"Lista Projetu",
		'page':"lista_projetu",
	}
	return render(request,'adminpage/project.html',context)

@login_required
def AdminProjectAdd(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Projetu Rejistadu ho Susesu!')
			return redirect('admin-project')
	else:
		form = ProjectForm()
	context = {
		'title':"Formulario Rejistu Projetu",
		'form':form,
		'page':"form_project",
	}
	return render(request,'adminpage/add_portfolio.html',context)
	
@login_required
def AdminProjectUpdate(request,pk):
	objects = get_object_or_404(Project,id=pk)
	if request.method == "POST":
		form = ProjectForm(request.POST,instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Projetu Atualizadu ho Susesu!')
			return redirect('admin-project')
	else:
		form = ProjectForm(instance=objects)
	context = {
		'title':"Formulario Atualiza Projetu",
		'form':form,
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminProjectDelete(request,id):
	objects = get_object_or_404(Project,id=id)
	objects.delete()
	messages.error(request,f'Dados Projetu hamoos ona ho susesu!')
	return redirect('admin-project')
	
@login_required
def AdminCategoria(request):
	objects = Categoria.objects.all()
	context = {
		'objects':objects,
		'title':"Lista Kategoria",
		'page':"lista_kategoria",
	}
	return render(request,'adminpage/categoria.html',context)

@login_required
def AdminCategoriaAdd(request):
	if request.method == "POST":
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Projetu Rejistadu ho Susesu!')
			return redirect('admin-categoria')
	else:
		form = CategoriaForm()
	context = {
		'title':"Formulario Rejistu Kategoria",
		'form':form,
		'page':"form_categoria",
	}
	return render(request,'adminpage/add_portfolio.html',context)
	
@login_required
def AdminCategoriaUpdate(request,pk):
	objects = get_object_or_404(Categoria,id=pk)
	if request.method == "POST":
		form = CategoriaForm(request.POST,instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request,'Dadus Kategoria Atualizadu ho Susesu!')
			return redirect('admin-categoria')
	else:
		form = CategoriaForm(instance=objects)
	context = {
		'title':"Formulario Atualiza Kategoria",
		'form':form,
		'page':'form_categoria',
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminCategoriaDelete(request,id):
	objects = get_object_or_404(Categoria,id=id)
	objects.delete()
	messages.error(request,f'Dados Kategoria hamoos ona ho susesu!')
	return redirect('admin-categoria')
	