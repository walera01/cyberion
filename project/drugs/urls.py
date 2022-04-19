from django.urls import path, include
from .views import *

urlpatterns = [
    path('drugi/',drug, name='drugs'),
    path('category/<slug:category_slug>/',sortcategory, name='category')
]
