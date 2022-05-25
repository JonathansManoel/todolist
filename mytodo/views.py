from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse

from .models import Tarefa
from .forms import TarefaModelForm, BasicForm, SimpleForm
from .services import tarefa_service


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class BasicFormView(FormView):
    template_name = 'mytodo/basic_form.html'
    form_class = BasicForm


class SimpleFormView(FormView):
    template_name = 'mytodo/simple_form.html'
    form_class = SimpleForm


class TarefaListView(ListView):

    model = Tarefa
    paginate_by = '100'
    context_object_name = 'tarefa_list'
    template_name = 'mytodo/tarefa_list.html'

    def get_context_data(self, **kwargs):
        context = super(TarefaListView, self).get_context_data(**kwargs)
        project = self.request.GET.get('project')
        context['project'] = project
        return context

    def get_queryset(self):
        project = self.request.GET.get('project')
        if not project:
            return Tarefa.objects.all()
        return Tarefa.objects.filter(project=project)


class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaModelForm
    context_object_name = 'tarefa'
    template_name = 'mytodo/tarefa_form.html'

    def get_success_url(self):
        return reverse("mytodo.tarefa.list")


class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaModelForm
    context_object_name = 'tarefa'
    template_name = 'mytodo/tarefa_form.html'

    def get_success_url(self):
        return reverse("mytodo.tarefa.list")

class TarefaDeleteView(DeleteView):
    model = Tarefa
    form_class = TarefaModelForm
    context_object_name = 'tarefa'
    template_name = 'mytodo/tarefa_delete_form.html'

    def get_success_url(self):
        return reverse("mytodo.tarefa.list")



class TarefaDoneView(View):

    def get(self, request, *args, **kwargs):
        tarefa_service.mark_as_done(self.kwargs.get('pk'))
        return redirect(reverse("mytodo.tarefa.list"))
