Repositorio ida ne'e uza ba Kursu Django iha FDLS.

Atualizasaun sira iha Repositorio ida ne'e sei bazeia ba ========================== AULA nebe la'o.==========================

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

========================== AULA 2 ==========================

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


========================== AULA 3 ==========================

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

========================== AULA 4 ==========================

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


========================== AULA 5 ==========================

Kria Model ka tabela Database.
* Model ida iha Projetu Django reprezenta tabela ida iha Database.
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



========================== AULA 6 ==========================
Relational Model
iha Aula ida ne'e, ita kria Model Categoria no Project nebe sei iha relasaun ho Model Portfolio.

#Model Categoria 
class Categoria(models.Model):
    naran = models.CharField(max_length=30)
    
    def __str__(self):
        template = '{0.naran}'
        return template.format(self) 

#Model Project
class Project(models.Model):
    portfolio = models.OneToOneField(Portfolio,on_delete=models.CASCADE,related_name='portfolio')
    cat = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    naran = models.CharField(max_length=100)
    data_hahu = models.DateField()
    data_remata = models.DateField()
    status = models.CharField(choices=[('Inisiu','Inisiu'),('Prosesu Hela','Prosesu Hela'),('Finalizadu','Finalizadu')],max_length=20,default='Inisiu')


    def __str__(self):
        template = '{0.naran} | {0.status}'
        return template.format(self)

Iha Model Project mak ita iha relasaun ho Model Categoria no Portfolio.
relasaun ho Portfolio ho tipo One to One nunee deklara (OneToOneField):
    portfolio = models.OneToOneField(Portfolio,on_delete=models.CASCADE,related_name='portfolio')

relasaun ho categoria ho tipo One to Many nunee deklara (ForeignKey):
    cat = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    

Ita mos aumenta tan field status no enderesu_url iha Model Portfolio nune'e ita nia model Portfolio sai hanesan:

class Portfolio(models.Model):
    titulu = models.CharField(max_length=50)
    deskrisaun = models.CharField(max_length=225)
    imajen = models.ImageField(upload_to='portfolio',null=True,blank=True)
    status = models.BooleanField(default=False)
    enderesu_url = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        template = '{0.titulu}'
        return template.format(self)

Hafoin Kria Model rua no aumenta field iha Model Portfolio. Signifika ita halo mudansa ba Model nune'e ita presija halo migrasaun ba Database nune'e bele atualiza mudansa sira ne'e ba iha Database. Ho komanda :
    python manage.py makemigrations
    
    python manage.py migrate

Atu Model rua ne'ebe foun (Categoria no Project) mos mosu iha Admin Panel ita presija rejista liu husi file admin.py
Import uluk lai Model rua refere
    from main.models import Portfolio,Categoria,Project

tuir mai Rejista Model
    admin.site.register(Categoria)
    admin.site.register(Project)


Karik hotu ona ba Database. Tuir mai ita bele kontinua ho Queryset.
Loke fali Shell.
    python manage.py shell

Oinsa kria dadus categoria foun liu husi shell
primeiru tenki import Model sira ne'ebe iha ho maneira:
    from main.models import Portfolio,Categoria,Project

tuir mai queryset hodi kria categoria foun:
    dados_categoria = Categoria.objects.create(naran='Web Application')
tuir check dados_categoria hodi haree katak dados kria ona ka seidauk (bele mos hare liu husi admin panel)
    dados_categoria  

========================== AULA 7 ==========================
Kontinuasaun Aula 6 no Oinsa load dadus husi database ba iha template (Uza Queryset)
Oinsa Kria ka insere dadus foun ida iha Model Project, presija tau atensaun tamba Model refere iha ForeignKey.

Loke fali Shell
    python manage.py shell

Import Model sira ne'ebe atu uza iha shell
    from main.models import Portfolio,Categoria,Project

bainhira ita kria dadus foun iha Model Project ho maneira deklara direta ID portfolio no ID categoria hanesan iha kraik ne'e:

    dados_project = Project.objects.create(portfolio=5,cat=1,naran="Clinic Apointment System",data_hahu='2024-03-16',data_remata='2024-05-30',status='Finalizadu')

bainhira executa Queryset refere, sei mosu erro katak field rua portfolio no cat tenki instance husi Model Portfolio no Categoria.

