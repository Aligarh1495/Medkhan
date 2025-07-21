from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import (
    Department, Service, Doctor, Specialty, DoctorSpecialty,
    DoctorService, Checkup, CheckupComponent, ContactRequest
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'services_count')
    search_fields = ('name', 'description')

    def services_count(self, obj):
        return obj.services.count()

    services_count.short_description = 'Количество услуг'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'cost', 'is_sedation_available')
    list_filter = ('department', 'is_sedation_available')
    search_fields = ('name', 'description')
    list_editable = ('cost', 'is_sedation_available')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience_years', 'consultation_cost', 'category')
    search_fields = ('full_name', 'category')
    list_filter = ('category', 'experience_years')
    list_editable = ('consultation_cost',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctors_count')
    search_fields = ('name',)

    def doctors_count(self, obj):
        return obj.doctorspecialty_set.count()

    doctors_count.short_description = 'Количество врачей'


@admin.register(DoctorSpecialty)
class DoctorSpecialtyAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'specialty')
    list_filter = ('specialty',)
    search_fields = ('doctor__full_name', 'specialty__name')


@admin.register(DoctorService)
class DoctorServiceAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'service')
    list_filter = ('service__department',)
    search_fields = ('doctor__full_name', 'service__name')


@admin.register(Checkup)
class CheckupAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'discounted_price', 'discount_percent', 'gender')
    list_filter = ('gender',)
    search_fields = ('name', 'description')
    list_editable = ('original_price', 'discounted_price')

    def discount_percent(self, obj):
        if obj.original_price > 0:
            percent = ((obj.original_price - obj.discounted_price) / obj.original_price) * 100
            return f"{percent:.1f}%"
        return "0%"

    discount_percent.short_description = 'Скидка'


@admin.register(CheckupComponent)
class CheckupComponentAdmin(admin.ModelAdmin):
    list_display = ('checkup', 'category', 'name', 'cost')
    list_filter = ('checkup', 'category')
    search_fields = ('name', 'checkup__name')


# НОВЫЙ АДМИН ДЛЯ ЗАЯВОК
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at',)
