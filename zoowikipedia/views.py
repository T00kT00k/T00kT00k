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
        'classis': classis,
        'menu': menu,
        'title': 'Главная страница',
        'classis_selected': 0,
    }

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
def show_classis(request, classis_post_id):
    post = get_object_or_404(Classis, pk=classis_post_id)
    classis = Classis.objects.all()

    # Словарь
    context = {
        'post': post,  # post
        'classis': classis,
        'menu': menu,
        'title': post.name,
        'classis_selected': post.pk,  # cat_selected
    }
    # women/index.html
    return render(request, 'zoowikipedia/classis_post.html', context=context)

# Список отрядов животных выбранного класса
def list_ordo(request, classis_list_id):
    ordo = Ordo.objects.filter(classis_id=classis_list_id)
    classis = Classis.objects.all()

    context = {
        'ordo': ordo,
        'classis': classis,
        'menu': menu,
        'title': 'Отображение по классам',
        'classis_selected': classis_list_id
    }

    return render(request, 'zoowikipedia/list_ordo.html', context=context)

# Показывает пост о классе животных
def show_ordo(request, ordo_id, classis_id):
    post = get_object_or_404(Ordo, pk=ordo_id)
    classis = Classis.objects.all()

    # Словарь
    context = {
        'post': post,  # post
        'classis': classis,
        'menu': menu,
        'title': post.name,
        'ordo_selected': post.pk,  # cat_selected
    }
    # women/index.html
    return render(request, 'zoowikipedia/ordo_post.html', context=context)

