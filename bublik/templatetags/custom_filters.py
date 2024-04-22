from django import template

register = template.Library()

@register.filter(name='to_float')
def to_float(value):
    """Преобразует значение в число с плавающей точкой."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

@register.filter(name='multiply')
def multiply(value, arg):
    """Умножает значение на аргумент."""
    return value * arg