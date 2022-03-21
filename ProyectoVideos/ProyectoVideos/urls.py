"""ProyectoVideos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppVideos import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #secciones 

    path('',views.index, name= 'Inicio' ),
    path('series/', views.series, name= 'Series'),
    path('galeria/', views.galeria, name= 'Galeria'),
    path('peliculas/', views.peliculas, name= 'Peliculas'),
    path('verfacebook/', views.facebook, name= 'Facebook'),

    #seccion de capitulos
    path('reyes/', views.reyes, name= 'Reyes'),
    path('apocalipsis/', views.apoca, name= 'Apoca'),
    path('reydavid/', views.reydavi, name= 'ReyDavi'),
    path('elricoylazaro/', views.elrico, name= 'Elrico'),
    path('genesis1/', views.genesis1, name= 'Genesis1'),
    path('genesis2/', views.genesis2, name= 'Genesis2'),
    path('jesus/', views.jesus, name= 'Jesus'),
    path('jezabel/', views.jezabel, name= 'Jezabel'),
    path('josedeegipto/', views.joseegi, name= 'Josedegipto'),
    path('tierraprometida/', views.tierrapro, name= 'Tierrapro'),
    path('labiblia/', views.biblia, name= 'Biblia'),
    path('labibliacontinua/', views.bibliac, name= 'Bibliac'),
    path('lareynaester/', views.reynaester, name= 'Reynaester'),
    path('lea', views.lea, name= 'Lea'),
    path('losmilagrosdejesus', views.milagros, name= 'Milagros'),
    path('mariamagdalena', views.mariamag, name= 'Mariamag'),
    path('moisesylosdiezmandamientos', views.moises, name= 'Moises'),
    path('sansonydalila', views.sanson, name= 'Sanson'),



    

]
