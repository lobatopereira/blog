from django.urls import path
from main.views import index,about

urlpatterns = [
	path('', index, name='home'),
	path('about/', about, name='konaba')
	
]