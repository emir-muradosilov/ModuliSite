from django.db import models
from slugify import slugify
# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Название города')
    name_where = models.CharField(max_length=100, unique=True, verbose_name='Название города - где?')
    name_oblast = models.CharField(max_length=100, unique=True, verbose_name='Название области')
    name_oblast_where = models.CharField(max_length=100, unique=True, verbose_name='Название области - где?')

    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Slug')
#    subdomain = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True, verbose_name='Город активен?')
    is_rented = models.BooleanField(default=False, verbose_name='Город сдан в аренду?')

    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес офиса')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='email')
    price_text = models.CharField(max_length=255, blank=True, null=True, verbose_name='Стоимость')

    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Title главной страницы')
    seo_description = models.TextField(blank=True, null=True, verbose_name='Description главной страницы')
    seo_keywords = models.TextField(blank=True, null=True, verbose_name='Keywords главной страницы')

    h1_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='H1 Заголовок главной страницы')

    rent_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rented_until = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True)

    page_score = models.IntegerField(default=0)

    is_main = models.BooleanField(default=False,verbose_name='Главный город')

# Блок 1
    choose_as_h2 = models.TextField( blank=True, null=True, verbose_name='Заголовок текста 1')
    choose_as = models.TextField( blank=True, null=True, verbose_name='Текст 1')
    img_choose_as = models.ImageField(upload_to='portfolio/',blank=True,null=True, verbose_name='Изображение 1')
    img_choose_as_alt = models.CharField(max_length=255, null=True, verbose_name='Alt Изображения 1')

# Блок 2
    useful_h2 = models.TextField( blank=True, null=True, verbose_name='Заголовок текста 2')
    useful = models.TextField( blank=True, null=True, verbose_name='Текст 2')
    img_useful = models.ImageField(upload_to='portfolio/',blank=True,null=True, verbose_name='Изображение 2')
    img_useful_alt = models.CharField(max_length=255, null=True, verbose_name='Alt Изображения 2')

# Блок 3
    homepage_text_h2 = models.TextField( blank=True, null=True, verbose_name='Заголовок текста 3')
    homepage_text = models.TextField( blank=True, null=True, verbose_name='Текст 3')
    homepage_text_img = models.ImageField(upload_to='portfolio/',blank=True,null=True, verbose_name='Изображение 3')
    homepage_text_img_alt = models.CharField(max_length=255, null=True, verbose_name='Alt Изображения 3')

# Блок 4
    homepage_advantages_h2 = models.TextField( blank=True, null=True, verbose_name='Заголовок текста 4')
    homepage_advantages = models.TextField( blank=True, null=True, verbose_name='Текст 4')



    def get_absolute_url(self):

        if self.is_main:
            return '/'

        return f'/{self.slug}/'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def in_city(self):
        return self.name_where


    @property
    def oblast(self):
        return self.name_oblast


    @property
    def in_oblast(self):
        return self.name_oblast_where



    class Meta:

        verbose_name = "Города"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name

