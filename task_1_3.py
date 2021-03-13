words = ['процент', 'процента', 'процентов']
rem = 0

for num in range(1, 20):
    if num == 1:
        print(num, words[0])
    elif 1 < num < 5:
        print(num, words[1])
    elif 5 <= num <= 20:
        print(num, words[2])

# всё работает для чисел от 1 до 20, по заданию
