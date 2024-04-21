from django.shortcuts import render,redirect,get_object_or_404
from main.models import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from main.forms import *

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

from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
class UserPasswordChange(PasswordChangeView):

	template_name = 'auth/change_password.html'
	success_url = reverse_lazy('user-change-password')
	def get_success_url(self):
		messages.success(self.request, 'Password was successfully changed.')
		return super().get_success_url()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context



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
	
@login_required
def AdminPost(request):
	objects = Post.objects.all().order_by('-id')
	context = {
		'objects':objects,
		'title':"Lista Publikasaun",
		'page':"lista_post",
	}
	return render(request,'adminpage/posts.html',context)

@login_required
def AdminPostAdd(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			Portfolio.objects.create()
			post.save()
			form.save_m2m()
			messages.success(request,'Dadus Post Rejistadu ho Susesu!')
			return redirect('admin-post')
	else:
		form = PostForm()
	context = {
		'title':"Formulario Rejistu Publikasaun",
		'form':form,
		'page':"form_post",
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPostUpdate(request,pk):
	objects = get_object_or_404(Post,id=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance=objects)
		if form.is_valid():
			post = form.save(commit=False)
			# post.author = request.user
			post.save()
			form.save_m2m()
			messages.success(request,'Dadus Post Atualizadu ho Susesu!')
			return redirect('admin-post')
	else:
		form = PostForm(instance=objects)
	context = {
		'title':"Formulario Atualiza Publikasaun",
		'form':form,
		'page':"form_post",
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPostDelete(request,pk):
	objects = get_object_or_404(Post,id=pk)
	objects.delete()
	messages.error(request,f'Dados Publikasaun {objects.title} hamoos ona ho susesu!')
	return redirect('admin-post')

@login_required
def AdminPostLoadUpdateForm(request):
	if request.method == 'GET':
		object_id = request.GET.get('objectID')
		objects = get_object_or_404(Post,id=object_id)
		form = PostForm(instance=objects)
	context = {
		'form':form,
		'objects':objects,
	}
	return render(request,'adminpage/posts_load_form.html',context)

from django.http import JsonResponse
import json

@login_required
def perform_post_action(request):
    if request.method == 'POST':
    	if request.POST.get('checkedItems') == '':
    		messages.error(request,f'Oops! Ita boot seidauk hili dadus ruma.')
    		return redirect('admin-post')
    	else:
	        action_type = request.POST.get('actionType')
	        ids = request.POST.get('checkedItems')
	        ids = ids.split(',')
	        if action_type == 'delete':
	            for i in ids:
	            	data = get_object_or_404(Post,id=i)
	            	data.delete()
	            messages.success(request,f'Dados Publikasaun nebe ita boot hili, Delete ona ho susesu!')
	            return redirect('admin-post')
	        elif action_type == 'publishCheckedPost':
	        	for i in ids:
	        		data = get_object_or_404(Post,id=i)
	        		data.status = 'Published'
	        		data.save()
	        	messages.success(request,f'Dados Publikasaun nebe ita boot hili, publika ona ho susesu!')
	        	return redirect('admin-post')
	        elif action_type == 'draftCheckedPost':
	        	for i in ids:
	        		data = get_object_or_404(Post,id=i)
	        		data.status = 'Draft'
	        		data.save()
	        	messages.success(request,f'Dados Publikasaun nebe ita boot hili, draft ona ho susesu!')
	        	return redirect('admin-post')
	        else:
	            return JsonResponse({'error': 'Invalid action type.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
