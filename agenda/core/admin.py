from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoaAdmin():
    list_display = ('tituto', 'data_evento', 'data_criacao')
    list_filter = ('titulo')
admin.site.register(Evento)
