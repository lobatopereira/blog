from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
 a =1
 return render(request,'about.html')


