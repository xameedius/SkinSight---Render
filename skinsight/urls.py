from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("predictor.urls")),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Render prod: still serve media through Django (works, but not ideal for large scale)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)