from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':"Home Page",
	}

	return render(request,'index.html',context)

def about(request):
	context = {
		'title':"Kona-ba Ha'u",
	}
	return render(request,'about.html',context)

def detailPost(request):
	context = {
		'title':"Post Detail",
	}
	return render(request,'postDetail.html',context)


