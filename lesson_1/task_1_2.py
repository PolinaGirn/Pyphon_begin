nums = []           # список
num = 0             # само число
num_copy = 0        # копия числа чтобы удобно считать сумму его цифр
rem = 0             # переменная для записи остатка
sum_of_num = 0      # сумма чисел, сумма цифр которых кратна 7

for i in range(1000):
    sum_of_digits = 0               # переменная для суммы цифр числа
    num = i+1
    rem = num % 2

    if rem != 0:
        num = num ** 3
        nums.append(num)
        num_copy = num

        while num_copy != 0:
            sum_of_digits += num_copy % 10
            num_copy //= 10
        # print(sum_of_digits)      # вывод сумм цифр для проверки

        rem = sum_of_digits % 7
        if rem == 0:
            sum_of_num += num

print("список №1: ", nums)
print("сумма чисел:", sum_of_num)

sum_of_num = 0
for i in range(len(nums)):
    nums[i] += 17
    num = nums[i]
    num_copy = num
    sum_of_digits = 0

    while num_copy != 0:
        sum_of_digits += num_copy % 10
        num_copy //= 10
    # print(sum_of_digits)          # вывод сумм цифр для проверки

    rem = sum_of_digits % 7
    if rem == 0:
        sum_of_num += num

print("список №2: ", nums)
print("сумма чисел:", sum_of_num)

# сделала все пункты, включая *, пункт b решен без создания нового списка
