from django.urls import path
from main.views import index,about,detailPost

urlpatterns = [
	path('', index, name='home'),

	path('post-detail/',detailPost,name='detailPost'),
	
	path('about-me/',about,name='konaba'),

	
]