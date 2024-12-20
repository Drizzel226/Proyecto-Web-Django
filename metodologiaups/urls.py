"""
URL configuration for metodologiaups project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),
    path('porque/', include('porque.urls')),
    path('MiniProyecto/', include('MiniProyecto.urls')),
    path('Kaizen/', include('Kaizen.urls')),
    path('HAPM/', include('HAPM.urls')),
    path('ORR/', include('ORR.urls')),


    path('visu5/', include('visu5.urls')),
    path('visuMini/', include('visuMini.urls')),
    path('visuKai/', include('visuKai.urls')),
    path('visuHAPM/', include('visuHAPM.urls')),
    path('visuORR/', include('visuORR.urls')),


    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
