from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
