from django.urls import path, re_path

from .views import *

urlpatterns = [
    # Стартовая страница
    path('', index, name='home'),
    # Страница о сайте
    path('about/', about, name='about'),
    # Страница для добавления новой информации
    path('addpage/', addpage, name='add_page'),
    # Страница с контактами
    path('contact/', contact, name='contact'),
    # Страница авторизации
    path('login/', login, name='login'),
    # Страница с постом, открытым на главной странице
    path('classis_post/<int:classis_post_id>/', show_classis, name='classis_post'),
    # Отряды выбранного в левом сайдбаре класса
    path('classis_list/<int:classis_list_id>/', list_ordo, name='classis_list'),
    # Страница с постом выбранного отряда
    path('classis_list/<int:classis_id>/ordo_post/<int:ordo_id>/', show_ordo, name='ordo_post'),
]

