from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('drugi/',Drug.as_view(), name='drug'),
    path('category/<slug:category_slug>/',sortcategory, name='category'),
    path('drugi/<int:drug>/', drug1, name="drugs"),
    path('addpost/', AddDrug.as_view(), name='addpost'),
    path('login/', Log_in.as_view(), name='login'),
    path('logout/', logout_use, name='logout'),
    path('register/', Register.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