Nune'e atu insere dadus foun iha Model Project ita tenki foti uluk lai dadus Portfolio no Categoria uza queryset get().

Ba Categoria:
    dados_cat = Categoria.objects.get(id=1)

Ba Portfolio:
    dados_portfolio = Portfolio.objects.get(id=5)

Karik ita iha ona dadus rua refere, tuir mai ita bele koko hodi hadia queryset hodi kria dadus Project.
    
    dados_project = Project.objects.create(portfolio=dados_portfolio,cat=dados_cat,naran="Clinic Apointment System",data_hahu='2024-03-16',data_remata='2024-05-30',status='Finalizadu')

karik mak mosu erro presija check fali queryset halo didiak.
bainhira susesu mak ita bele check dados nebe ita kria (ou bele check husi admin panel).
    dados_project 

Tuir Oinsa load dadus husi database ba iha template (Uza Queryset)
Exemplu ne'ebe ita sei halo mak, ita sei foti dadus Portfolio hodi ba mostra iha pajina Portfolio nian.

atu foti dadus Portfolio ita presija ba halo queryset iha view portfolio nian.

loke file view.py
no halo queryset iha view portfolio nian ho maneira all()
Portfolio.objects.all()

nune'e ita nia view ba portfolio nian sai hanesan tuir mai:

def portfolio(request):
    dados_portfolio = Portfolio.objects.all() #all() signifika foti dadus hotu-hotu
    context = {
        'title':"Porfolio",
        'portfolio_active':"active",
        'dados':dados_portfolio,
    }
    return render(request,'portfolio.html',context)

Hafoin ita foti dadus Portfolio no tau hamutuk ona iha render template, tuir mai ita bele ona bolu iha template html portfolio nian.
Loke file html portfolio nian
tamba dadus Portfolio nebe ita query, mai ho tipo Lista ka dadus barak (multiple data), atu mostra ita tenki looping dadus refere.

{% for data in dados %}
    <div class="col-md-4 col-sm-6">
         <div class="team-thumb">
              <div class="team-image">
                   {% if data.imajen %}<!-- kondisaun atu check karik imajen iha mak mostra selae mostra imajen default husi file static -->
                   <img src="{{data.imajen.url}}" class="img-responsive" alt="">
                   {% else %}
                   <img src="{% static 'images/author-image1.jpg' %}" class="img-responsive" alt="">
                   {% endif %}
              </div>
              <div class="team-info">
                   <h3>{{data.titulu}} </h3>
                   <span>{{data.deskrisaun}}</span>
              </div>
         </div>
    </div>
{% endfor %}

iha parte ida ne'e bele hare tuir iha file portfolio nia laran hodi haree kodigu html kompletu


========================== AULA 8 ==========================
Kria Custom Admin Page hodi jere dadus.

pip install django-crispy-forms
pip install crispy-bootstrap4

kria pajina index Admin nian.
    kria url:
        path('administrador/',IndexAdmin,name='IndexAdmin'),
    kria views:
        from django.contrib.auth.decorators import login_required
        @login_required #funsaun atu limita uzuariu atu asesu view ida ne'e karik tenki Login.
        def IndexAdmin(request):
            return render(request,'adminpage/index.html')

