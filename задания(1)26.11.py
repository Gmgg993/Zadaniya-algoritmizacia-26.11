def task1():
    try:
        balance = float(input("Введите баланс: "))
        withdrawal = float(input("Введите сумму снятия: "))

        if withdrawal < 0:
            raise ValueError("Сумма снятия не может быть отрицательной!")

        if withdrawal > balance:
            raise ValueError("Недостаточно средств!")

        balance -= withdrawal
        print("Операция выполнена!")
        print("Остаток:", balance)

    except ValueError as e:
        print("Ошибка:", e)

    except Exception:
        print("Произошла неизвестная ошибка.")

def task2():
    try:
        numbers = input("Введите числа через пробел: ")

        if not numbers.strip():
            raise ValueError("Список пуст!")

        numbers = [float(x) for x in numbers.split()]

        average = sum(numbers) / len(numbers)

    except ValueError as e:
        print("Ошибка:", e)

    except ZeroDivisionError:
        print("Невозможно вычислить среднее значение!")

    else:
        print("Среднее значение:", average)

def task3():
    try:
        with open("numbers.txt", "r", encoding="utf-8") as file:
            total = 0

            for number, line in enumerate(file, start=1):
                try:
                    total += float(line.strip())
                except ValueError:
                    raise ValueError(f"Ошибка в строке {number}: неправильное число")

    except FileNotFoundError:
        print("Файл не найден!")

    except PermissionError:
        print("Нет доступа к файлу!")

    except ValueError as e:
        print(e)

    else:
        print("Сумма чисел:", total)

def task4():
    users = {
        "admin": "12345",
        "user": "qwerty",
        "student": "python"
    }

    attempts = 3

    while attempts > 0:
        try:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            if not login or not password:
                raise ValueError("Поля не должны быть пустыми!")

            if login not in users:
                raise KeyError("Такого логина не существует!")

            if users[login] != password:
                raise ValueError("Неверный пароль!")

        except (ValueError, KeyError) as e:
            attempts -= 1
            print("Ошибка:", e)
            print("Осталось попыток:", attempts)

        else:
            print("Вы успешно вошли в систему!")
            break

    if attempts == 0:
        print("Вход заблокирован!")

def task5():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        operation = input("Введите операцию (+, -, *, /, //, %, **): ")

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b
        elif operation == "//":
            result = a // b
        elif operation == "%":
            result = a % b
        elif operation == "**":
            result = a ** b
        else:
            raise ValueError("Неизвестная операция!")

        if abs(result) > 1e100:
            raise OverflowError("Слишком большой результат!")

    except ValueError as e:
        print("Ошибка:", e)

    except ZeroDivisionError:
        print("Деление на ноль невозможно!")

    except OverflowError as e:
        print("Ошибка:", e)

    else:
        print("Результат:", result)

def task6():
    products = {
        "Хлеб": {"price": 200, "quantity": 10},
        "Молоко": {"price": 500, "quantity": 5},
        "Сахар": {"price": 350, "quantity": 8}
    }

    while True:
        print("\n1. Просмотр товаров")
        print("2. Добавить товар")
        print("3. Изменить количество")
        print("4. Продать товар")
        print("0. Выход")

        try:
            choice = int(input("Выберите действие: "))

            if choice == 0:
                break

            elif choice == 1:
                for name, data in products.items():
                    print(name, "| Цена:", data["price"],
                          "| Количество:", data["quantity"])

            elif choice == 2:
                name = input("Название товара: ")
                price = float(input("Цена: "))
                quantity = int(input("Количество: "))

                if price <= 0 or quantity < 0:
                    raise ValueError("Неправильная цена или количество!")

                if name in products:
                    raise ValueError("Такой товар уже существует!")

                products[name] = {
                    "price": price,
                    "quantity": quantity
                }

                print("Товар добавлен!")

            elif choice == 3:
                name = input("Название товара: ")

                if name not in products:
                    raise KeyError("Товар не найден!")

                quantity = int(input("Новое количество: "))

                if quantity < 0:
                    raise ValueError("Количество не может быть отрицательным!")

                products[name]["quantity"] = quantity
                print("Количество изменено!")

            elif choice == 4:
                name = input("Название товара: ")

                if name not in products:
                    raise KeyError("Товар не найден!")

                quantity = int(input("Количество для продажи: "))

                if quantity <= 0:
                    raise ValueError("Количество должно быть положительным!")

                if quantity > products[name]["quantity"]:
                    raise ValueError("Недостаточно товара на складе!")

                products[name]["quantity"] -= quantity
                print("Стоимость:", quantity * products[name]["price"])

            else:
                print("Неверный пункт меню!")

        except (ValueError, KeyError) as e:
            print("Ошибка:", e)

