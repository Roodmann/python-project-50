

def format_plain(diffs):
    """Преобразует разницу в форматированный текст."""

    def transform_value(value):
        """Преобразует значения в определенный формат."""
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, str):
            return f"'{value}'"
        if value is None:
            return 'null'
        return str(value)

    lines = []

    def walk(diffs, patch=[]):
        """Рекурсия, формирует соответствующее 
           действие для каждого элемента.
        """
        #  проходиМ по каждому элементу разницы
        for diff in diffs:
            status = diff['status']
            key = diff['key']

            if status == 'removed':
                property_path = '.'.join(patch + [key])
                lines.append(f"Property '{property_path}' was removed")

            elif status == 'added':
                property_path = '.'.join(patch + [key])
                new_value = transforms_value(diff['new_value'])
                lines.append(f"Property '{property_path}'"
                         f" was added with value: {new_value}"
                         )
            elif status == 'nested':
                property_path = '.'.join(patch + [key])
                nested_diffs = diff['nested']
                walk(nested_diffs, patch=patch + [key])

            elif status == 'updated':
                property_path = '.'.join(patch + [key])
                old_value = transforms_value(diff['old_value'])
                new_value = transforms_value(diff['new_value'])
                lines.append(f"Property '{property_path}'"
                         f" was updated. From {old_value} to {new_value}"
                         )

    walk(diffs)
    return '\n'.join(lines)
    


def transforms_value(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, (dict, list)):
        return '[complex value]'

    return str(value)\
        .replace("True", "true")\
        .replace('False', 'false')\
        .replace('None', 'null')
