from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drugs.urls'), name='drugs')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if not settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.STATIC_ROOT}),
#     ]