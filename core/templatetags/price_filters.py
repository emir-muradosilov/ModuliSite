from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def format_price(value):
    """
    Форматирует число как цену:
    - разделитель тысяч — пробел
    - десятичный разделитель — запятая
    - всегда два знака после запятой
    """
    if value is None:
        return "0,00"
    try:
        # Преобразуем в Decimal, чтобы точно контролировать формат
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        # Целая часть и дробная часть
        integer_part = int(value)
        fractional_part = f"{value % 1:.2f}".split('.')[1]  # два знака
        # Форматируем целую часть с пробелами
        formatted_integer = f"{integer_part:,}".replace(',', ' ')
        return f"{formatted_integer},{fractional_part}"
    except (ValueError, TypeError):
        return str(value)