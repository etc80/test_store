# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20171017_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Компьютеры', (('001', 'Ноутбуки'), ('002', 'Жесткие диски'), ('003', 'Мыши'), ('004', 'Клавы'), ('005', 'Флешки'), ('006', 'Память'), ('007', 'Моники'), ('008', 'Процессоры'), ('009', 'Видюхи'))), ('Электроника', (('101', 'Мобильники'), ('102', 'Навушники'), ('103', 'Колонки'), ('104', 'Телеки'), ('105', 'Проэкторы'), ('106', 'Фотики'), ('107', 'Часы'), ('108', 'Электронные книги'), ('109', 'Гарнитуры'))), ('Бытовуха', (('201', 'Обогреватели'), ('202', 'Увлажнители'), ('203', 'Холодильники'), ('204', 'Стиралки'), ('205', 'Плиты'), ('206', 'Чайники'), ('207', 'Блендеры'), ('208', 'Водонагреватели'), ('209', 'Пылесосы'))), ('Мебель', (('301', 'Диваны'), ('302', 'Кресла'), ('303', 'Стулья'), ('304', 'Кровати'), ('305', 'Матрасы'), ('306', 'Шкафы'), ('307', 'Столы'), ('308', 'Комоды'), ('309', 'Кухни'))), (None, 'Uncategorized')], default=None, max_length=20),
        ),
    ]