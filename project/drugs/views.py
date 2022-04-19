from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


def drug(request):
    model=Drugs.objects.all()
    content={
        'model': model,
    }
    return render(request,'drugs/drug_catalog.html', context=content)

def sortcategory(request, category_slug):
    cat = Category.objects.filter(slug=category_slug)
    model = Drugs.objects.filter(category_id=cat[0].id)
    content = {
        'model': model,
    }
    return render(request,'drugs/drug_catalog.html', context=content)