Repositorio ida ne'e uza ba Kursu Django iha FDLS.

Atualizasaun sira iha Repositorio ida ne'e sei bazeia ba Aula nebe la'o.

Atu install python, bele download aplikasaun Python iha https://www.python.org/downloads/

Hafoin installa python, tuir mai ne'e oinsa kria ambiente virtual (virtual environment) 
hodi installa pakote sira ne'ebe sei suporta ba dezenvolve aplikasaun web ho framework Django.

komandu atu kria ambiente virtual : 
    python -m venv <ambiente virtual nia naran>
    ex: python -m venv djangocourseenv

atu servisu iha ambiente virtual ida ne'e, presija ativu ambiente refere ho komandu mak:
    djangocourseenv\Scripts\activate.bat ka djangocourseenv\Scripts\activate

Bainhira ativu ona ambiente virtual refere. ita bele ona installa pakote sira nebe suporta projetu ida ne'e mak hanesan:
    installa django : pip install django

komandu hodi check django installa ona ka seidauk:
    django-admin --version

karik installa ona. ita bele diresiona ba folder projetu nian nebe naran "blog" ho komandu "cd blog" no ezekuta komandu:
    python manage.py runserver 
hodi lansa projetu refere.



--------informasaun adisional--------
komandu hodi kria projetu foun:
    django-admin startproject <naran projetu>

komandu hodi kria app foun iha projetu django:
    python manage.py startapp <app nia naran>

komandu atu kria file migrasaun:
    python manage.py makemigrations
    

komandu atu orienta base de dados hodi kria tabela tuir file migrasaun nebe kria ona
    python manage.py migrate

aula 2
# muda default template django nian, troka ho ita nia template rasik
1. kria app ho naran "main"
    python manage.py startapp main
2. rejista app main iha settings.py iha parte INSTALLED_APPS 
    "main",

3. kria file ho naran "urls.py" iha app main nia laran no kria lista url no bolu views naran "index"

    from django.urls import path
    from main.views import index

    urlpatterns = [
        path('', index, name='home'),
        
    ]

4. kria view naran "index" iha file views.py iha app main nia laran
    def index(request):
	    return render(request,'index.html')

5. tamba ita render template "index.html" entaun ita presija kria file tempate refere
    - iha app main nia laran, kria folder naran "templates"
    - kria file naran "index.html" iha folder templates nebe ita kria
    - iha file "index.html" nia laran koko kria codigu html simples hodi haree iha pajina web
6. urls.py nebe ita kria iha app main nia laran, ita mos presija rejista iha ita nia main url
nebe lokaliza iha app konfigurasaun nian iha file urls.py! iha kazu ida ne'e. file urls.py iha blog nia laran.
    - inklui funsaun "include"
        from django.urls import path,include  
    - resjita urls foun husi app main
        path("",include('main.urls')),
    keta haluha atu aumenta virgula "," iha lista url sira.


aula 3
# load static files in django project

1. foti template nebe ita hakarak
2. copy folder css,fonts,img,js. kria folder static iha projetu blog (sejajar ho app sira) no paste folder css,fonts,img,js ba lara.
3. resjitu static folder da settings.py
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
4. load static file iha templates
    {% load static %}
5. bolu file specifiku css,img,js ih template
    {% static 'css/bootstrap.min.css' %}
    
    <img src="{% static 'images/author-image1.jpg' %}" class="img-responsive" alt="">
    <script src="{% static 'js/jquery.js' %}"></script>

6. apply template inheritance
    - kria file base.html
    - cut conteudu file no kria block naran konteudu
        {% block konteudu %}      
        {% endblock %}  
    - paste fali conteudu ba index.html no tau iha block naran konteudu
    - no extend file index ba file base
        {% extends 'base.html' %}

aula 4 
Troka/muda templates tuir nesesidade
    
-deklara variavel no valor hodi mostra iha template
    -Deklara object ho naran context no tau informasaun sira iha object nia laran no bolu iha return

    def index(request):
        context = {
            'title':"Home Page",
        }
        return render(request,'index.html',context)

    -Halo maeira hanesan ba view seluk nafatin ho key mak title maibe valor diferente tuir pajina ida-idak
    
    def about(request):
        context = {
            'title':"Kona-ba Ha'u",
        }
        return render(request,'about.html',context)

-oinsa mostra informasaun ne'e haruku husi view ba iha template
    -key nebe deklara naran title nune'e iha file html ita sei bolu nia ho maneira
        {{title}}

    ezemplu :

             <title>Portfolio - {{title}}</title>

            - tau iha parte head husi html ou iha parte seluk template nian

aula 5

Kria Model ka tabela Database
exemplu model ba rai dadus Portfolio ho kampu sira mak henesan (titulu,deskrisaun no imajen).
jeralmente django sei kria id nudar primary key automatika ba model karik ita la kria manual.

class Portfolio(models.Model):
	titulu = models.CharField(max_length=50)
	deskrisaun = models.CharField(max_length=225)
	imajen = models.ImageField(upload_to='portfolio',null=True,blank=True)

	def __str__(self):
		template = '{0.titulu}'
		return template.format(self)

hafoin kria Model ita mos sei ba rejista iha file admin.py hodi hamosu iha admin panel.
presija import model portfolio
    from main.models import Portfolio
tuir mai rejista
    admin.site.register(Portfolio)

-library nebe suporta hodi uza ImageField mak narna Pillow. nunee ita presija intalla ho maneira
    python -m pip install Pillow

hafoin kria model iha ita nia projetu ita presija run komandu tuir mai ne'e:
    python manage.py makemigrations     : atu kria file migrations
    no
    python manage.py migrate            : atu komunika ho database hodi kria tabela tuir model nebe kria iha project


-konfigura file imajen nebe upload / media file
    settings.py 
        MEDIA_ROOT = BASE_DIR / 'media'
        MEDIA_URL = '/media/'
    urls.py 
        from django.conf import settings
        from django.conf.urls.static import static
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

karik ita kria susesu ona ita nia Model. Ita bele ona koko halo querysets.

maneira atu halimar querysets iha terminal :
    python manage.py shell

hafoin tama tiha ba shell, molok ita atu halimar querysets ita presija import models ne'ebe atu koko querysets.
exemplu portfolio
    from main.models import Portfolio

querysets sira mak hanesan:

    Select :
        data = Portfolio.objects.all()      : atu fo sai dados hotu hotu iha tabela Portfolio
        data = Portfolio.objects.get(id=1)  : atu fo sai dados Portfolio ho ID '1'. queryset ida ne'e sei retorna dados ida deit.
        data = Portfolio.objects.filter(titulu='Web') : sei fo sai dados Portfolio sira ne'ebe ho titulu 'Web'
        data = Portfolio.objects.filter(titulu__icontains='Web') : sei fo sai dados Portfolio sira ne'ebe iha titulu eziste liafuan 'Web'

    Create:
        portfolio_instance = Portfolio.objects.create(titulu='django framework',deskrisaun='deskrisaun')
        aneksa file imajen
        >>> dir_imajen = 'C:/Users/Lobato Pereira/blog/static/images/bg8.jpg'
        >>> with open(dir_imajen, 'rb') as f:
        ...     portfolio_instance.imajen.save('bg8.jpg',f)
        ...
        >>> portfolio_instance.save()

    Update:
        portfolio_instance = Portfolio.objects.get(pk=1) 
        portfolio_instance.titulu = 'Updated Titulu'
        portfolio_instance.save()

    Delete
        portfolio_instance = Portfolio.objects.get(pk=1) 
        portfolio_instance.delete()