def task7():
    try:
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        email = input("Введите электронную почту: ")
        password = input("Введите пароль: ")

        if len(name) < 3:
            raise ValueError("Имя должно содержать минимум 3 символа!")

        if age < 14 or age > 100:
            raise ValueError("Возраст должен быть от 14 до 100 лет!")

        if "@" not in email or "." not in email:
            raise ValueError("Неправильный адрес электронной почты!")

        if len(password) < 8:
            raise ValueError("Пароль должен содержать минимум 8 символов!")

    except ValueError as e:
        print("Ошибка:", e)

    else:
        print("Регистрация прошла успешно!")

def task8():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    try:
        for row in matrix:
            print(row)

        row = int(input("Номер строки (0-2): "))
        col = int(input("Номер столбца (0-2): "))

        if not (0 <= row < len(matrix)):
            raise IndexError("Такой строки не существует!")

        if not (0 <= col < len(matrix[row])):
            raise IndexError("Такого столбца не существует!")

        value = input("Новое значение: ")

        if not value.isdigit():
            raise ValueError("Новое значение должно быть целым числом!")

        matrix[row][col] = int(value)

    except ValueError as e:
        print("Ошибка:", e)

    except IndexError as e:
        print("Ошибка:", e)

    else:
        print("Изменённая матрица:")
        for row in matrix:
            print(row)

def task9():
    products = {
        "Ноутбук": {"price": 250000, "stock": 5},
        "Мышь": {"price": 5000, "stock": 20},
        "Клавиатура": {"price": 12000, "stock": 10}
    }

    MAX_SUM = 500000

    try:
        print("Доступные товары:")

        for name, data in products.items():
            print(name, "-", data["price"], "тг. Остаток:", data["stock"])

        name = input("Выберите товар: ")

        if name not in products:
            raise KeyError("Товар отсутствует!")

        quantity = int(input("Введите количество: "))

        if quantity <= 0:
            raise ValueError("Количество должно быть положительным!")

        if quantity > products[name]["stock"]:
            raise ValueError("Недостаточно товара на складе!")

        total = products[name]["price"] * quantity

        if total > MAX_SUM:
            raise ValueError("Сумма заказа превышает 500000 тенге!")

        products[name]["stock"] -= quantity

    except ValueError as e:
        print("Ошибка:", e)

    except KeyError as e:
        print("Ошибка:", e)

    else:
        print("Заказ оформлен!")
        print("Итоговая стоимость:", total, "тенге")

def task10():
    class InvalidAgeError(Exception):
        pass


    class InvalidEmailError(Exception):
        pass


    class WeakPasswordError(Exception):
        pass


    try:
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        email = input("Введите email: ")
        password = input("Введите пароль: ")

        if len(name) < 3:
            raise ValueError("Имя слишком короткое!")

        if age < 14 or age > 100:
            raise InvalidAgeError("Недопустимый возраст!")

        if "@" not in email or "." not in email:
            raise InvalidEmailError("Неправильный email!")

        if len(password) < 8:
            raise WeakPasswordError("Слишком слабый пароль!")

    except InvalidAgeError as e:
        print("Ошибка возраста:", e)

    except InvalidEmailError as e:
        print("Ошибка почты:", e)

    except WeakPasswordError as e:
        print("Ошибка пароля:", e)

    except ValueError as e:
        print("Ошибка:", e)

    else:
        print("Пользователь успешно зарегистрирован!")

def task11():
    from datetime import datetime

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        result = a / b

    except ValueError as e:
        error = e
        print("Ошибка: необходимо вводить числа!")

    except ZeroDivisionError as e:
        error = e
        print("Ошибка: деление на ноль!")

    else:
        print("Результат:", result)

        error = None

    finally:
        if error is not None:
            with open("errors.log", "a", encoding="utf-8") as file:
                file.write(
                    f"{datetime.now()} | "
                    f"{type(error).__name__} | {error}\n"
                )

        print("Работа программы завершена.")

