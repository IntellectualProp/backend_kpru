from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django/admin/', admin.site.urls),  # Admin panel under /django/admin/
    path('django/api', include("api.urls")),  # Your app under /django/
    path('django/', include("myapp.urls")),  # Your app under /django/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
