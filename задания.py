import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

def task1():
    window = tk.Tk()
    window.title("Моё первое приложение")
    window.geometry("600x400")
    window.mainloop()
    
def task2():
    window = tk.Tk()
    window.title("Информационная система")
    window.geometry("700x450")
    window.configure(bg="lightblue")
    window.minsize(400, 300)
    window.maxsize(900, 600)
    window.mainloop()
    
def task3():
    window = tk.Tk()
    window.title("Окно по центру")
    window.geometry("500x350")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 500) // 2
    y = (screen_height - 350) // 2
    window.geometry(f"500x350+{x}+{y}")
    window.mainloop()
    
def task4():
    window = tk.Tk()
    window.title("Электронный дневник")
    window.geometry("600x450")
    window.configure(bg="#EAF2F8")
    window.resizable(False, False)
    title = tk.Label(
        window,
        text="Электронный дневник",
        font=("Arial", 22, "bold"),
        bg="#EAF2F8",
        fg="#1A5276"
    )
    title.pack(pady=25)
    greeting = tk.Label(
        window,
        text="Добро пожаловать!",
        font=("Arial", 16),
        bg="#EAF2F8"
    )
    greeting.pack(pady=10)
    user = tk.Label(
        window,
        text="Пользователь: Симонов Богдан Иванович",
        font=("Arial", 12),
        bg="#EAF2F8"
    )
    user.pack(pady=10)
    def start_work():
        greeting.config(text="Вы начали работу!")
    tk.Button(
        window,
        text="Начать работу",
        font=("Arial", 12),
        width=20,
        command=start_work
    ).pack(pady=15)
    tk.Button(
        window,
        text="Выход",
        font=("Arial", 12),
        width=20,
        command=window.destroy
    ).pack(pady=10)
    window.mainloop()

def task5():
    window = tk.Tk()
    window.title("Авторизация")
    window.geometry("400x300")
    window.configure(bg="#EAF2F8")
    window.resizable(False, False)
    tk.Label(
        window,
        text="Вход в систему",
        font=("Arial", 20, "bold"),
        bg="#EAF2F8"
    ).pack(pady=20)
    tk.Label(
        window,
        text="Логин:",
        font=("Arial", 12),
        bg="#EAF2F8"
    ).pack()
    login_entry = tk.Entry(window, font=("Arial", 12))
    login_entry.pack(pady=5)
    tk.Label(
        window,
        text="Пароль:",
        font=("Arial", 12),
        bg="#EAF2F8"
    ).pack()
    password_entry = tk.Entry(
        window,
        font=("Arial", 12),
        show="*"
    )
    password_entry.pack(pady=5)
    def login():
        print("Логин:", login_entry.get())
        print("Пароль:", password_entry.get())
    def clear():
        login_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    tk.Button(
        window,
        text="Войти",
        width=15,
        command=login
    ).pack(pady=5)
    tk.Button(
        window,
        text="Очистить",
        width=15,
        command=clear
    ).pack(pady=5)
    tk.Button(
        window,
        text="Закрыть",
        width=15,
        command=window.destroy
    ).pack(pady=5)
    window.mainloop()

def task6():
    window_title = "Настройка интерфейса"
    window_width = 600
    window_height = 400
    background_color = "lightblue"
    window = tk.Tk()
    window.title(window_title)
    window.geometry(f"{window_width}x{window_height}")
    window.configure(bg=background_color)
    def change_color():
        window.configure(bg="lightgreen")
        title.config(bg="lightgreen")
    title = tk.Label(
        window,
        text="Настройка цвета окна",
        font=("Arial", 18, "bold"),
        bg=background_color
    )
    title.pack(pady=30)
    tk.Button(
        window,
        text="Изменить цвет фона",
        font=("Arial", 12),
        command=change_color
    ).pack(pady=20)
    window.mainloop()

