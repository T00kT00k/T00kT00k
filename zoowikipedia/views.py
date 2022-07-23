from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

backtomain = ["Вернуться на главную страницу"]

# Главная страница (показывает список постов о Классах животных)
def index(request):
    classis = Classis.objects.all()

    # Словарь
    context = {
        'classis': classis, #post
        'menu': menu,
        'title': 'Главная страница',
        'classis_selected': 0, #cat_selected
    }
    #women/index.html
    return render(request, 'zoowikipedia/index.html', context=context)



# Страница с информацией о сайте
def about(request):
    return HttpResponse("О сайте")
    #return render(request, 'zoowikipedia/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

# Информационная страница
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# Показывает пост о классе животных
def show_classis(request, classis_id):
    classis = get_object_or_404(Classis, pk=classis_id)

    # Словарь
    context = {
        'classis': classis,  # post
        'menu': menu,
        'title': classis.name,
        'classis_selected': classis.pk,  # cat_selected
    }
    # women/index.html
    return render(request, 'zoowikipedia/classis_post.html', context=context)

# Показывает список постов об отрядах, принадлежащих выбранному классу
#show_cathegory
#def show_classis(request, classis_id):
    #women
#    posts = Ordo.objects.filter(classis_id=classis_id) #classis_id

#    if len(posts) == 0:
#        raise Http404()

    #Словарь
#    context = {
#        'ordo': posts,
#        'menu': menu,
#        'title': 'Отображение отрядов в классе',
#        'classis_selected': classis_id,
#    }
#    return render(request, 'zoowikipedia/index.html', context=context)