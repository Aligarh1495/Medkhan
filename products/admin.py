from django.contrib import admin
from .models import Department, Service, Doctor, Specialty, DoctorSpecialty, DoctorService, Checkup, CheckupComponent

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'cost', 'is_sedation_available')
    list_filter = ('department', 'is_sedation_available')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience_years', 'consultation_cost')

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DoctorSpecialty)
class DoctorSpecialtyAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'specialty')

@admin.register(DoctorService)
class DoctorServiceAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'service')

@admin.register(Checkup)
class CheckupAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'discounted_price')

@admin.register(CheckupComponent)
class CheckupComponentAdmin(admin.ModelAdmin):
    list_display = ('checkup', 'category', 'name', 'cost')
    list_filter = ('checkup', 'category')