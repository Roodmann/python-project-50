def format_removed(diff, patch):
    property_path = '.'.join(patch + [diff['key']])
    return f"Property '{property_path}' was removed"


def format_added(diff, patch):
    property_path = '.'.join(patch + [diff['key']])
    new_value = format_value(diff['new_value'])
    return (f"Property '{property_path}'"
            f" was added with value: {new_value}"
            )


def format_updated(diff, patch):
    property_path = '.'.join(patch + [diff['key']])
    old_value = format_value(diff['old_value'])
    new_value = format_value(diff['new_value'])
    return (f"Property '{property_path}'"
            f" was updated. From {old_value} to {new_value}"
            )


def format_nested(diff, patch):
    nested_diffs = diff['nested']
    return walk(nested_diffs, patch=patch + [diff['key']])


def walk(diffs, patch=[]):
    """Рекурсия, формирует соответствующее
       действие для каждого элемента.
    """
    formatted_diffs = []

    for diff in diffs:
        status = diff['status']
        if status == 'removed':
            formatted_diffs.append(format_removed(diff, patch))

        elif status == 'added':
            formatted_diffs.append(format_added(diff, patch))

        elif status == 'nested':
            formatted_diffs.extend(format_nested(diff, patch))

        elif status == 'updated':
            formatted_diffs.append(format_updated(diff, patch))

    return formatted_diffs


def format_plain(diffs):
    """Преобразует разницу в форматированный текст."""
    formatted_diffs = walk(diffs)
    return '\n'.join(formatted_diffs)


def format_value(value):
    """Преобразует значения в определенный формат."""
    if isinstance(value, str):
        return "'" + str(value) + "'"

    elif isinstance(value, (dict, list)):
        return '[complex value]'

    elif isinstance(value, bool):
        return str(value).lower()

    return str(value)\
        .replace("True", "true")\
        .replace('False', 'false')\
        .replace('None', 'null')
