from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from .models import Checkup, CheckupComponent, Department, Doctor,Service, Specialty, DoctorService, DoctorSpecialty


def main(request):
    """Главная страница с конкретными акциями"""
    # Получаем конкретные 5 акций для главной страницы
    featured_checkup_names = [
        'Боль в спине Расширенный',
        'Женское здоровье',
        'Репродуктивность',
        'Здоровый желудок',
        'Гастрологический'
    ]

    popular_checkups = []
    for name in featured_checkup_names:
        try:
            checkup = Checkup.objects.filter(name__icontains=name).first()
            if checkup:
                # Добавляем процент скидки
                if checkup.original_price > 0:
                    checkup.discount_percent = round(
                        ((checkup.original_price - checkup.discounted_price) / checkup.original_price) * 100)
                else:
                    checkup.discount_percent = 0
                popular_checkups.append(checkup)
        except:
            continue

    # Если не нашли нужные акции, берем первые 5
    if len(popular_checkups) < 5:
        all_checkups = Checkup.objects.all()[:5]
        for checkup in all_checkups:
            if checkup.original_price > 0:
                checkup.discount_percent = round(
                    ((checkup.original_price - checkup.discounted_price) / checkup.original_price) * 100)
            else:
                checkup.discount_percent = 0
        popular_checkups = list(all_checkups)

    # Получаем популярные отделения
    popular_departments = Department.objects.filter(
        name__in=[
            'Урология', 'Гинекология', 'Неврология',
            'Гастроэнтерология', 'Хирургия', 'Проктология'
        ]
    )
    departments_dict = {dept.name: dept for dept in popular_departments}

    context = {
        'title': 'MedKhan® - Главная',
        'departments_dict': departments_dict,
        'popular_checkups': popular_checkups,
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


def dynamic_checkup(request, checkup_id):
    """Динамическая страница акции"""
    checkup = get_object_or_404(Checkup, id=checkup_id)

    # Получаем компоненты чекапа
    components = CheckupComponent.objects.filter(checkup=checkup)

    # Группируем компоненты по категориям
    components_by_category = {}
    for component in components:
        category = component.category
        if category not in components_by_category:
            components_by_category[category] = []
        components_by_category[category].append(component)

    # Получаем врачей
    doctors = Doctor.objects.filter(
        doctorservice__service__checkupcomponent__checkup=checkup
    ).distinct()[:3]  # Ограничиваем до 3 врачей

    # Вычисляем процент скидки
    discount_percent = 0
    if checkup.original_price > 0:
        discount_percent = round(((checkup.original_price - checkup.discounted_price) / checkup.original_price) * 100)

    context = {
        'title': f'{checkup.name} - MedKhan®',
        'checkup': checkup,
        'components_by_category': components_by_category,
        'doctors': doctors,
        'discount_percent': discount_percent,
    }
    return render(request, 'products/BackPain.html', context)

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
    # Изменено: теперь разделяем по запятой
    advantages_list = []
    if service.advantages:
        advantages_list = [adv.strip() for adv in service.advantages.split(',') if adv.strip()]

    indications_list = []
    if service.indications:
        indications_list = [ind.strip() for ind in service.indications.split(',') if ind.strip()]

    contraindications_list = []
    if service.contraindications:
        contraindications_list = [contra.strip() for contra in service.contraindications.split(',') if contra.strip()]

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
    """Страница акций с фильтрацией и пагинацией"""
    gender_filter = request.GET.get('gender', '')
    page = int(request.GET.get('page', 1))

    # Базовый queryset
    all_checkups = Checkup.objects.all()

    # Фильтрация по полу (предполагаем, что есть поле gender в модели Checkup)
    if gender_filter == 'male':
        all_checkups = all_checkups.filter(gender='male')
    elif gender_filter == 'female':
        all_checkups = all_checkups.filter(gender='female')
    elif gender_filter == 'child':
        all_checkups = all_checkups.filter(gender='child')

    # Добавляем процент скидки ко всем акциям
    for checkup in all_checkups:
        if checkup.original_price > 0:
            checkup.discount_percent = round(
                ((checkup.original_price - checkup.discounted_price) / checkup.original_price) * 100)
        else:
            checkup.discount_percent = 0

    # Определяем количество акций для начального отображения с уникальным дизайном
    initial_display_count = 5  # 1 большая + 1 зеленая + 3 белых = 5

    # Акции для начального отображения (с уникальным дизайном)
    initial_checkups_display = all_checkups[:initial_display_count]

    # Остальные акции для пагинации
    remaining_checkups = all_checkups[initial_display_count:]

    # Пагинация остальных акций (по 6 штук за раз)
    paginator = Paginator(remaining_checkups, 6)
    paginated_remaining_checkups = paginator.get_page(page)

    # AJAX запрос для "Показать ещё"
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('products/partials/checkup_cards.html', {
            'checkups': paginated_remaining_checkups.object_list,
        })
        return JsonResponse({
            'html': html,
            'has_next': paginated_remaining_checkups.has_next(),
            'next_page': paginated_remaining_checkups.next_page_number() if paginated_remaining_checkups.has_next() else None
        })

    context = {
        'title': 'Акции - MedKhan®',
        'initial_checkups_display': initial_checkups_display,  # Передаем первые 5 акций
        'paginated_remaining_checkups': paginated_remaining_checkups,  # Передаем пагинированные остальные акции
        'has_next': paginated_remaining_checkups.has_next(),
        'next_page': paginated_remaining_checkups.next_page_number() if paginated_remaining_checkups.has_next() else None,
        'current_filter': gender_filter,
    }
    return render(request, 'products/stocks.html', context)
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