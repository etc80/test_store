# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20171019_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default='img/placeholder.png', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Компьютеры', (('001', 'Ноутбуки'), ('002', 'Жесткие диски'), ('003', 'Мыши'), ('004', 'Клавы'), ('005', 'Флешки'), ('006', 'Память'), ('007', 'Моники'), ('008', 'Процессоры'), ('009', 'Видюхи'))), ('Электроника', (('101', 'Мобильники'), ('102', 'Навушники'), ('103', 'Колонки'), ('104', 'Телеки'), ('105', 'Проэкторы'), ('106', 'Фотики'), ('107', 'Часы'), ('108', 'Электронные книги'), ('109', 'Гарнитуры'))), ('Бытовуха', (('201', 'Обогреватели'), ('202', 'Увлажнители'), ('203', 'Холодильники'), ('204', 'Стиралки'), ('205', 'Плиты'), ('206', 'Чайники'), ('207', 'Блендеры'), ('208', 'Водонагреватели'), ('209', 'Пылесосы'))), ('Мебель', (('301', 'Диваны'), ('302', 'Кресла'), ('303', 'Стулья'), ('304', 'Кровати'), ('305', 'Матрасы'), ('306', 'Шкафы'), ('307', 'Столы'), ('308', 'Комоды'), ('309', 'Кухни'))), ('Стройка', (('301', 'Плитка'), ('302', 'Обои'), ('303', 'Радиаторы'), ('304', 'Смесители'), ('305', 'Линолеум'), ('306', 'Ванны'), ('307', 'Котлы'), ('308', 'Ламинат'), ('309', 'Дрели'))), ('Авто', (('301', 'Шины'), ('302', 'Аккумуляторы'), ('303', 'Автомобили'), ('304', 'Масла'), ('305', 'Видеорегистраторы'), ('306', 'Магнитолы'), ('307', 'Акустика'), ('308', 'Мотоциклы'), ('309', 'Сигнализцаии'))), (None, 'Uncategorized')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('001', 'Samsung'), ('002', 'Sony'), ('003', 'Siemens'), ('004', 'Xiaomi'), ('005', 'Meizu'), ('006', 'Apple'), ('007', 'Noname'), ('008', 'Phillips'), ('009', 'CAT'), ('010', 'Frost'), ('011', 'Brown'), (None, 'unknown')], default=None, max_length=20),
        ),
    ]
