from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('drugi/',Drug.as_view(), name='drug'),
    path('drugi/<int:drug>/', drug1, name="drugs"),
    path('drugi/<str:sort>/',Drug.as_view(), name='drugsort'),
    path('category/<slug:category_slug>/',SorttCategory.as_view(), name='category'),
    path('category/<slug:category_slug>/<str:sort>/',SorttCategory.as_view(), name='categorysort'),
    path('drugi/edit/drugi/<int:drug>/', edit, name='edit'),
    path('addpost/', AddDrug.as_view(), name='addpost'),
    path('login/', Log_in.as_view(), name='login'),
    path('logout/', logout_use, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('chat/', chat, name='chat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

