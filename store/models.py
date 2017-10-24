from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.FloatField()
    PRODUCERS = (
    ('001', 'Samsung'),
    ('002', 'Sony'),
    ('003', 'Siemens'),
    ('004', 'Xiaomi'),
    ('005', 'Meizu'),
    ('006', 'Apple'),
    ('007', 'Noname'),
    ('008', 'Phillips'),
    ('009', 'CAT'),
    ('010', 'Frost'),
    ('011', 'Brown'),
    (None, 'unknown'),
    )
    producer = models.CharField(max_length=20, choices=PRODUCERS, default=None)
    CATEGORIES = (
    ('Компьютеры', (
            ('001', 'Ноутбуки'),
            ('002', 'Жесткие диски'),
            ('003', 'Мыши'),
            ('004', 'Клавы'),
            ('005', 'Флешки'),
            ('006', 'Память'),
            ('007', 'Моники'),
            ('008', 'Процессоры'),
            ('009', 'Видюхи'),
        )
    ),
    ('Электроника', (
            ('101', 'Мобильники'),
            ('102', 'Навушники'),
            ('103', 'Колонки'),
            ('104', 'Телеки'),
            ('105', 'Проэкторы'),
            ('106', 'Фотики'),
            ('107', 'Часы'),
            ('108', 'Электронные книги'),
            ('109', 'Гарнитуры'),
        )
    ),
    ('Бытовуха', (
            ('201', 'Обогреватели'),
            ('202', 'Увлажнители'),
            ('203', 'Холодильники'),
            ('204', 'Стиралки'),
            ('205', 'Плиты'),
            ('206', 'Чайники'),
            ('207', 'Блендеры'),
            ('208', 'Водонагреватели'),
            ('209', 'Пылесосы'),
        )
    ),
    ('Мебель', (
            ('301', 'Диваны'),
            ('302', 'Кресла'),
            ('303', 'Стулья'),
            ('304', 'Кровати'),
            ('305', 'Матрасы'),
            ('306', 'Шкафы'),
            ('307', 'Столы'),
            ('308', 'Комоды'),
            ('309', 'Кухни'),
            )
        ),
    ('Стройка', (
            ('301', 'Плитка'),
            ('302', 'Обои'),
            ('303', 'Радиаторы'),
            ('304', 'Смесители'),
            ('305', 'Линолеум'),
            ('306', 'Ванны'),
            ('307', 'Котлы'),
            ('308', 'Ламинат'),
            ('309', 'Дрели'),
            )
        ),
    ('Авто', (
            ('301', 'Шины'),
            ('302', 'Аккумуляторы'),
            ('303', 'Автомобили'),
            ('304', 'Масла'),
            ('305', 'Видеорегистраторы'),
            ('306', 'Магнитолы'),
            ('307', 'Акустика'),
            ('308', 'Мотоциклы'),
            ('309', 'Сигнализцаии'),
            )
        ),
        (None, 'Uncategorized')
    )

    category = models.CharField(max_length=20, choices=CATEGORIES, default=None)
    subcategory = models.CharField(max_length=20)
    available = models.BooleanField()
    image = models.FileField()

    def get_cats_by_group(gr, categories):
        cats = []
        for group in categories:
            if group[0] == gr:
                for item in group[1]:
                    cats.append(item[0])
                break
        return cats


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# class Article(models.Model):
#     title = models.CharField(max_length=20)
#     desc = models.TextField()
#     author_id = models.IntegerField()
#
#
#     def get_author_name(self):
#         return User.objects.get(pk=self.author_id).username
#
#
#     def __str__(self):
#         return self.title
