from django import template

register = template.Library()


@register.filter
def split_by_newline(value):
    """
    Разбивает строку на список строк по символу новой строки,
    удаляя пустые строки и пробелы по краям.
    """
    if not isinstance(value, str):
        return []
    return [line.strip() for line in value.split('\n') if line.strip()]


@register.filter
def parse_education_timeline(value):
    """
    Разбивает строку образования на список словарей,
    где каждый словарь содержит 'year' и 'description'.
    Ожидаемый формат: 'ГОД - Описание'
    """
    if not isinstance(value, str):
        return []

    items = []
    for line in value.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Пытаемся найти первый дефис, чтобы разделить год и описание
        parts = line.split(' - ', 1)
        if len(parts) == 2:
            year = parts[0].strip()
            description = parts[1].strip()
            items.append({'year': year, 'description': description})
        else:
            # Если формат не соответствует, просто используем всю строку как описание
            items.append({'year': '', 'description': line})
    return items
