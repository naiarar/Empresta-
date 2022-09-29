from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from index.views import index

import usuarios

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.CSS_URL, document_root=settings.CSS_ROOT)
