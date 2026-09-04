from django.contrib import admin


from django.contrib import admin

from .models import (
    SiteSettings,
    PriceTable,
    PriceTableItem,
    WorkType
)

from .models import Category, Product
from django.urls import reverse
from django.utils.html import format_html


class PriceTableItemInline(admin.TabularInline):

    model = PriceTableItem
    extra = 1
    ordering = ['sort_order']
    fields = [
        'service',
        'unit',
        'price',
        'sort_order'
    ]

@admin.register(PriceTable)
class PriceTableAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'sort_order'
    ]
    ordering = ['sort_order']
    inlines = [PriceTableItemInline]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'is_active')
    list_filter = ('parent', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    # Добавляем inline для быстрого просмотра дочерних категорий (опционально)
    # fieldsets можно настроить под свои нужды


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'service_template', 'price', 'is_active')
    list_filter = ('category', 'is_active', 'service_template')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


class ProductInline(admin.TabularInline):
    model = Product
    fk_name = 'site_settings'   # указываем поле связи
    extra = 0
    fields = ('name', 'slug', 'category', 'image','price', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):


    fieldsets = (
        ( 'Основные', {'fields': ('site_name', 'default_phone', 'default_email', 'logo', 'favicon', 'hero_background',)}),
        ('SEO главной страницы',{ 'fields': (
            'homepage_title', 'homepage_description','homepage_keywords',)}),
        ('Статьи для главной страницы',{ 'fields': (
            'homepage_title_block_1','homepage_text_block_1', 'img_homepage_block_1', 'img_homepage_alt_block_1',
            'homepage_title_block_2', 'homepage_text_block_2', 'img_homepage_block_2','img_homepage_alt_block_2',
            'content_title_block_3', 'homepage_text_block_3', 'img_homepage_block_3','img_homepage_alt_block_3',
            ) }),
    )
    inlines = [ProductInline]


    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # Добавляем ссылки на управление категориями и товарами
        extra_context['catalog_links'] = {
            'categories': reverse('admin:core_category_changelist'),
            'products': reverse('admin:core_product_changelist'),
        }
        return super().change_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()




@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'sort_order',
        'is_published'
    )

    list_editable = (
        'sort_order',
        'is_published'
    )

    search_fields = (
        'title',
        'description'
    )




