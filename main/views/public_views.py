from django.shortcuts import render,redirect,get_object_or_404
from main.models import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from main.forms import PortfolioForm,ProjectForm,CategoriaForm


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
	objects = Post.objects.filter(status="Published").all()

	post_image_urls = []
	for post in objects:
		image_urls,text = extract_images_from_post_content(post.content)
		_,words20 = extract_total_words(text)
		post_image_urls.append({
			'id':post.id,
			'title':post.title,
			'image':image_urls,
			'content_text':words20,
			'publication_date':post.publication_date,
			})
	print('post_image_urls:',post_image_urls)

	context = {
		'title':"Posts",
		'posts_active':"active",
		'post_image_urls':post_image_urls,
		'dados':objects,
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

def detailPost(request,pk):
	postData = get_object_or_404(Post,id=pk)
	recentPost = Post.objects.all().order_by('-publication_date')[:3]
	recent_post_with_image = []
	for post in recentPost:
		image_urls,text = extract_images_from_post_content(post.content)
		words10,_ = extract_total_words(text)
		recent_post_with_image.append({
			'id':post.id,
			'title':post.title,
			'image':image_urls,
			'content_text':words10,
			'publication_date':post.publication_date,
			})
	context = {
		'title':"Post Detail",
		'posts_active':"active",
		'postData':postData,
		'recentPost':recent_post_with_image,
	}
	return render(request,'postDetail.html',context)

from bs4 import BeautifulSoup

# Assuming you have a Post model with a 'content' field containing HTML content
from main.models import Post

def extract_images_from_post_content(content):
    # Parse the HTML content of each post
    soup = BeautifulSoup(content, 'html.parser')

    # Find all image tags in the content
    images = soup.find_all('img')

    text = soup.get_text(separator=' ')
    text = ' '.join(text.split())

    # Extract the src attribute of each image
    image_urls = [img['src'] for img in images]

    # Return the list of image URLs
    return image_urls,text

def extract_total_words(text):
    # Split the text into words
    words = text.split()

    # Take the first 100 words
    words10 = ' '.join(words[:10])
    words20 = ' '.join(words[:20])

    return words10,words20


