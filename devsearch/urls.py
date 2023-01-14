from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

# todo => now we are able to open image from site
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# todo => static file can be loaded in production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



