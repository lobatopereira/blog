from django.db import models

# Create your models here.


class Portfolio(models.Model):
	titulu = models.CharField(max_length=50)
	deskrisaun = models.CharField(max_length=225)
	imajen = models.ImageField(upload_to='portfolio',null=True,blank=True)
	status = models.BooleanField(default=False)
	enderesu_url = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		template = '{0.titulu}'
		return template.format(self)

class Categoria(models.Model):
	naran = models.CharField(max_length=30)
	
	def __str__(self):
		template = '{0.naran}'
		return template.format(self)	

class Project(models.Model):
	portfolio = models.OneToOneField(Portfolio,on_delete=models.CASCADE,related_name='project',null=True,blank=True)
	cat = models.ForeignKey(Categoria,on_delete=models.CASCADE)
	naran = models.CharField(max_length=100)
	data_hahu = models.DateField()
	data_remata = models.DateField()
	status = models.CharField(choices=[('Inisiu','Inisiu'),('Prosesu Hela','Prosesu Hela'),('Finalizadu','Finalizadu')],max_length=20,default='Inisiu')


	def __str__(self):
		template = '{0.naran} | {0.status}'
		return template.format(self)

from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Categoria)
    status_choices = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('scheduled', 'Scheduled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='draft')

    def __str__(self):
        return self.title

# Kliete
# Periodu
# categoria



