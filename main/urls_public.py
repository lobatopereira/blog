from django.urls import path
from main.views import *

urlpatterns = [
	path('', index, name='home'),

	path('post-detail/<str:postId>',detailPost,name='detailPost'),
	
	path('about-me/',about,name='konaba'),
	path('portfolio/',portfolio,name='portfolio'),
	path('posts/',posts,name='posts'),
	path('partnership/',partnership,name='partnership'),
	path('gallery/',gallery,name='gallery'),
	path('contact/',contact,name='contact'),

]