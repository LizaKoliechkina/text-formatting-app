import enum


class Filter(str, enum.Enum):
    capitalize = 'capitalize'
    upper = 'upper'
    lower = 'lower'
    title = 'title'
    strange_format = 'strange_format'


def apply_filter(text: str, f: Filter) -> str:
    if f == 'capitalize':
        return text.capitalize()
    elif f == 'upper':
        return text.upper()
    elif f == 'lower':
        return text.lower()
    elif f == 'title':
        return text.title()
    elif f == 'strange_format':
        s = ''
        for i in range(len(text)):
            s += text[i].upper() if i % 2 == 1 else text[i].lower()
        return s