kria pajina login
    kria url:
        path('login/', loginPage, name='login'),
    kria view:
        from django.contrib import messages
        from django.contrib.auth import authenticate,login,logout
        def loginPage(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request,username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect('IndexAdmin')
                else:
                    messages.error(request,'Username ou Password la loos! Favor Prense fali!')
            context = {
                "title":"Pajina Login",
            }
            return render(request,'auth/login.html',context)
kria funsaun logout
    kria url:
        path('logout/', logoutPage, name='logout'),
    kria view:
        @login_required
        def logoutPage(request):
            logout(request)
            return render(request,'auth/logout.html')


file sira nebe uza iha materia ida ne'e
    -kopia file html sira iha app main no folder templates (auth no adminpage)
    -kopia static file ba pajina admin nian ho naran "main" iha folder static

konfigurasaun nebe halo iha aula ida ne'e:
iha file setting.py:
aumenta
LOGIN_URL = 'login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

no aumenta 
'crispy_forms',
'crispy_bootstrap4',
iha INSTALLED_APPS

========================== AULA 9 no 10 ==========================
1. Kontinuasaun Funsionalidade Login no Logout

2. Lee ka kria funsaun Read data Portfolio
    -Kria url ba lee dadus portfolio:
        path('admin-portfolio/', AdminPortfolio, name='admin-portfolio'),
    -Kria view hodi lee dadus Portfolio
        @login_required
        def AdminPortfolio(request):
            objects = Portfolio.objects.all()
            context = {
                'objects':objects
            }
            return render(request,'adminpage/portfolio.html',context)
    -kria template naran portfolio.html iha folder adminpage nia laran no lee ka hamosu dadus portfolio iha tabela:
        <table class="table table-bordered table-sm">
            <tr>
                <th>Imajen</th>
                <th>Titulu</th>
                <th>Deskrisaun</th>
                <th>#</th>
            </tr>
            {% for data in objects %} 
            <tr>
                <td>{% if data.imajen %}<img src="{{data.imajen.url}}" width="50px" height="50px">{%endif%}</td>
                <td>{{data.titulu}}</td>
                <td>{{data.deskrisaun}}</td>
                <td>
                    <a href="" class="btn btn-sm btn-outline-success my-4"><i class="fa fa-edit"></i></a>

                    <a href="" class="btn btn-sm btn-outline-danger my-4"><i class="fa fa-trash"></i></a>
                </td>
            </tr>
            {% endfor %}
        </table>   

3. Kria funsionalidade Create ka Insert dadus Portfolio
    -Kria url hodi handle insert dadus portfolio:
        path('admin-portfolio/add', AdminPortfolioAdd, name='admin-portfolio-add'),
    -Kria file forms.py hodi generate form ba Model Portfolio:
        from django import forms
        from main.models import *
            class PortfolioForm(forms.ModelForm):
                class Meta:
                    model = Portfolio
                    fields = ['titulu','deskrisaun','imajen','status','enderesu_url']
    -Kria view hodi halo funsaun insert dadus Portfolio
        from main.forms import PortfolioForm
        @login_required
        def AdminPortfolioAdd(request):
            if request.method == "POST":
                form = PortfolioForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Dadus Portfolio Rejistadu ho Susesu!')
                    return redirect('admin-portfolio')
            else:
                form = PortfolioForm()
            context = {
                'page':"Formulario Rejistu Portfolio",
                'form':form,
            }
            return render(request,'adminpage/add_portfolio.html',context)
    -Kria file add_portfolio.html no tau codigo html:
        {% extends "adminpage/admin_base.html" %}
        {% load crispy_forms_tags %}
        {% block content %}  
        <div class="container mt-3 p-5">
            <div class="card">
                <div class="card-header">
                    <h3>{{page}}</h3>
                </div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{form|crispy}}
                    <button type="submit" class="btn btn-sm btn-primary"><i class="fa fa-save"></i> Save</button>
                    <form>
                </div>
            </div>
            
        </div>

        {% endblock %}

4. Kria Funsionalidade Update dadus Portfolio
    -Kria url hodi handle update dadus portfolio:
        path('admin-portfolio/update/<str:id>', AdminPortfolioUpdate, name='admin-portfolio-update'),
    -Kria view hodi halo funsaun update dadus Portfolio
        @login_required
        def AdminPortfolioUpdate(request,id):
            dataPortfolio = Portfolio.objects.get(id=id)
            if request.method == "POST":
                form = PortfolioForm(request.POST, request.FILES,instance=dataPortfolio)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Dadus Portfolio Atualizadu ho Susesu!')
                    return redirect('admin-portfolio')
            else:
                form = PortfolioForm(instance=dataPortfolio)
            context = {
                'page':"Formulario Atualiza Portfolio",
                'form':form,
            }
            return render(request,'adminpage/add_portfolio.html',context)
    - iha funsaun update ida ne'e ita sei uza nafatin template add_portfolio.html tamba konteudu sei hanesan ho template add nian.

5. Kria Funsionalidade Delete dadus Portfolio
    -Kria url hodi handle delete dadus Portfolio
        path('admin-portfolio/delete/<str:id>', AdminPortfolioDelete, name='admin-portfolio-delete'),
    -Kria view hodi halo funsaun delete dadus Portfolio nian
        @login_required
        def AdminPortfolioDelete(request,id):
            dataPortfolio = Portfolio.objects.get(id=id)
            dataPortfolio.delete()
            messages.error(request,f'Dadus Portfolio {dataPortfolio.titulu} Hamoos ho Susesu!')
            return redirect('admin-portfolio')
    iha ne'e ita sei la uza template tanba bainhira dadus delete ona sei redirect kedas ba tabela portfolio nian.

