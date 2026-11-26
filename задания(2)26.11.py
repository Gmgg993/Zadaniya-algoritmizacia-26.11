def task1():
    name = input("Введите имя: ") # <-- Исправленный код

    if name != "":
        print("Здравствуйте,", name)
    else:
        print("Имя не введено")

def task2():
    number = int(input("Введите число: ")) # <-- тоже исправленный код

    if number < 0:
        print("Отрицательное число")
    elif number > 0:
        print("Положительное число")
    else:
        print("Число равно нулю")

def task3():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        operation = input("Введите операцию (+, -, *, /): ")

        if operation == "+":
            print("Результат:", a + b)

        elif operation == "-":
            print("Результат:", a - b)

        elif operation == "*":
            print("Результат:", a * b)

        elif operation == "/":
            if b == 0:
                print("Ошибка: деление на ноль!")
            else:
                print("Результат:", a / b)

        else:
            print("Неизвестная операция!")

    except ValueError:
        print("Ошибка: необходимо вводить числа!")
    
def task4():
    a = 10
    b = 20
    c = 30

    average = (a + b + c) / 3

    print("Среднее значение:", average)
    a = 5
    b = 10
    c = 15

    average = (a + b + c) / 3

    print("Дополнительная проверка:", average)

def task5():

    def check_even(number):
        if number % 2 == 0:
            return "Чётное"
        else:
            return "Нечётное"


    print("8:", check_even(8))
    print("7:", check_even(7))
    print("0:", check_even(0))
    print("-4:", check_even(-4))
    print("-9:", check_even(-9))

def task6():
    numbers = [5, 12, 3, 21, 8]

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Максимальное число:", maximum)
    numbers = [-5, -12, -3, -21, -8]

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Максимальное отрицательное число:", maximum)

def task7():

    correct_login = "admin"
    correct_password = "Python123"

    attempts = 3

    while attempts > 0:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login == correct_login and password == correct_password:
            print("Доступ разрешён")
            break

        else:
            attempts -= 1
            print("Неверный логин или пароль!")
            print("Осталось попыток:", attempts)

    else:
        print("Доступ заблокирован")

while True:
    print("Менюшка")
    choice=input("Выберите задание: ")
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "5":
        task5()
    elif choice == "6":
        task6()
    elif choice == "7":
        task7()
    elif choice == "0":
        print("Завершение")
        break
    else:
        print("Нет такого задания")
