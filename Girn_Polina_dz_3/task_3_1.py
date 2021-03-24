def num_translate(word):
    translate = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return translate.get(word, None)


"""
меня всегда учили (с++), что функция не должна выводить на экран ничего сама,
максимум возвращать строку, которую нужно вывести, поэтому так

я хотела вынести словарь куда-нибудь в наружу, но не получилось
"""

print(num_translate('one'))
print(num_translate('three'))
print(num_translate('nine'))
print(num_translate('cat'))
print(num_translate('dog'))
