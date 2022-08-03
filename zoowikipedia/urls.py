from django.urls import path, re_path

from .views import *

urlpatterns = [
    # Стартовая страница
    path('', index, name='home'),

    # Страница о сайте
    path('about/', about, name='about'),

    # Страница выбора объекта
    path('action_page/', actionPage, name='action_page'),

    # Страница для добавления нового класса
    path('create_classis/', addClassis, name='create_classis'),

    # Страница для добавления нового отряда
    path('create_ordo/', addOrdo, name='create_ordo'),

    # Удаление поста про класс
    path('delete_classis/<int:id>/', delClassis),

    # Удаление поста про отряд
    path('classis_list/<int:classis_list_id>/delete_ordo/<int:id>/', delOrdo),

    # Редактирование поста про класс
    path('edit_classis/<int:id>/', editClassis),

    # Редактирование поста про отряд
    path('classis_list/<int:classis_list_id>/edit_ordo/<int:id>/', editOrdo),

    # Страница с постом, открытым на главной странице
    path('classis_post/<int:classis_post_id>/', show_classis, name='classis_post'),

    # Отряды выбранного в левом сайдбаре класса
    path('classis_list/<int:classis_list_id>/', list_ordo, name='classis_list'),

    # Страница с постом выбранного отряда
    path('classis_list/<int:classis_id>/ordo_post/<int:ordo_id>/', show_ordo, name='ordo_post'),
]