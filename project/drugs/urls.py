from django.urls import path, include
from .views import *

urlpatterns = [
    path('drugi/',Drug.as_view(), name='drug'),
    path('category/<slug:category_slug>/',sortcategory, name='category'),
    path('drugi/<int:drug>/', drug1, name="drugs"),
    path('addpost/', AddDrug.as_view(), name='addpost'),
]
