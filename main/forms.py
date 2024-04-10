from django import forms

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
		fields = ['portfolio','cat','naran','data_hahu','data_remata','status']