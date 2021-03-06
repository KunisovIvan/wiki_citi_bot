# Generated by Django 4.0.6 on 2022-07-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('href', models.CharField(max_length=120, verbose_name='Ссылка')),
                ('population', models.IntegerField(verbose_name='Население')),
                ('type', models.CharField(choices=[('Город', 'Citi'), ('Поселок городского типа', 'Pgt')], max_length=24, verbose_name='Тип населенного пункта')),
            ],
        ),
    ]
