
from django.contrib import admin
from django.urls import path

from products.views import main, services, stocks, specialists, AboutSenter, magazine, HanYmar, BackPain, \
    RestorativeMedicene, cosmetic, patients,HanTulpan,NudelmanNatalia,BasharovaAlena, Uldashev

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
    path('patients/', patients, name='patients'),
    path('HanTulpan/',HanTulpan,name='HanTulpan'),
    path('NudelmanNatalia/',NudelmanNatalia,name='NudelmanNatalia'),
    path('BasharovaAlenf/',BasharovaAlena,name='BasharovaAlena'),
    path('Uldashev/',Uldashev,name='Uldashev')
]
