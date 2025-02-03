from django import template

register = template.Library()

@register.filter(name='celsius_to_fahrenheit')
def celsius_to_fahrenheit(celsius):
    try:
        fahrenheit = float(celsius) * 1.8 + 32
        return int(round(fahrenheit))
    except (ValueError, TypeError):
        return ''
