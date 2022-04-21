from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *

class AddDrug(CreateView):
    form_class = RegisterDrugs
    template_name = 'drugs/adddrug.html'

class Drug(ListView):
    model = Drugs
    template_name = 'drugs/drug_catalog.html'
    context_object_name = 'model'

def sortcategory(request, category_slug):
    cat = Category.objects.filter(slug=category_slug)
    model = Drugs.objects.filter(category_id=cat[0].id)
    content = {
        'model': model,
    }
    return render(request,'drugs/drug_catalog.html', context=content)

def drug1(request, drug):
    model = Drugs.objects.filter(id=drug)
    content = {
        'model': model,
    }
    return render(request, 'drugs/drug_catalog.html', context=content)

class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'drugs/register.html'
    success_url = reverse_lazy('drug')
