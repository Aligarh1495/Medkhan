from django.contrib import admin
from django.urls import path
from products.views import (
    main, services, stocks, specialists, AboutSenter, magazine, BackPain,
    patients, dynamic_department, dynamic_service, dynamic_checkup,
    submit_contact_request, quick_contact_request, dynamic_doctor_profile
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('services/', services, name='services'),
    path('stocks/', stocks, name='stocks'),

    # Динамические URL
    path('department/<int:department_id>/', dynamic_department, name='dynamic_department'),
    path('service/<int:service_id>/', dynamic_service, name='dynamic_service'),
    path('checkup/<int:checkup_id>/', dynamic_checkup, name='dynamic_checkup'),
    path('doctor/<int:doctor_id>/', dynamic_doctor_profile, name='dynamic_doctor_profile'),

    # API для заявок
    path('api/contact-request/', submit_contact_request, name='submit_contact_request'),
    path('api/quick-contact/', quick_contact_request, name='quick_contact_request'),
    path('submit-contact/', submit_contact_request, name='submit_contact_request'),

    # Остальные страницы (статические страницы врачей удалены)
    path('specialists/', specialists, name='specialists'),
    path('AboutSenter/', AboutSenter, name='AboutSenter'),
    path('magazine/', magazine, name='magazine'),
    path('BackPain/', BackPain, name='BackPain'),
    path('patients/', patients, name='patients'),
]