NB:
ikus link husi create, update no delete sei uza iha template portfolio.html hanesan tuir mai ne'e:
 <div class="card-header">
    <a href="{% url 'admin-portfolio-add' %}" class="btn btn-sm btn-outline-info"><i class="fa fa-plus-square"></i> Rejistu Portfolio</a>
</div>
<div class="card-body">
    <table class="table table-bordered table-sm">
        <tr>
            <th>Imajen</th>
            <th>Titulu</th>
            <th>Deskrisaun</th>
            <th>#</th>
        </tr>
        {% for data in objects %}
        <tr>
            <td>{% if data.imajen %}<img src="{{data.imajen.url}}" width="50px" height="50px">{%endif%}</td>
            <td>{{data.titulu}}</td>
            <td>{{data.deskrisaun}}</td>
            <td>
                <a href="{% url 'admin-portfolio-update' data.id %}" class="btn btn-sm btn-outline-success my-4"><i class="fa fa-edit"></i></a>

                <a href="{% url 'admin-portfolio-delete' data.id %}" class="btn btn-sm btn-outline-danger my-4"><i class="fa fa-trash"></i></a>
            </td>
        </tr>
        {% endfor %}
    </table>    
</div>

Ba dadus Kategoria no Project Ita boot sira bele koko tuir Ezemplu CRUD iha Model Portfolio nian.

========================== AULA 11 ==========================
Kontinuasaun CRUD : Model Project no Aumenta Funsionalidade Konfirmasaun molok Delete Dadus.

1. CRUD Model Project :
    - Read Dados husi Model Project
        urls.py : path('admin-project/', AdminProject, name='admin-project'),
        views.py : kria view naran AdminProject
        kria template ho naran : project.html iha folder adminpage
    - Create ka insert Dados ba Model Project
        urls.py : path('admin-project/add', AdminProjectAdd, name='admin-project-add'),
        views.py : kria view naran AdminProjectAdd
        kria Form iha forms.py ho naran : ProjectForm
    - Update dados Project
        urls.py : path('admin-project/update/<str:pk>', AdminProjectUpdate, name='admin-project-update'),
        views.py : kria views ho naran AdminProjectUpdate
    - Delete dados Project
        urls.py : path('admin-project/delete/<str:id>', AdminProjectDelete, name='admin-project-delete'),
        views.py : kria views ho naran :AdminProjectDelete

2. Funsionalidade Konfirmasaun ba Delete dadus
    Iha butaun delete nian bainhira click sei mosu modal:
        <a href="#" data-toggle="modal" data-target="#delete-{{ data.id }}" class="btn btn-sm btn-outline-danger my-4"><i class="fa fa-trash"></i></a>
    Modal nebe atu mosu:
        <div class="modal fade" id="delete-{{ data.id}}">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-body">
                  Ita Boot hakarak hamoos dadus Projetu ho naran {{data.naran}}?
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-danger" data-dismiss="modal">No</button>
                  <a href="{% url 'admin-project-delete' data.id %}" class="btn btn-info">Yes</a>
                </div>
              </div>
            </div>
        </div>
        binhira user click iha konfirmasaun ka butaun yes mak sei ezekuta funsaun delete dadus.

Iha aula ida ne'e mos funsionalide CRUD ba Model Categoria Aumenta ona bele check iha kodigu.

========================== AULA 12 ==========================
Konekta django project ba Database (Mysql no Postgresql)
1. muda database default django nian (db.sqlite3) ba fali database MySQL no PostgreSQL
    settings.py
    # instalasaun library nebe apoio koneksaun no konfigurasaun database MySQL:
        pip install mysqlclient
        DATABASES = {  
            'default': {  
                'ENGINE': 'django.db.backends.mysql',  
                'NAME': 'db_blog',  
                'USER': 'root',  
                'PASSWORD': '',  
                'HOST': '127.0.0.1', 
                'PORT': '3306',  
                'OPTIONS': {  
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
                }  
            }  
        }

    # instalasaun library nebe apoio koneksaun database PostreSQL:
        pip install psycopg2
        DATABASES = {
            'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': 'db_blog',
               'USER': 'postgres',
               'PASSWORD': 'password', #tau password
               'HOST': 'localhost',
               'PORT': '5432',
               'OPTIONS': {
                    'options': '-c search_path=db_blog',
                },
            }
        }
    # husi parte database MySQL ka PostgreSQL ita tenki kria Database nebe ita atu konekta ba, exemplu: "db_blog".
    # hafoin konfigura database, presija migrate fali ba database foun nebe ita konfigura ona.
    python manage.py migrate

