from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'AppVideos/index.html')


""" secciones """
def series(request):
    return render(request, 'AppVideos/series.html')

def peliculas(request):
    return render (request, 'AppVideos/peliculas.html')

def galeria(request):
    return render(request, 'AppVideos/galeria.html')

def facebook(request):
    return render(request, 'AppVideos/facebook.html')


""" series """

def reyes(request):
    return render (request, 'AppVideos/reyes.html')

def apoca(request):
    return render (request, 'AppVideos/apocalipsis.html')


def reydavi(request):
    return render (request, 'AppVideos/reydavi.html')

def elrico(request):
    return render (request, 'AppVideos/elrico.html')

def genesis1(request):
    return render (request, 'AppVideos/genesis1.html')


def genesis2(request):
    return render (request, 'AppVideos/genesis2.html')

def jesus(request):
    return render (request, 'AppVideos/jesus.html')

def jezabel(request):
    return render (request, 'AppVideos/jezabel.html')

def joseegi(request):
    return render (request, 'AppVideos/joseegi.html')


def tierrapro(request):
    return render (request, 'AppVideos/tierrapro.html')

def biblia(request):
    return render (request, 'AppVideos/biblia.html')

def bibliac(request):
    return render (request, 'AppVideos/bibliac.html')

def reynaester(request):
    return render (request, 'AppVideos/reynaester.html')

def lea(request):
    return render (request, 'AppVideos/lea.html')


def milagros(request):
    return render (request, 'AppVideos/milagros.html')


def mariamag(request):
    return render (request, 'AppVideos/mariamag.html')

def moises(request):
    return render (request, 'AppVideos/moises.html')


def sanson(request):
    return render (request, 'AppVideos/sanson.html')