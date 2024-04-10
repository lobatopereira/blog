from django.urls import path
from main.views import *

urlpatterns = [
	path('', index, name='home'),

	path('post-detail/',detailPost,name='detailPost'),
	
	path('about-me/',about,name='konaba'),
	path('portfolio/',portfolio,name='portfolio'),
	path('posts/',posts,name='posts'),
	path('partnership/',partnership,name='partnership'),
	path('gallery/',gallery,name='gallery'),
	path('contact/',contact,name='contact'),

	# admin
	path('administrador/',IndexAdmin,name='IndexAdmin'),
	path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    
    
	path('admin-portfolio/', AdminPortfolio, name='admin-portfolio'),
	path('admin-portfolio/add', AdminPortfolioAdd, name='admin-portfolio-add'),
	path('admin-portfolio/update/<str:id>', AdminPortfolioUpdate, name='admin-portfolio-update'),
	path('admin-portfolio/delete/<str:id>', AdminPortfolioDelete, name='admin-portfolio-delete'),




	
]