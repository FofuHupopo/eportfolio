# Generated by Django 4.1.3 on 2022-11-20 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название класса')),
                ('students', models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='Ученики')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'db_table': 'core__class',
            },
        ),
    ]
