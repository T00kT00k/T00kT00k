from django import template
from ..models import *

register = template.Library()

# Передача параметров в html-шаблон через теги
# {% get_classis %} - передача всех параметров
# {% get_classis 1 %} - передача 1-ого параметра
@register.simple_tag(name='getclass')
def get_classis(filter=None):
   if not filter:
       return Classis.objects.all()
   else:
       return Classis.objects.filter(pk=filter)

@register.simple_tag(name='getordo')
def get_ordo(filter=None):
   if not filter:
       return Ordo.objects.all()
   else:
       return Ordo.objects.filter(pk=filter)

@register.simple_tag(name='getfam')
def get_familia(filter=None):
   if not filter:
       return Familia.objects.all()
   else:
       return Familia.objects.filter(pk=filter)

@register.simple_tag(name='getgen')
def get_genus(filter=None):
   if not filter:
       return Genus.objects.all()
   else:
       return Genus.objects.filter(pk=filter)

# Теги, с помощью которых можно возвращать фрагмент html-страницы
# {% show_classises %} - вывод фрагмента без изменений
# {% show_classises '-name' classis_selected %} - задается сортировка по имени в обратном порядке
@register.inclusion_tag('zoowikipedia/sidebar_list_classis.html')
def show_classises(sort=None, classis_selected=0):
   if not sort:
       classis = Classis.objects.all()
   else:
       classis = Classis.objects.order_by(sort)

   return {"classis": classis, "classis_selected": classis_selected}

@register.inclusion_tag('zoowikipedia/sidebar_list_ordo.html')
def show_ordoes(sort=None, ordo_selected=0):
   if not sort:
       ordo = Ordo.objects.all()
   else:
       ordo = Ordo.objects.order_by(sort)

   return {"ordo": ordo, "ordo_selected": ordo_selected}

@register.inclusion_tag('zoowikipedia/sidebar_list_familia.html')
def show_families(sort=None, familia_selected=0):
   if not sort:
       familia = Familia.objects.all()
   else:
       familia = Familia.objects.order_by(sort)

   return {"familia": familia, "familia_selected": familia_selected}

@register.inclusion_tag('zoowikipedia/sidebar_list_genus.html')
def show_genuses(sort=None, genus_selected=0):
   if not sort:
       genus = Genus.objects.all()
   else:
       genus = Genus.objects.order_by(sort)

   return {"genus": genus, "genus_selected": genus_selected}