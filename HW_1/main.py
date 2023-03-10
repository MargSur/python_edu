"""
 Задание 1.
 Поработайте с переменными, создайте несколько,
 выведите на экран, запросите у пользователя несколько чисел и
 строк и сохраните в переменные, выведите на экран.
 %10s %5d %10s %5d
"""

print("Последовательность четных и нечетных цифр")
a = [1, 3, 5, 7]
b = [0, 2, 4, 6]
a.append(9)
b.append(8)
print(f"Нечетные - {a}")
print(f"Четные - {b}")
print("Заполните короткую анкету")
name = input("Введите ваше имя")
age = int(input("Введите ваш возраст"))
residence = input("Введите ваш город проживания в родительном падеже")
building = int(input("Введите ваш номер дома"))
print(f"Вас зовут {name}, Вам {age} лет, проживаете в {residence}, "
      f"Ваш номер дома - {building})")


"""
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


time = int(input("Введите время в секундах"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} ч: {minutes} м: {seconds} с")


"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""

print("Введите число:")
a = input()
print(a + a)
print(a + a + a)
total = (int(a) + int(str(a + a)) + int(str(a + a + a)))
print(f"Сумма чисел: {a} + {a+a} + {a+a+a} = {total}")

"""
Задание 4
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
"""


n = abs(int(input("Введите целое положительное число ")))
max_num = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_num:
        max_num = n % 10
    if n > 9:
        continue
    else:
        print(f"Максимальная цифра в числе равна {max_num}")
        break


"""
Задание 5.
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""

profit = float(input("Введите выручку фирмы"))
costs = float(input("Введите издержки фирмы"))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила "
          f"{round(((profit - costs )/ costs)*100, 2)}%")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника сотавила "
          f"{round((profit-costs) / workers, 2)}у.е.")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")