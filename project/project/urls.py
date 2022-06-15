from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drugs.urls'), name='drugs')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
#
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.views.static import serve as mediaserve
from django.conf.urls import url


urlpatterns += [
    url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root': settings.MEDIA_ROOT}),
    url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root': settings.STATIC_ROOT}),
]