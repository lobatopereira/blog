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








