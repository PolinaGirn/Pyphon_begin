price = [57.8, 92.42, 55, 7.4, 21.4, 66.4, 18.6, 52,
         47, 3.5, 5, 14.5, 9.7, 99.9]

print()     # для красоты

for i in range(len(price)):
    rub = int(price[i])
    kop = int(round(price[i] % 1, 2) * 100)

    if i == len(price)-1:
        final = '.\n'
    else:
        final = ', '

    if kop < 10 and i < len(price):
        print(f'{rub} руб 0{kop} коп', end=final)
    elif i < len(price):
        print(f'{rub} руб {kop} коп', end=final)

# задание А выполнено

print('\nid списка до сортировки:', id(price))
price.sort()
print('сортировка по возрастанию:', price)
print('id списка после сортировки:', id(price))

# задание В выполнено

waning_price = sorted(price, reverse=True)
print('\nсортировка по убывванию:', waning_price)

# задание С выполнено

print('\nСамые дорогие товары:')
for i in range(5):
    print(f'{i+1}. ', waning_price[i])

# задание D выполнено
# все задания сделала, всё запускается и работает
