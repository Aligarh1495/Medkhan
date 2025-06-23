"""
URL configuration for Medkhan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from products.views import main, services, stocks, specialists, AboutSenter, magazine, HanYmar, BackPain, \
    RestorativeMedicene, cosmetic, patients

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('services/', services, name='services'),
    path('stocks/', stocks,name='stocks'),
    path('specialists/', specialists,name='specialists'),
    path('AboutSenter/', AboutSenter, name='AboutSenter'),
    path('magazine/', magazine,name='magazine'),
    path('HanYmar/', HanYmar, name='HanYmar'),
    path('BackPain/', BackPain, name='BackPain'),
    path('RestorativeMedicene/',RestorativeMedicene,name='RestorativeMedicene'),
    path('cosmetic/', cosmetic, name='cosmetic'),
    path('patients/', patients, name='patients')
]
