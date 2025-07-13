from django.db import models

# Информацию об отделениях клиники (эндоскопия, гинекология, хирургия и т.д.)
class Department(models.Model):
    name = models.CharField(max_length=128)
    # slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# O медицинских процедурах и услугах.
class Service(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=256)
    # slug = models.SlugField(blank=True)
    description = models.TextField()
    advantages = models.TextField()
    indications = models.TextField()
    contraindications = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_sedation_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    full_name = models.CharField(max_length=128)
    experience_years = models.IntegerField()
    consultation_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    profile_treatment = models.TextField()
    work_experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.full_name

# Cпециальности врачей (например, "Эндоскопист", "Гинеколог", "Хирург")
class Specialty(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
# Связывает врачей с их специальностями
class DoctorSpecialty(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

# Связывает врачей с услугами, которые они предоставляют
class DoctorService(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

# О комплексных чекапах
class Checkup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    girls_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

# Элементы чекапа (лабораторные анализы, инструментальная диагностика, консультации).
class CheckupComponent(models.Model):
    checkup = models.ForeignKey(Checkup, on_delete=models.CASCADE, related_name='components')
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.name}"