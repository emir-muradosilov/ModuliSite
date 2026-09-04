from django.db import models
from django.urls import reverse



class SiteSettings(models.Model):

    site_name = models.CharField( max_length=255, default='Производтво модульных зданий, блок контейнеров и металлоконструкций', verbose_name='Название сайта')
    default_phone = models.CharField( max_length=30, blank=True, verbose_name='Номер телефона на сайте')
    default_email = models.CharField( max_length=30, blank=True, verbose_name='email на сайте')
    logo = models.ImageField( upload_to='site/', blank=True, null=True, verbose_name='Логотип')
    favicon = models.ImageField( upload_to='site/', blank=True, null=True, verbose_name='favicon')

    homepage_title = models.CharField( max_length=255, blank=True, verbose_name='Tittle главной страницы' )
    homepage_description = models.TextField( blank=True, verbose_name='Description главной страницы')
    homepage_keywords = models.TextField(blank=True, verbose_name='Keywords главной страницы')
    hero_background = models.ImageField( upload_to='hero/', blank=True, null=True)

# block 1
    homepage_title_block_1 = models.CharField( blank=True, null=True, verbose_name='Заголовок блока 1')
    homepage_text_block_1 = models.TextField( blank=True, null=True, verbose_name='Текст блока 1')

    img_homepage_block_1 = models.ImageField(upload_to='portfolio/',blank=True,null=True, verbose_name='Img блока 1')
    img_homepage_alt_block_1 = models.CharField(max_length=255, null = True, verbose_name='Alt для Img блока 1')

# block 2
    homepage_title_block_2 = models.CharField( blank=True, null=True, verbose_name='Заголовок блока 2')
    homepage_text_block_2 = models.TextField( blank=True, null=True, verbose_name='Текст блока 2')

    img_homepage_block_2 = models.ImageField(upload_to='portfolio/',blank=True, null=True, verbose_name='Img блока 2')
    img_homepage_alt_block_2 = models.CharField(max_length=255, null = True, verbose_name='Alt для Img блока 2')

# block 3
    content_title_block_3 = models.CharField( blank=True, null=True, verbose_name='Заголовок блока 3')
    homepage_text_block_3 = models.TextField( blank=True, null=True, verbose_name='Текст блока 3')

    img_homepage_block_3 = models.ImageField(upload_to='portfolio/',blank=True, null=True, verbose_name='Img блока 3')
    img_homepage_alt_block_3 = models.CharField(max_length=255, null = True, verbose_name='Alt для Img блока 3')

    class Meta:
        verbose_name = 'Настройка сайта'          # единственное число
        verbose_name_plural = 'Настройки сайта'   # множественное
        db_table = 'site_settings'             # опционально: явное имя таблицы


    def __str__(self):
        return 'Настройки сайта'
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)



class PriceTable(models.Model):

    settings = models.ForeignKey( SiteSettings, on_delete=models.CASCADE, related_name='price_tables')
    title = models.CharField(max_length=255)
    service_column_name = models.CharField( max_length=100, default='Услуга')
    unit_column_name = models.CharField( max_length=100, default='Ед. изм.')
    price_column_name = models.CharField(max_length=100, default='Цена')
    sort_order = models.PositiveIntegerField( default=0)

    show_unit = models.BooleanField(default=True)
    show_price = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.title



class PriceTableItem(models.Model):

    table = models.ForeignKey( PriceTable, on_delete=models.CASCADE, related_name='items')
    service = models.CharField( max_length=255,)
    unit = models.CharField( max_length=100, blank=True, )
    price = models.CharField( max_length=100,)
    sort_order = models.PositiveIntegerField( default=0)




class WorkType(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    image = models.ImageField(
        upload_to='work-types/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    button_text = models.CharField(
        max_length=100,
        default='Оставить заявку',
        verbose_name='Текст кнопки'
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    class Meta:
        ordering = ['sort_order']
        verbose_name = 'Выполняемая работа'
        verbose_name_plural = 'Выполняемые работы'

    def __str__(self):
        return self.title





class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-ярлык")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name="Родительская категория"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category_detail', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название товара")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL-ярлык")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Категория"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Главное изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    service_template = models.ForeignKey(
        'pages.ServiceTemplate',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name="Шаблон услуги"
    )

    site_settings = models.ForeignKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        related_name='products',
        null=True,          # разрешаем товарам существовать без привязки
        blank=True,
        verbose_name='Настройки сайта'
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('product_detail', args=[self.category.slug, self.slug])
#        return reverse('catalog:product_detail', args=[self.category.slug, self.slug])