def task12():
    import json
    import os


    class BookNotFoundError(Exception):
        pass


    class BookAlreadyIssuedError(Exception):
        pass


    class BookNotIssuedError(Exception):
        pass


    def load_books():
        try:
            if not os.path.exists("library.json"):
                return {}

            with open("library.json", "r", encoding="utf-8") as file:
                books = json.load(file)

                if not isinstance(books, dict):
                    raise ValueError("Неправильный формат файла!")

                return books

        except FileNotFoundError:
            return {}

        except PermissionError:
            print("Нет доступа к файлу!")
            return {}

        except json.JSONDecodeError:
            print("Файл повреждён!")
            return {}

        except ValueError as e:
            print("Ошибка:", e)
            return {}


    def save_books():
        try:
            with open("library.json", "w", encoding="utf-8") as file:
                json.dump(books, file, ensure_ascii=False, indent=4)

        except PermissionError:
            print("Нет доступа для сохранения!")

        except OSError as e:
            print("Ошибка сохранения:", e)

        else:
            print("Данные сохранены!")


    def add_book():
        title = input("Название книги: ")
        author = input("Автор книги: ")

        if not title.strip() or not author.strip():
            raise ValueError("Название и автор не должны быть пустыми!")

        if title in books:
            raise ValueError("Такая книга уже существует!")

        books[title] = {
            "author": author,
            "issued": False,
            "reader": None
        }

        print("Книга добавлена!")


    def search_book():
        title = input("Введите название книги: ")

        if title not in books:
            raise BookNotFoundError("Книга не найдена!")

        print("Название:", title)
        print("Автор:", books[title]["author"])

        if books[title]["issued"]:
            print("Статус: выдана читателю", books[title]["reader"])
        else:
            print("Статус: доступна")


    def issue_book():
        title = input("Название книги: ")

        if title not in books:
            raise BookNotFoundError("Книга не найдена!")

        if books[title]["issued"]:
            raise BookAlreadyIssuedError("Книга уже выдана!")

        reader = input("Имя читателя: ")

        if not reader.strip():
            raise ValueError("Имя читателя не может быть пустым!")

        books[title]["issued"] = True
        books[title]["reader"] = reader

        print("Книга выдана читателю!")


    def return_book():
        title = input("Название книги: ")

        if title not in books:
            raise BookNotFoundError("Книга не найдена!")

        if not books[title]["issued"]:
            raise BookNotIssuedError("Книга не была выдана!")

        books[title]["issued"] = False
        books[title]["reader"] = None

        print("Книга успешно возвращена!")


    books = load_books()

    while True:
        print("\n===== БИБЛИОТЕКА =====")
        print("1. Добавить книгу")
        print("2. Найти книгу")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Показать все книги")
        print("6. Сохранить данные")
        print("0. Выход")

        try:
            choice = int(input("Выберите действие: "))

            if choice == 1:
                add_book()

            elif choice == 2:
                search_book()

            elif choice == 3:
                issue_book()

            elif choice == 4:
                return_book()

            elif choice == 5:
                if not books:
                    print("Библиотека пуста!")
                else:
                    for title, data in books.items():
                        status = "Выдана" if data["issued"] else "Доступна"
                        print(title, "-", data["author"], "-", status)

            elif choice == 6:
                save_books()

            elif choice == 0:
                save_books()
                print("Выход из программы...")
                break

            else:
                print("Такого пункта меню нет!")

        except ValueError as e:
            print("Ошибка ввода:", e)

        except BookNotFoundError as e:
            print("Ошибка:", e)

        except BookAlreadyIssuedError as e:
            print("Ошибка:", e)

        except BookNotIssuedError as e:
            print("Ошибка:", e)

        finally:
            print("Операция завершена.")

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
    elif choice == "8":
        task8()
    elif choice == "9":
        task9()
    elif choice == "10":
        task10()
    elif choice == "11":
        task11()
    elif choice == "12":
        task12()
    elif choice == "0":
        print("Завершение")
        break
    else:
        print("Нет такого задания")
