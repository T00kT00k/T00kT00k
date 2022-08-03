from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'action_page'},
]

action_menu = [{'title': "Добавить новый класс", 'url_name': "create_classis"},
               {'title': "Добавить новый отряд", 'url_name': "create_ordo"},
]

backtomain = ["Вернуться на главную страницу"]

# Главная страница (показывает список постов о Классах животных)
def index(request):

    # Словарь
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'classis_selected': 0,
    }
    return render(request, 'zoowikipedia/index.html', context=context)

# Страница с информацией о сайте
def about(request):
    # Словарь
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'zoowikipedia/about.html', context=context)

# Страница выбора объекта для дальнейших действий
def actionPage(request):

    # Словарь
    context = {
        'menu': menu,
        'title': 'Выбор объекта',
        'action_menu': action_menu,
        # 'classis_selected': 0,
    }
    return render(request, 'zoowikipedia/action.html', context=context)

# Добавление информации о классе на сайт
def addClassis(request):
    if request.method == 'POST':
        form = AddClassisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddClassisForm()
    return render(request, 'zoowikipedia/create_classis.html', {'form': form, 'menu': menu, 'title': 'Добавление класса'})

# Добавление информации об отряде на сайт
def addOrdo(request):
    if request.method == 'POST':
        form = AddOrdoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddOrdoForm()
    return render(request, 'zoowikipedia/create_ordo.html', {'form': form, 'menu': menu, 'title': 'Добавление отряда'})

# Удаление поста о классе
def delClassis(request, id):
    try:
        form = Classis.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Classis.DoesNotExist:
        return HttpResponseNotFound("<h2>Classis not found</h2>")

# Удаление поста об отряде
def delOrdo(request, id, classis_list_id):
    try:
        form = Ordo.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Ordo.DoesNotExist:
        return HttpResponseNotFound("<h2>Ordo not found</h2>")

# Редактирование поста о классе
def editClassis(request, id):
    try:
        form = Classis.objects.get(id=id)
        if request.method == "POST":
            form = AddClassisForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.save()
            return redirect('home')
        else:
            form = AddClassisForm(instance=form)
            return render(request, "classis_edit.html", {'form': form})
    except Classis.DoesNotExist:
        return HttpResponseNotFound("<h2>Classis not found</h2>")

# Редактирование поста об отряде
def editOrdo(request, id, classis_list_id):
    try:
        form = Ordo.objects.get(id=id)
        if request.method == "POST":
            form = AddOrdoForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.classis = request.POST.get("classis")
            form.save()
            return redirect('home')
        else:
            form = AddOrdoForm(instance=form)
            return render(request, "ordo_edit.html", {'form': form})
    except Classis.DoesNotExist:
        return HttpResponseNotFound("<h2>Ordo not found</h2>")

# Информационная страница "Страница не найдена"
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_classis(request, classis_post_id):
    post = get_object_or_404(Classis, pk=classis_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'classis_selected': post.pk,
    }
    return render(request, 'zoowikipedia/classis_post.html', context=context)

def list_ordo(request, classis_list_id):
    ordo = Ordo.objects.filter(classis_id=classis_list_id)

    context = {
        'ordo': ordo,
        'menu': menu,
        'title': 'Отображение по классам',
        'classis_selected': classis_list_id
    }
    return render(request, 'zoowikipedia/list_ordo.html', context=context)

# Показывает пост об отряде животных
def show_ordo(request, ordo_id, classis_id):
    post = get_object_or_404(Ordo, pk=ordo_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'ordo_selected': post.pk,
    }
    return render(request, 'zoowikipedia/ordo_post.html', context=context)

