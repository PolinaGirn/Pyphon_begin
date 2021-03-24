def thesaurus(*args):
    """
    создаю пустой словарь, иду по элементам списка,
    если в словаре ещё нет слов на первую букву текущего элемента,
    создаем пару в словаре, где ключ - первая буква элемента,
    а значение - список с одним элементом, текущим значением
    если же такой ключ уже есть, добавляем к существующему списку новое значение
    """
    dictionary = {}
    for word in args:
        first_letter = word[0]
        words = []
        if dictionary.get(first_letter, None) is None:
            words.append(word)
            dictionary.setdefault(first_letter, words)
        else:
            dictionary[first_letter].append(word)

    return dictionary


names = ['Мария', 'Марк', 'Петр', 'Ольга', 'Олег']

"""тут распаковка, так как список это один элемент, а нам надо много"""
print(thesaurus(*names))
print(thesaurus('Михаил', 'Константин', 'Марк', 'Иван', 'Петр'))
