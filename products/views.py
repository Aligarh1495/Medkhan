from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    context = {
        'title': 'MedKhan® - Главная',
    }
    return render(request,'products/main.html',context)
def services(request):
    context = {
        'title': 'Услуги - MedKhan®',
        'products': [
            {
                'image': '/static/images/telik.png',
                'name': 'Диагностика',
            },
            {
                'image': '/static/images/tabls.png',
                'name': 'Общая медицина',
            },
            {
                'image': '/static/images/plus.png',
                'name': 'Восстановительная медицина',
            },
            {
                'image': '/static/images/smile.png',
                'name': 'Лицо и тело',
            },
            {
                'image': '/static/images/baby.png',
                'name': 'Медицина для детей',
            },
            {
                'image': '/static/images/ножницы_1.png',
                'name': 'Хирургия',
            },
        ]
    }
    return render(request,'products/services.html',context)
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