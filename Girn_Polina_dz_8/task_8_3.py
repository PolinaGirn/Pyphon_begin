def type_logger(func):

    def wrapper(*args):
        calc = func(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for i in args:
                print(f'{i}: {type(i)}')
        return calc
    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


num = 10.7
a = calc_cube(num, 0, 'text', (4, 8, 5), {'a', 'b', 'a', 'c'})
print(f'куб числа {num} равен: {a}')

# немного подсмотрела как делать в следующей лекции
# поразбираю на днях декораторы, не совсем поняла тему
