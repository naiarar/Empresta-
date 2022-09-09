from django.contrib import admin
from django.urls import path, include

import usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    

]