def task7():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            total INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            reader TEXT NOT NULL,
            issue_date TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)
    cursor.execute(
        "INSERT OR IGNORE INTO users (login, password, role) VALUES (?, ?, ?)",
        ("admin", "admin123", "Администратор")
    )
    cursor.execute(
        "INSERT OR IGNORE INTO users (login, password, role) VALUES (?, ?, ?)",
        ("librarian", "lib123", "Библиотекарь")
    )
    demo_books = [
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 5),
        ("Война и мир", "Лев Толстой", 1869, "Роман", 4),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 3),
        ("Гарри Поттер", "Джоан Роулинг", 1997, "Фэнтези", 6),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 4),
        ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 5),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", 3),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 4),
        ("Алхимик", "Пауло Коэльо", 1988, "Приключения", 3),
        ("Дюна", "Фрэнк Герберт", 1965, "Фантастика", 5)
    ]
    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO books (title, author, year, genre, total)
            VALUES (?, ?, ?, ?, ?)
        """, demo_books)
    conn.commit()
    window = tk.Tk()
    window.title("Библиотечная система")
    window.geometry("1000x650")
    window.configure(bg="#EAF2F8")
    window.minsize(800, 550)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 1000) // 2
    y = (screen_height - 650) // 2
    window.geometry(f"1000x650+{x}+{y}")
    current_user = None
    current_role = None

    BG = "#EAF2F8"
    BLUE = "#2874A6"
    DARK = "#1A5276"
    WHITE = "#FFFFFF"

    def clear_page():
        for widget in page_frame.winfo_children():
            widget.destroy()
    def get_available(book_id):
        cursor.execute("""
            SELECT
                b.total - COUNT(l.id)
            FROM books b
            LEFT JOIN loans l
                ON b.id = l.book_id AND l.return_date IS NULL
            WHERE b.id = ?
            GROUP BY b.id
        """, (book_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    def create_title(text):
        tk.Label(
            page_frame,
            text=text,
            font=("Arial", 21, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=15)
    def create_button(parent, text, command):
        return tk.Button(
            parent,
            text=text,
            font=("Arial", 10),
            bg=BLUE,
            fg=WHITE,
            activebackground=DARK,
            activeforeground=WHITE,
            width=18,
            height=2,
            cursor="hand2",
            command=command
        )

    def show_login():
        clear_page()

        global current_user, current_role
        current_user = None
        current_role = None
        create_title("Вход в библиотечную систему")
        login_frame = tk.Frame(page_frame, bg=BG)
        login_frame.pack(pady=30)
        tk.Label(
            login_frame,
            text="Логин:",
            font=("Arial", 12),
            bg=BG
        ).pack(pady=5)
        login_entry = tk.Entry(
            login_frame,
            font=("Arial", 12),
            width=25
        )
        login_entry.pack(pady=5)
        tk.Label(
            login_frame,
            text="Пароль:",
            font=("Arial", 12),
            bg=BG
        ).pack(pady=5)
        password_entry = tk.Entry(
            login_frame,
            font=("Arial", 12),
            width=25,
            show="*"
        )
        password_entry.pack(pady=5)

        def login():
            global current_user, current_role
            login_value = login_entry.get().strip()
            password_value = password_entry.get()
            cursor.execute("""
                SELECT login, role FROM users
                WHERE login = ? AND password = ?
            """, (login_value, password_value))
            result = cursor.fetchone()
            if result:
                current_user = result[0]
                current_role = result[1]
                show_home()
            else:
                messagebox.showerror(
                    "Ошибка",
                    "Неверный логин или пароль!",
                    parent=window
                )
        create_button(
            login_frame,
            "Войти",
            login
        ).pack(pady=10)
        create_button(
            login_frame,
            "Выход",
            close_program
        ).pack(pady=5)
        tk.Label(
            page_frame,
            text="Администратор: admin / admin123\n"
                 "Библиотекарь: librarian / lib123",
            font=("Arial", 10),
            bg=BG,
            fg="gray"
        ).pack(pady=15)
        login_entry.focus()

    def show_home():
        clear_page()

        create_title("Библиотечная система")

        tk.Label(
            page_frame,
            text=f"Пользователь: {current_user} | Роль: {current_role}",
            font=("Arial", 12),
            bg=BG,
            fg=DARK
        ).pack(pady=5)

        menu_frame = tk.Frame(page_frame, bg=BG)
        menu_frame.pack(pady=30)

        if current_role == "Администратор":
            create_button(
                menu_frame,
                "Добавить книгу",
                add_book
            ).pack(pady=7)
        create_button(
            menu_frame,
            "Список книг",
            show_books
        ).pack(pady=7)
        create_button(
            menu_frame,
            "Поиск книг",
            show_search
        ).pack(pady=7)
        create_button(
            menu_frame,
            "Выдать книгу",
            show_issue
        ).pack(pady=7)
        create_button(
            menu_frame,
            "Список выданных книг",
            show_issued
        ).pack(pady=7)
        create_button(
            menu_frame,
            "Выйти из аккаунта",
            show_login
        ).pack(pady=7)

    def book_form(book=None):

        form = tk.Toplevel(window)
        form.title("Добавление книги" if book is None else "Редактирование книги")
        form.geometry("400x420")
        form.configure(bg=BG)
        form.resizable(False, False)
        form.transient(window)
        form.grab_set()
        tk.Label(
            form,
            text="Добавление книги" if book is None else "Редактирование книги",
            font=("Arial", 17, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=15)
        fields = {}
        field_names = [
            "Название книги",
            "Автор",
            "Год издания",
            "Жанр",
            "Количество экземпляров"
        ]
        values = list(book[1:]) if book else ["", "", "", "", ""]
        for name, value in zip(field_names, values):
            tk.Label(
                form,
                text=name,
                font=("Arial", 10),
                bg=BG
            ).pack()
            entry = tk.Entry(form, font=("Arial", 11), width=35)
            entry.pack(pady=4)
            entry.insert(0, str(value))
            fields[name] = entry

        def save_book():
            title = fields["Название книги"].get().strip()
            author = fields["Автор"].get().strip()
            year = fields["Год издания"].get().strip()
            genre = fields["Жанр"].get().strip()
            total = fields["Количество экземпляров"].get().strip()
            if not all([title, author, year, genre, total]):
                messagebox.showwarning(
                    "Проверка",
                    "Заполните все поля!",
                    parent=form
                )
                return
            try:
                year = int(year)
                total = int(total)
                if year < 1 or year > date.today().year:
                    raise ValueError
                if total < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Ошибка",
                    "Год должен быть корректным числом,\n"
                    "а количество экземпляров — целым числом не меньше нуля.",
                    parent=form
                )
                return
            if book is None:
                cursor.execute("""
                    INSERT INTO books (title, author, year, genre, total)
                    VALUES (?, ?, ?, ?, ?)
                """, (title, author, year, genre, total))
            else:
                active = book[5] - get_available(book[0])
                if total < active:
                    messagebox.showerror(
                        "Ошибка",
                        "Количество экземпляров не может быть меньше "
                        "числа выданных книг!",
                        parent=form
                    )
                    return
                cursor.execute("""
                    UPDATE books
                    SET title = ?, author = ?, year = ?,
                        genre = ?, total = ?
                    WHERE id = ?
                """, (title, author, year, genre, total, book[0]))
            conn.commit()
            form.destroy()
            messagebox.showinfo(
                "Успех",
                "Данные книги сохранены!",
                parent=window
            )
            show_books()
        create_button(
            form,
            "Сохранить",
            save_book
        ).pack(pady=15)
    def show_books():
        clear_page()
        create_title("Каталог книг")
        table_frame = tk.Frame(page_frame, bg=BG)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)
        columns = (
            "id", "title", "author", "year",
            "genre", "total", "available"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )
        headings = {
            "id": "№",
            "title": "Название",
            "author": "Автор",
            "year": "Год",
            "genre": "Жанр",
            "total": "Всего",
            "available": "Доступно"
        }
        widths = {
            "id": 40,
            "title": 200,
            "author": 180,
            "year": 60,
            "genre": 110,
            "total": 70,
            "available": 80
        }
        for column in columns:
            tree.heading(column, text=headings[column])
            tree.column(column, width=widths[column], anchor="center")
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def load_books():
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM books ORDER BY id")
            for book in cursor.fetchall():
                available = get_available(book[0])
                tree.insert(
                    "",
                    "end",
                    values=(
                        book[0],
                        book[1],
                        book[2],
                        book[3],
                        book[4],
                        book[5],
                        available
                    )
                )

        load_books()
        buttons = tk.Frame(page_frame, bg=BG)
        buttons.pack(pady=10)

        def get_selected():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning(
                    "Внимание",
                    "Сначала выберите книгу!",
                    parent=window
                )
                return None
            return tree.item(selected[0], "values")

        def edit_selected():
            if current_role != "Администратор":
                messagebox.showerror(
                    "Доступ запрещён",
                    "Редактировать книги может только администратор.",
                    parent=window
                )
                return
            selected = get_selected()
            if selected is None:
                return
            book_id = int(selected[0])
            cursor.execute(
                "SELECT * FROM books WHERE id = ?",
                (book_id,)
            )
            book_form(cursor.fetchone())

        def delete_selected():
            if current_role != "Администратор":
                messagebox.showerror(
                    "Доступ запрещён",
                    "Удалять книги может только администратор.",
                    parent=window
                )
                return
            selected = get_selected()

            if selected is None:
                return
            book_id = int(selected[0])
            cursor.execute("""
                SELECT COUNT(*) FROM loans
                WHERE book_id = ? AND return_date IS NULL
            """, (book_id,))
            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Невозможно удалить",
                    "Эта книга сейчас выдана читателю.",
                    parent=window
                )
                return
            answer = messagebox.askyesno(
                "Удаление",
                "Вы действительно хотите удалить книгу?",
                parent=window
            )
            if answer:
                cursor.execute(
                    "DELETE FROM loans WHERE book_id = ?",
                    (book_id,)
                )
                cursor.execute(
                    "DELETE FROM books WHERE id = ?",
                    (book_id,)
                )
                conn.commit()
                load_books()
        if current_role == "Администратор":
            create_button(
                buttons,
                "Добавить",
                add_book
            ).pack(side="left", padx=5)
            create_button(
                buttons,
                "Редактировать",
                edit_selected
            ).pack(side="left", padx=5)
            create_button(
                buttons,
                "Удалить",
                delete_selected
            ).pack(side="left", padx=5)
        create_button(
            buttons,
            "Выдать книгу",
            lambda: issue_selected(tree)
        ).pack(side="left", padx=5)
        create_button(
            buttons,
            "Назад",
            show_home
        ).pack(side="left", padx=5)

    def add_book():
        if current_role != "Администратор":
            messagebox.showerror(
                "Доступ запрещён",
                "Добавлять книги может только администратор.",
                parent=window
            )
            return
        book_form()

    def show_search():
        clear_page()
        create_title("Поиск книг")
        search_entry = tk.Entry(
            page_frame,
            font=("Arial", 13),
            width=40
        )
        search_entry.pack(pady=10)
        tree_frame = tk.Frame(page_frame, bg=BG)
        tree_frame.pack(fill="both", expand=True, padx=15, pady=10)
        columns = ("id", "title", "author", "year", "genre", "available")
        tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            height=15
        )
        headings = {
            "id": "№",
            "title": "Название",
            "author": "Автор",
            "year": "Год",
            "genre": "Жанр",
            "available": "Доступно"
        }
        for column in columns:
            tree.heading(column, text=headings[column])
            tree.column(column, width=140, anchor="center")
        tree.pack(fill="both", expand=True)

        def search():
            tree.delete(*tree.get_children())
            query = search_entry.get().strip().lower()
            cursor.execute("""
                SELECT id, title, author, year, genre
                FROM books
            """)
            results = []
            for book in cursor.fetchall():
                if (
                    query in book[1].lower()
                    or query in book[2].lower()
                    or query in book[4].lower()
                ):
                    results.append(book)
            if not results:
                messagebox.showinfo(
                    "Поиск",
                    "Книги не найдены!",
                    parent=window
                )
                return
            for book in results:
                tree.insert(
                    "",
                    "end",
                    values=(
                        *book,
                        get_available(book[0])
                    )
                )
        create_button(
            page_frame,
            "Найти",
            search
        ).pack(pady=5)
        create_button(
            page_frame,
            "Показать все книги",
            lambda: [search_entry.delete(0, tk.END), search()]
        ).pack(pady=5)
        create_button(
            page_frame,
            "Назад",
            show_home
        ).pack(pady=5)
        search_entry.focus()

    def issue_selected(tree):
        selected = tree.selection()
        if not selected:
            messagebox.showwarning(
                "Внимание",
                "Выберите книгу в таблице!",
                parent=window
            )
            return
        book_id = int(tree.item(selected[0], "values")[0])
        issue_book(book_id)

    def issue_book(book_id):
        available = get_available(book_id)
        if available <= 0:
            messagebox.showwarning(
                "Нет экземпляров",
                "Все экземпляры этой книги уже выданы!",
                parent=window
            )
            return
        cursor.execute(
            "SELECT title FROM books WHERE id = ?",
            (book_id,)
        )
        book = cursor.fetchone()
        if not book:
            return
        form = tk.Toplevel(window)
        form.title("Выдача книги")
        form.geometry("400x250")
        form.configure(bg=BG)
        form.resizable(False, False)
        form.transient(window)
        form.grab_set()
        tk.Label(
            form,
            text="Выдача книги",
            font=("Arial", 18, "bold"),
            bg=BG,
            fg=DARK
        ).pack(pady=15)
        tk.Label(
            form,
            text=f"Книга: {book[0]}",
            font=("Arial", 11),
            bg=BG,
            wraplength=350
        ).pack(pady=5)
        tk.Label(
            form,
            text="Ф. И. О. читателя:",
            font=("Arial", 11),
            bg=BG
        ).pack()
        reader_entry = tk.Entry(
            form,
            font=("Arial", 12),
            width=30
        )
        reader_entry.pack(pady=8)

        def confirm_issue():
            reader = reader_entry.get().strip()
            if not reader:
                messagebox.showwarning(
                    "Ошибка",
                    "Введите имя читателя!",
                    parent=form
                )
                return
            if get_available(book_id) <= 0:
                messagebox.showwarning(
                    "Нет экземпляров",
                    "Все книги уже выданы!",
                    parent=form
                )
                return
            cursor.execute("""
                INSERT INTO loans (book_id, reader, issue_date)
                VALUES (?, ?, ?)
            """, (book_id, reader, date.today().isoformat()))
            conn.commit()
            form.destroy()
            messagebox.showinfo(
                "Успех",
                "Книга успешно выдана!",
                parent=window
            )
        create_button(
            form,
            "Подтвердить выдачу",
            confirm_issue
        ).pack(pady=10)

    def show_issue():
        clear_page()
        create_title("Выдача книги")
        tk.Label(
            page_frame,
            text="Выберите книгу из каталога для выдачи читателю.",
            font=("Arial", 12),
            bg=BG
        ).pack(pady=10)
        create_button(
            page_frame,
            "Открыть каталог книг",
            show_books
        ).pack(pady=10)
        create_button(
            page_frame,
            "Назад",
            show_home
        ).pack(pady=10)

    def show_issued():
        clear_page()
        create_title("Выданные книги")
        table_frame = tk.Frame(page_frame, bg=BG)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = (
            "id", "title", "reader", "issue_date"
        )
        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=17
        )
        headings = {
            "id": "№ выдачи",
            "title": "Название книги",
            "reader": "Читатель",
            "issue_date": "Дата выдачи"
        }
        widths = {
            "id": 80,
            "title": 300,
            "reader": 250,
            "issue_date": 150
        }
        for column in columns:
            tree.heading(column, text=headings[column])
            tree.column(column, width=widths[column], anchor="center")
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        def load_issued():
            tree.delete(*tree.get_children())
            cursor.execute("""
                SELECT loans.id, books.title,
                       loans.reader, loans.issue_date
                FROM loans
                JOIN books ON books.id = loans.book_id
                WHERE loans.return_date IS NULL
                ORDER BY loans.id DESC
            """)
            for loan in cursor.fetchall():
                tree.insert("", "end", values=loan)
        load_issued()

        def return_book():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning(
                    "Внимание",
                    "Выберите выданную книгу!",
                    parent=window
                )
                return
            loan_id = int(
                tree.item(selected[0], "values")[0]
            )
            answer = messagebox.askyesno(
                "Возврат книги",
                "Подтвердить возврат выбранной книги?",
                parent=window
            )
            if answer:
                cursor.execute("""
                    UPDATE loans
                    SET return_date = ?
                    WHERE id = ? AND return_date IS NULL
                """, (date.today().isoformat(), loan_id))
                conn.commit()
                messagebox.showinfo(
                    "Успех",
                    "Книга успешно возвращена!",
                    parent=window
                )
                load_issued()
        buttons = tk.Frame(page_frame, bg=BG)
        buttons.pack(pady=10)
        create_button(
            buttons,
            "Вернуть книгу",
            return_book
        ).pack(side="left", padx=5)
        create_button(
            buttons,
            "Обновить",
            load_issued
        ).pack(side="left", padx=5)
        create_button(
            buttons,
            "Назад",
            show_home
        ).pack(side="left", padx=5)

    def close_program():
        answer = messagebox.askyesno(
            "Выход",
            "Вы действительно хотите закрыть программу?",
            parent=window
        )
        if answer:
            conn.close()
            window.destroy()
    page_frame = tk.Frame(
        window,
        bg=BG
    )
    page_frame.pack(
        fill="both",
        expand=True
    )
    window.protocol(
        "WM_DELETE_WINDOW",
        close_program
    )
    show_login()
    window.mainloop()

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
