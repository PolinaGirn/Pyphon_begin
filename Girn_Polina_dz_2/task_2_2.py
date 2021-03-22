text = ['в', '5', 'часов', '17', 'минут', 'температура',
        'воздуха', 'была', '+5', 'градусов']

count = 0
i = 0

while i != len(text):

    for elem_index in range(len(text[i])):
        if text[i][elem_index].isdigit():
            count += 1

    if count == 1:
        # text[i] = list(text[i])
        if not text[i][0].isdigit():
            text[i] = text[i][0] + '0' + text[i][1:]
            # text[i].insert(1, '0')
        else:
            text[i] = '0' + text[i]
            # text[i].insert(0, '0')

    count = 0
    i += 1

print(" ".join(map(str, text)))

# Сделано задание со *, без создания новых строк
