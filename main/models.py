from django.db import models

# Create your models here.

class Portfolio(models.Model):
	titulu = models.CharField(max_length=50)
	deskrisaun = models.CharField(max_length=225)
	imajen = models.ImageField(upload_to='portfolio',null=True,blank=True)

	def __str__(self):
		template = '{0.titulu}'
		return template.format(self)



