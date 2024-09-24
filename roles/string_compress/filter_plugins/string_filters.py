def compress(value):
    if not value:
        return ''
    result = []
    current_char = value[0]
    count = 1
    for char in value[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    return ''.join(result)

class FilterModule(object):
    def filters(self):
        return {
            'compress': compress
        }
