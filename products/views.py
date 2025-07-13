from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Department, Service, Doctor, Specialty, DoctorSpecialty, DoctorService, Checkup, CheckupComponent


def main(request):
    # Получаем популярные отделения для главной страницы
    popular_departments = Department.objects.filter(
        name__in=[
            'Урология', 'Гинекология', 'Неврология',
            'Гастроэнтерология', 'Хирургия', 'Проктология'
        ]
    )

    # Создаем словарь для быстрого поиска отделений по названию
    departments_dict = {dept.name: dept for dept in popular_departments}

    context = {
        'title': 'MedKhan® - Главная',
        'departments_dict': departments_dict,
    }
    return render(request, 'products/main.html', context)


def services(request):
    departments = Department.objects.prefetch_related('services').all()

    products = []
    for department in departments:
        department_services = department.services.all()
        if department_services.exists():
            products.append({
                'image': f'/static/images/{department.name.lower()}.png',
                'name': department.name,
                'description': department.description,
                'services_count': department_services.count(),
                'department_id': department.id  # Добавляем ID отделения
            })

    context = {
        'title': 'Услуги - MedKhan®',
        'products': products,
        'departments': departments,
    }
    return render(request, 'products/services.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Department, Service, Doctor, Specialty, DoctorSpecialty, DoctorService, Checkup, CheckupComponent


# Все ваши существующие функции остаются без изменений...

def dynamic_department(request, department_id):
    """Динамическая страница отделения - использует шаблон RestorativeMedicene.html"""
    department = get_object_or_404(Department, id=department_id)
    services_list = Service.objects.filter(department=department)

    # Получаем врачей этого отделения через DoctorService
    doctors = Doctor.objects.filter(doctorservice__service__department=department).distinct()

    context = {
        'title': f'{department.name} - MedKhan®',
        'department': department,
        'services': services_list,
        'doctors': doctors,
    }
    return render(request, 'products/RestorativeMedicene.html', context)


def dynamic_service(request, service_id):
    """Динамическая страница услуги - использует шаблон cosmetic.html"""
    service = get_object_or_404(Service, id=service_id)

    # Получаем врачей, которые предоставляют эту услугу через DoctorService
    doctors = Doctor.objects.filter(doctorservice__service=service).distinct()

    # Парсим преимущества, показания и противопоказания
    advantages_list = []
    if service.advantages:
        advantages_list = [adv.strip() for adv in service.advantages.split('\n') if adv.strip()]

    indications_list = []
    if service.indications:
        indications_list = [ind.strip() for ind in service.indications.split('\n') if ind.strip()]

    contraindications_list = []
    if service.contraindications:
        contraindications_list = [contra.strip() for contra in service.contraindications.split('\n') if contra.strip()]

    context = {
        'title': f'{service.name} - MedKhan®',
        'service': service,
        'department': service.department,
        'doctors': doctors,
        'advantages_list': advantages_list,
        'indications_list': indications_list,
        'contraindications_list': contraindications_list,
    }
    return render(request, 'products/cosmetic.html', context)
def stocks(request):
    context = {
        'title': 'Акции - MedKhan®'
    }
    return render(request,'products/stocks.html',context)
def specialists(request):
    context = {
        'title': 'Специалисты - MedKhan®'
    }
    return render(request,'products/specialists.html',context)
def AboutSenter(request):
    context = {
        'title': 'О Центре - MedKhan®'
    }
    return render(request,'products/AboutSenter.html',context)
def magazine(request):
    context = {
        'title': 'Журнал О Здоровье - MedKhan®'
    }
    return render(request,'products/magazine.html',context)
def HanYmar(request):
    context = {
        'title': 'Хан Умар Хаят - Главный врач, уролог-андролог - MedKhan®'
    }
    return render(request,'products/HanYmar.html',context)
def BackPain(request):
    context = {
        'title' : 'CHECK UP «Боль в спине Расширенный» - MedKhan®'
    }
    return render(request, 'products/BackPain.html',context)
def RestorativeMedicene(request):
    context = {
        'title' : 'Восстановительная медицина - MedKhan®'
    }
    return render(request,'products/RestorativeMedicene.html',context)
def cosmetic(request):
    context = {
        'title' : 'Косметология - MedKhan®'
    }
    return render(request,'products/cosmetic.html', context)
def patients(request):
    context = {
        'title': 'Пациентам - MedKhan®'
    }
    return render(request,'products/patients.html',context)
def HanTulpan(request):
    context = {
        'title': 'Хан Тюльпан Тимергалиевна - Гинеколог врач УЗИ - MedKhan®'
    }
    return render(request,'products/HanTulpan.html',context)
def NudelmanNatalia(request):
    context = {
        'title': 'Нудельман Наталия Федоровна - Невролог - MedKhan®'
    }
    return render(request,'products/NudelmanNatalia.html',context)
def BasharovaAlena(request):
    context = {
        'title': 'Башарова Альбина Шарипзяновна - Кардиолог врач УЗИ терапевт - MedKhan®'
    }
    return render(request,'products/BasharovaAlena.html',context)
def Uldashev(request):
    context = {
        'title': 'Юлдашев Фарход Талибович - Проктолог - MedKhan®'
    }
    return render(request,'products/Uldashev.html',context)