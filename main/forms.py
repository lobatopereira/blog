from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from main.models import *


class DateInput(forms.DateInput):
	input_type = 'date'

class PortfolioForm(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = ['titulu','deskrisaun','imajen','status','enderesu_url']

class ProjectForm(forms.ModelForm):
	data_hahu = forms.DateField(label='Data Hahu', widget=DateInput())
	data_remata = forms.DateField(label='Data Remata', widget=DateInput())
	class Meta:
		model = Project
		fields = ['cat','naran','data_hahu','data_remata','status']

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['naran']

class PostForm(forms.ModelForm):
	content = forms.CharField(label="Konteudu", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}))
	category = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Post
		fields = ['title', 'content', 'category', 'status']  # Specify the fields you want in your form
		labels = {
			'title':"Titulu"
		}
	# def __init__(self, *args, **kwargs):
	# 	super(PostForm, self).__init__(*args, **kwargs)
	# 	self.fields['category'].queryset = Categoria.objects.all()  # Populate the category field with all categories
