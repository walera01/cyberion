from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('drug')

class Log_in(LoginView):
    form_class = LoginUserForm
    template_name = 'drugs/log_in.html'

    def get_success_url(self):
        return reverse_lazy('drug')

def logout_use(request):
    logout(request)
    return redirect('login')