from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
ListView,DetailView, CreateView, UpdateView, DeleteView)

from . import models # . means look at current directory
# from django.http import HttpResponse

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchooListView(ListView):
    model = models.School
    # ListView takes the model called, 'School' in this case, lower case it and add list.returns school_list. But in this method, other people may not know what is returned here.

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    #DetailView return lower case of the model, in this case, 'school'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list") #when a entry is deleted successfully, show list page

class IndexView(TemplateView):
    template_name = 'index.html' #assuming the template is in templates folder

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION'
    #     return context

# def index(request):
#     return render(request, 'index.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CBV are cool")