2. Kria Model Post

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

3. Organiza Estrutura Kodigu Django (Views no urls) 
    Views :
        kria folder views no separa views public nian ba file foun naran public_views.py no     administrador nian ba admin_views.py
    No rejistu fali file rua (public_view no admin_views) iha file foun naran __init__.py
        from .admin_views import *
        from .public_views import *
        from main.views1 import *
    Urls iha app blog nia laran:
        path("",include('main.urls_public')),
        path("administrador/",include('main.urls')),
    kria urls_public.py hodi rai url sira public nian
    no urls ba administrador nian manten nafatin ho urls.py

Iha aula ida ne mos atualiza ona CRUD ba Model Blog nian (check codigo tuir commit aula 12).


========================== AULA 13 ==========================
1. Review CRUD ba Model Blog nebe push iha aula 12
    urls crud nian:
        path('admin-post/', AdminPost, name='admin-post'),
        path('admin-post/add', AdminPostAdd, name='admin-post-add'),
        path('admin-post/update/<str:pk>', AdminPostUpdate, name='admin-post-update'),
        path('admin-post/delete/<str:pk>', AdminPostDelete, name='admin-post-delete'),
        funsionalidade update utiliza modal: 
        path('admin-post/load-post-update-form', AdminPostLoadUpdateForm, name='load-post-update-form'),
        funsionalidade halo asaun ba dadus post sira nebe ita hili:
        path('perform_post_action/', perform_post_action, name='perform_post_action'),
    views crud nian:
        @login_required
        def AdminPost(request):
            objects = Post.objects.all().order_by('-id')
            context = {
                'objects':objects,
                'title':"Lista Publikasaun",
                'page':"lista_post",
            }
            return render(request,'adminpage/posts.html',context)

        @login_required
        def AdminPostAdd(request):
            if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    Portfolio.objects.create()
                    post.save()
                    form.save_m2m()
                    messages.success(request,'Dadus Post Rejistadu ho Susesu!')
                    return redirect('admin-post')
            else:
                form = PostForm()
            context = {
                'title':"Formulario Rejistu Publikasaun",
                'form':form,
                'page':"form_post",
            }
            return render(request,'adminpage/add_portfolio.html',context)

        @login_required
        def AdminPostUpdate(request,pk):
            objects = get_object_or_404(Post,id=pk)
            if request.method == "POST":
                form = PostForm(request.POST,instance=objects)
                if form.is_valid():
                    post = form.save(commit=False)
                    # post.author = request.user
                    post.save()
                    form.save_m2m()
                    messages.success(request,'Dadus Post Atualizadu ho Susesu!')
                    return redirect('admin-post')
            else:
                form = PostForm(instance=objects)
            context = {
                'title':"Formulario Atualiza Publikasaun",
                'form':form,
                'page':"form_post",
            }
            return render(request,'adminpage/add_portfolio.html',context)

        @login_required
        def AdminPostDelete(request,pk):
            objects = get_object_or_404(Post,id=pk)
            objects.delete()
            messages.error(request,f'Dados Publikasaun {objects.title} hamoos ona ho susesu!')
            return redirect('admin-post')

        funsionalidade update utiliza modal: 
        @login_required
        def AdminPostLoadUpdateForm(request):
            if request.method == 'GET':
                object_id = request.GET.get('objectID')
                objects = get_object_or_404(Post,id=object_id)
                form = PostForm(instance=objects)
            context = {
                'form':form,
                'objects':objects,
            }
            return render(request,'adminpage/posts_load_form.html',context)

        from django.http import JsonResponse
        import json
        funsionalidade halo asaun ba dadus post sira nebe ita hili:
        @login_required
        def perform_post_action(request):
            if request.method == 'POST':
                if request.POST.get('checkedItems') == '':
                    messages.error(request,f'Oops! Ita boot seidauk hili dadus ruma.')
                    return redirect('admin-post')
                else:
                    action_type = request.POST.get('actionType')
                    ids = request.POST.get('checkedItems')
                    ids = ids.split(',')
                    if action_type == 'delete':
                        for i in ids:
                    data = get_object_or_404(Post,id=i)
                    data.delete()
                messages.success(request,f'Dados Publikasaun nebe ita boot hili, Delete ona ho susesu!')
                return redirect('admin-post')
            elif action_type == 'publishCheckedPost':
                for i in ids:
                    data = get_object_or_404(Post,id=i)
                    data.status = 'Published'
                    data.save()
                messages.success(request,f'Dados Publikasaun nebe ita boot hili, publika ona ho susesu!')
                return redirect('admin-post')
            elif action_type == 'draftCheckedPost':
                for i in ids:
                    data = get_object_or_404(Post,id=i)
                    data.status = 'Draft'
                    data.save()
                messages.success(request,f'Dados Publikasaun nebe ita boot hili, draft ona ho susesu!')
                return redirect('admin-post')
            else:
                return JsonResponse({'error': 'Invalid action type.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

2. Kria funsionalidade Change Password
    urls: 
        path('user/change/password/', UserPasswordChange.as_view(), name='user-change-password'),
    views:
        class based views nebe django prepara ona ba funsionalidade change password nian:
        from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
        from django.urls import reverse_lazy 
        class UserPasswordChange(PasswordChangeView):
            template_name = 'auth/change_password.html'
            success_url = reverse_lazy('user-change-password')
            def get_success_url(self):
                messages.success(self.request, 'Password was successfully changed.')
                return super().get_success_url()
            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return context
    templates:
        kria template ho naran change_password.html iha folder auth nia laran
3. codigo atu fo sai error sira iha form karik form nebe atu kria dadus hetan erro.
    {% if form.errors %}
        {% for field in form %}
            {% for error in field.errors %}
            <div id="divmessage" class="alert alert-danger alert-dismissable">
                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                {{ field.label }}: {{ error }}
              </div>
            {% endfor %}
        {% endfor %}
    {% endif %}
    codigo ida ne'e bele tau iha kada form sira hotu.

NB: ba file .html sira favor check direta iha file sira ho detallu.

========================== AULA 14 ==========================
1. Kria funsionalidade Change Username
    form :

        class UserChangeAccountForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username','email']

    url :

        path('user/change-user-account/',UserChangeAccount,name='user-change-account'),
    
    views :

        @login_required
        def UserChangeAccount(request):
            loginUser = get_object_or_404(User,id=request.user.id)
            if request.method == "POST":
                form = UserChangeAccountForm(request.POST,instance=loginUser)
                if form.is_valid():
                    form.save()
                    messages.success(request,f'Ita boot nia Konta Uzuario Atualiza ho susesu!')
                    return redirect('user-change-account')
            else:
                form = UserChangeAccountForm(instance=loginUser)

            context = {
                'form':form,
                'title':"Altera Konta Utilizador",
            }
            return render(request,'adminpage/add_portfolio.html',context)

2. Fo sai dadus post iha pajina publiku, halo queryset ba model Post iha views post nian

public_views:

def posts(request):
    objects = Post.objects.filter(status="Published").all()
    context = {
        'title':"Posts",
        'posts_active':"active",
        'dados':objects,
    }
    return render(request,'posts.html',context)

templates posts:

{% for data in dados %}
  <div class="col-md-4 col-sm-4">
       <div class="item">
            <div class="courses-thumb">
                 <div class="courses-top">
                      <div class="courses-image">
                           <img src="{% static 'images/courses-image1.jpg' %}" class="img-responsive" alt="">
                      </div>
                      <div class="courses-date">
                           <span><i class="fa fa-calendar"></i> {{data.publication_date}}</span>
                           <!-- <span><i class="fa fa-clock-o"></i> 7 Hours</span> -->
                      </div>
                 </div>

                 <div class="courses-detail">
                      <h3><a href="{% url 'detailPost' %}">{{data.title}}</a></h3>
                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                 </div>

                 
            </div>
       </div>
  </div>
{% endfor %}



