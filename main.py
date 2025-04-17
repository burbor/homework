def summ(x):
    sum_number = 0
    while x >= 1:
        sum_number += x % 10
        x //= 10
    return sum_number


def num(y):
    num_number = 0
    while y > 1:
        y /= 10
        num_number += 1
    return num_number


number = int(input('Введите число :'))
print('Сумма чисел:', summ(number))
print('Количество цифр:', num(number))
difference = summ(number) - num(number)
print('Разность суммы и количества цифр:', difference)
