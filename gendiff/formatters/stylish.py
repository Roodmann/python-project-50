from itertools import chain

START_DEPTH = 0
INDENT = '  '
STEP_INDENT = '    '


def make_line(diff, depth):
    key = diff.get('key')
    status = diff.get('status')
    indent = f'{INDENT}{STEP_INDENT*depth}'

    if status == 'added':
        new_value = diff.get('new_value')
        value = calculate_value(new_value, depth)
        return f'{indent}+ {key}: {value}'

    elif status == 'unchanged':
        old_value = diff.get('old_value')
        value = calculate_value(old_value, depth)
        return f"{indent}  {key}: {value}"

    elif status == 'updated':
        old_value = diff.get('old_value')
        new_value = diff.get('new_value')
        value = calculate_value(old_value, depth)
        value2 = calculate_value(new_value, depth)
        return f'{indent}- {key}: {value}\n{indent}+ {key}: {value2}'

    elif status == 'removed':
        old_value = diff.get('old_value')
        value = calculate_value(old_value, depth)
        return f'{indent}- {key}: {value}'

    elif status == 'nested':
        nested = diff.get('nested')
        value = calculate_value(nested, depth)
        return f'{indent}  {key}: {value}'


def calculate_value(diff, depth):
    if isinstance(diff, dict):
        return format_diff(diff, depth + 1)

    elif isinstance(diff, list):
        return format_diff(diff, depth + 1)

    elif isinstance(diff, bool):
        return str(diff).lower()

    elif diff is None:
        return 'null'

    return str(diff)


def format_stylish(diff):
    return format_diff(diff, START_DEPTH)


def format_diff(diff, depth):
    lines = []

    for elem in diff:
        if isinstance(elem, dict):
            lines.append(make_line(elem, depth))
        else:
            lines.append(make_line({'key': elem, "status": 'unchanged',
                                    'old_value': diff.get(elem)}, depth)
                         )

    result = chain("{", lines, [f"{STEP_INDENT * depth}" + "}"])
    return '\n'.join(result)
