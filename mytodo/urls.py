from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import forms


urlpatterns = [
    path('', TemplateView.as_view(template_name="mytodo/index.html"), name='mytodo.index'),

    # LOGIN
    path(
        'login', auth_views.LoginView.as_view(
            template_name='mytodo/login.html',
            authentication_form=forms.LoginForm,
        ), name='mytodo.login'),
    path(
        'login/success', TemplateView.as_view(
            template_name='mytodo/login_success.html',
        ), name='mytodo.login_success'),

    # GET STARTED
    path('getstarted', TemplateView.as_view(template_name="mytodo/getstarted.html"), name='mytodo.getstarted'),
    path('basic_form', views.BasicFormView.as_view(), name='mytodo.basic_form'),
    path('simple_form', views.SimpleFormView.as_view(), name='mytodo.simple_form'),

    # CRUD
    path('tarefa/list', views.TarefaListView.as_view(), name="mytodo.tarefa.list"),
    path('tarefa/create', views.TarefaCreateView.as_view(), name="mytodo.tarefa.create"),
    path('tarefa/update/<pk>', views.TarefaUpdateView.as_view(), name='mytodo.tarefa.update'),
    path('tarefa/delete/<pk>', views.TarefaDeleteView.as_view(), name='mytodo.tarefa.delete'),

    # SERVICE
    path('tarefa/done/<pk>', views.TarefaDoneView.as_view(), name='mytodo.tarefa.done'),

]
