from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tarefa, TarefaAdmin)