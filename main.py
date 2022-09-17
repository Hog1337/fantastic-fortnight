# калькулятор
from math import *

def is_negative(num):
    negative = num
    num = num.replace('-', '').replace('.', '').replace(',', '')
    if num.isdigit():
        if negative[0] == '-':
            return True
        else:
            return False


def digit_check(num):
    while num.isdigit() != True:
        print('Введёный элемент не является числом, введите число:')
        num = input()
    return num


def check_for_log(num):
    num1 = num.replace('.', '').replace(',', '')
    while is_negative(num) or num1.isdigit() != True:
        if is_negative(num):
            print('Введёный элемент является отрицательным, введите положительное число:')
            num = input()
            num1 = num.replace('.', '').replace(',', '')
        elif '.' in num or ',' in num:
            return num
        elif num1.isdigit() != True:
            print('Введёный элемент не является числом, введите число:')
            num = input()
            num1 = num.replace('.', '').replace(',', '')
    return num


def round_down(a, n):
    if a > 0:
        return round(a - 0.5 / 10 ** n, n)
    else:
        return round(a + 0.5 / 10 ** n, n)


def typical_1():
    c = []
    print("Введите первое число:")
    num = input()
    num1 = num.replace('-', '').replace('.', '').replace(',', '')
    while num1.isdigit() != True and is_negative(num1) != True:
        print('Введёный элемент не является числом, введите первый элемент:')
        num = input()
        num1 = num.replace('-', '').replace('.', '').replace(',', '')
    c.append(num)
    print('Введите второе число:')
    num = input()
    num1 = num.replace('-', '').replace('.', '').replace(',', '')
    while num1.isdigit() != True and is_negative(num1) != True:
        print('Введёный элемент не является числом, введите второй элемент:')
        num = input()
        num1 = num.replace('-', '').replace('.', '').replace(',', '')
    c.append(num)
    for i in range(len(c)):
        if ',' in c[i] or '.' in c[i]:
            c[i] = float(c[i])
        else:
            c[i] = int(c[i])
    return c


def typical_2():
    c = []
    print('Введите число:')
    num = input()
    num1 = num
    if '.' or ',' in num:
        num = num.replace('.', '').replace(',', '').replace('-', '')
    while num.isdigit() != True and is_negative(num) != True:
        print('Введёный элемент не является числом, введите число:')
        num = input()
        num1 = num
    c.append(float(num1))
    print('Введите количество знаков после округления:')
    num = input()
    while num.isdigit() != True and is_negative(num) != True:
        print('Введёный элемент не является числом, введите число:')
        num = input()
    c.append(int(num))
    return c


print("Допустимые функции: \n")
a = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Возведение в степень', 'Логарифм',
     'Округление в большую сторону до N знака после запятой', 'Округление в меньшую сторону до N знака после запятой']
for i in range(len(a)): print(a[i])
for i in range(len(a)):
    a.append(a[i].swapcase())
    a.append(a[i].lower())
    a.append(a[i].upper())
print('\nВыберите функцию:')
func = input()
while func not in a:
    print("Данной функции не существует, выберите функцию из списка:")
    func = input()
# сложение
if func == a[0] or func == a[8] or func == a[9] or func == a[10]:
    num_1, num_2 = typical_1()
    print('Результат:', num_1 + num_2)
# вычитание
elif func == a[1] or func == a[11] or func == a[12] or func == a[13]:
    num_1, num_2 = typical_1()
    print('Результат:', num_1 - num_2)
# умножение
elif func == a[2] or func == a[14] or func == a[15] or func == a[16]:
    num_1, num_2 = typical_1()
    print('Результат:', num_1 * num_2)
# деление
elif func == a[3] or func == a[17] or func == a[18] or func == a[19]:
    num_1, num_2 = typical_1()
    while num_2 == 0:
        print('Делитель не может быть равен 0, введите другое число:')
        num_2 = input()
        if ',' in num_2 or '.' in num_2:
            num_2 = float(num_2)
        else:
            num_2 = int(num_2)
    print('Результат:', num_1 / num_2)
# возведение в степень
elif func == a[4] or func == a[20] or func == a[21] or func == a[22]:
    print('Введите число:')
    num = input()
    num = int(digit_check(num))
    print('Введите степень:')
    n = input()
    n = int(digit_check(n))
    print('Результат:', int(pow(num, n)))
# логарифм
elif func == a[5] or func == a[23] or func == a[24] or func == a[25]:
    print('Введите основание:')
    b = input()
    while b == '1':
        print('Основание не может быть равно 1, введите другое число:')
        b = input()
    b = float(check_for_log(b))
    print('Введите подлогорифмическое выражение:')
    a = input()
    while a == '0':
        print('Подлогарифмическкое выражение не может быть равно 0, введите другое число:')
        a = input()
    a = float(check_for_log(a))
    print('Результат:', log(a, b))
# округление вверх
elif func == a[6] or func == a[26] or func == a[27] or func == a[28]:
    a, b = typical_2()
    if a > 0:
        print('Результат:', round(a, b))
    else:
        print("Результат:", round_down(a, b))
# округление вниз
elif func == a[7] or func == a[29] or func == a[30] or func == a[31]:
    a, b = typical_2()
    if a > 0:
        print('Результат:', round_down(a, b))
    else:
        print("Результат:", round(a, b))
input('Нажмите любую клавишу')