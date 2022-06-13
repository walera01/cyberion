from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('drugi/',Drug.as_view(), name='drug'),                                 #все товары
    path('drugi/find/',cache_page(100)(Drug.as_view()), name='drugfind'),                       #поиск и поиск по цене
    path('category/<slug:category_slug>/find/',Drug.as_view(), name='catfind'),
    path('subcategory/<slug:subcategory_slug>/find/',Drug.as_view(), name='subcatfind'),

    path('drugi/<int:drug>/', Product.as_view(), name="drugs"),
    # path('drugi/<str:sort>/',Drug.as_view(), name='drugsort'),
    path('category/<slug:category_slug>/',Drug.as_view(), name='category'),             ## Вывод по категориям
    path('subcategory/<slug:subcategory_slug>/',Drug.as_view(), name='subcategory'),       ## Вывод по подкатегориям
    path('category/<slug:category_slug>/<str:sort>/',Drug.as_view(), name='categorysort'),
    re_path(r'drugi/(?P<drug>\d+)/edit$', edit, name='edit'),
    path('addpost/', AddDrug.as_view(), name='addpost'),
    path('login/', Log_in.as_view(), name='login'),
    path('logout/', logout_use, name='logout'),
    path('register/', Register.as_view(), name='register'),
    # path('chat/', chat, name='chat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

