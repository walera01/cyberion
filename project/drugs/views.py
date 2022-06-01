from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db.models import Q


from .forms import *
from .models import *



def chat(request):
    return render(request, 'drugs/room.html')


class AddDrug(CreateView):
    form_class = RegisterDrugs
    template_name = 'drugs/adddrug.html'

class Drug(ListView):               #Главная страница и отображение по категориям
    model = Drugs
    template_name = 'drugs/drug_catalog.html'
    context_object_name = 'model'

    def get_queryset(self):
        if 'subcategory_slug' in self.kwargs.keys():
            print(self.kwargs)
            return Drugs.objects.filter(subcategory__slug=self.kwargs['subcategory_slug']).select_related('subcategory')
        elif 'category_slug' in self.kwargs.keys():
            print(self.kwargs)
            return Drugs.objects.filter(subcategory__category__slug=self.kwargs['category_slug']).select_related('subcategory')
        else:
            return Drugs.objects.all()

    def post(self, request, *args, **kwargs):

        if 'subcategory_slug' in self.kwargs.keys():
            print(self.kwargs)
            return Drugs.objects.filter(subcategory__slug=self.kwargs['subcategory_slug']).select_related('subcategory')
        elif 'category_slug' in self.kwargs.keys():
            print(self.kwargs)
            return Drugs.objects.filter(subcategory__category__slug=self.kwargs['category_slug']).select_related(
                'subcategory')
        else:
            model = Drugs.objects.all()
        return render(request,'drugs/drug_catalog.html', context=sort_prise(request, model ))


def sort_prise(request, model):                       # Поиск по цене
    context = {}
    if request.POST.get('search'):
        search = str(request.POST.get('search'))
        context.update({'search': search})
        model = Drugs.objects.filter( Q(name__icontains=request.POST.get('search')) | Q(description__icontains=request.POST.get('search')))
    max_prise = model.order_by('-prise')[0].prise
    min_prise = model.order_by('prise')[0].prise
    if request.POST.get('id1'):
        min_prise = float(request.POST.get('id1'))
        context.update({'min_prise': min_prise})

    if request.POST.get('id2'):
        max_prise = float(request.POST.get('id2'))
        context.update({'max_prise': max_prise})

    model = model.filter(prise__gte=min_prise).filter(prise__lte=max_prise)
    context.update({'model': model})
    return context

def edit(request, drug):
    model = Drugs.objects.get(id=drug)
    if request.method != 'POST':
        form = RegisterDrugs(instance=model)
    else:
        form = RegisterDrugs(instance=model, data=request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'drugs/adddrug.html', context=context)

class Product(ListView):
    model = Drugs.objects.all()
    template_name = 'drugs/fulldescription.html'
    context_object_name = 'model'

    def get_queryset(self):
        print(self.kwargs['drug'])
        return Drugs.objects.filter(id=self.kwargs['drug'])



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



# def sortcategory(request, category_slug):
#     cat = Category.objects.filter(slug=category_slug)
#     model = Drugs.objects.filter(category_id=cat[0].id)
#     content = {
#         'model': model,
#     }
#     return render(request,'drugs/drug_catalog.html', context=content)
