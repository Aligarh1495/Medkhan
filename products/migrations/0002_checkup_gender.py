# Generated by Django 4.2.23 on 2025-07-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkup',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский'), ('child', 'Ребёнок')], help_text='Пол, для которого предназначен чекап (мужской, женский, ребёнок)', max_length=10, null=True),
        ),
    ]
