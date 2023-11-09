

def format_plain(diff_line):
    lines = []

    def walk(diff, patch):
        patch += (diff.get('key'),)
        status = diff.get('status')

        if status == 'removed':
            lines.append(f"Property '{'.'.join(patch)}' was removed")

        elif status == 'added':
            new_value = transforms_value(diff.get('new_value'))
            lines.append(f"Property '{'.'.join(patch)}'"
                         f" was added with value: {new_value}"
                         )

        elif status == 'updated':
            old_value = transforms_value(diff.get('old_value'))
            new_value = transforms_value(diff.get('new_value'))
            lines.append(f"Property '{'.'.join(patch)}'"
                         f" was updated. From {old_value} to {new_value}"
                         )

        list(map(lambda value: walk(value, patch), diff.get('nested', [])))

    for elem in diff_line:
        walk(elem, ())

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
