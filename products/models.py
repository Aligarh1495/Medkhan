from django.db import models

from django.utils import timezone





# Информацию об отделениях клиники (эндоскопия, гинекология, хирургия и т.д.)

class Department(models.Model):

    name = models.CharField(max_length=128)

    description = models.TextField(blank=True)



    def __str__(self):

        return self.name





# O медицинских процедурах и услугах.

class Service(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='services')

    name = models.CharField(max_length=256)

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

    # НОВЫЕ ПОЛЯ

    image = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Фотография врача")

    online_booking_link = models.URLField(max_length=500, null=True, blank=True, help_text="Ссылка на онлайн-запись к врачу")





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

    GENDER_CHOICES = [

        ('male', 'Мужской'),

        ('female', 'Женский'),

        ('child', 'Ребёнок'),

    ]



    name = models.CharField(max_length=256)

    description = models.TextField()

    original_price = models.DecimalField(max_digits=10, decimal_places=2)

    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)

    girls_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    gender = models.CharField(

        max_length=10,

        choices=GENDER_CHOICES,

        null=True,

        blank=True,

        help_text="Пол, для которого предназначен чекап (мужской, женский, ребёнок)"

    )



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





# НОВАЯ МОДЕЛЬ: Заявки от пользователей

class ContactRequest(models.Model):

    STATUS_CHOICES = [

        ('new', 'Новая'),

        ('in_progress', 'В обработке'),

        ('completed', 'Завершена'),

        ('cancelled', 'Отменена'),

    ]



    SOURCE_CHOICES = [

        ('stocks_page', 'Страница акций'),

        ('services_page', 'Страница услуг'),

        ('main_page', 'Главная страница'),

        ('specialists_page', 'Страница специалистов'),

        ('checkup_page', 'Страница чекапа'),

        ('other', 'Другое'),

    ]



    # Основная информация

    name = models.CharField(

        max_length=100,

        verbose_name="Имя",

        help_text="Как вас зовут?"

    )

    phone = models.CharField(

        max_length=20,

        verbose_name="Номер телефона",

        help_text="Ваш номер телефона"

    )



    # Дополнительная информация

    email = models.EmailField(

        blank=True,

        null=True,

        verbose_name="Email",

        help_text="Электронная почта (необязательно)"

    )

    message = models.TextField(

        blank=True,

        null=True,

        verbose_name="Сообщение",

        help_text="Дополнительная информация или вопросы"

    )



    # Метаданные заявки

    source_page = models.CharField(

        max_length=20,

        choices=SOURCE_CHOICES,

        default='other',

        verbose_name="Источник заявки",

        help_text="С какой страницы была отправлена заявка"

    )



    # Связанные объекты (опционально)

    related_checkup = models.ForeignKey(

        Checkup,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        verbose_name="Связанный чекап",

        help_text="Чекап, по которому была отправлена заявка"

    )

    related_service = models.ForeignKey(

        Service,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        verbose_name="Связанная услуга",

        help_text="Услуга, по которой была отправлена заявка"

    )

    related_doctor = models.ForeignKey(

        Doctor,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        verbose_name="Связанный врач",

        help_text="Врач, к которому хотят записаться"

    )



    # Статус и временные метки

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='new',

        verbose_name="Статус заявки"

    )

    created_at = models.DateTimeField(

        auto_now_add=True,

        verbose_name="Дата создания"

    )

    updated_at = models.DateTimeField(

        auto_now=True,

        verbose_name="Дата обновления"

    )



    # Технические поля

    ip_address = models.GenericIPAddressField(

        null=True,

        blank=True,

        verbose_name="IP адрес",

        help_text="IP адрес пользователя"

    )

    user_agent = models.TextField(

        blank=True,

        null=True,

        verbose_name="User Agent",

        help_text="Информация о браузере пользователя"

    )



    class Meta:

        verbose_name = "Заявка"

        verbose_name_plural = "Заявки"

        ordering = ['-created_at']

        indexes = [

            models.Index(fields=['created_at']),

            models.Index(fields=['status']),

            models.Index(fields=['phone']),

        ]



    def __str__(self):

        return f"Заявка от {self.name} ({self.phone}) - {self.get_status_display()}"



    def get_absolute_url(self):

        return f"/admin/products/contactrequest/{self.id}/"



    @property

    def is_new(self):

        return self.status == 'new'



    @property

    def days_since_created(self):

        return (timezone.now() - self.created_at).days
