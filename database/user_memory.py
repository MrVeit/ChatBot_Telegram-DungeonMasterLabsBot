import sqlite3
from aiogram import types
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к базе данных SQLite прошло успешно!")
    except Error as error:
        print(f"Обнаружена следующая ошибка: '{error}'")
    return connection


def database_connection(connection, query):
    cursor = connection.cursor()
    connection = create_connection("files/local_memory/username_info.db")
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно!")
    except Error as error:
        print(f"Обнаружена следующая ошибка: '{error}'")


def create_users_database(message: types.Message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id
    full_name_user = str(message.from_user.full_name)
    user_nickname = f"{full_name_user}"
    path = "files/local_memory/username_info.db"

    connection = create_connection(path)

    create_users_table = """CREATE TABLE IF NOT EXISTS username (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL,
                  nickname TEXT NOT NULL);
                  """
    create_connection(path)
    cursor = connection.cursor()
    connection = create_connection("files/local_memory/username_info.db")

    cursor.execute("SELECT count(*) "
                   "FROM username "
                   "WHERE user_id=?", (user_id,))
    data = cursor.fetchone()[0]

    if data == 0:
        print(f"Пользователь {full_name_user} не обнаружен в БД")
        print(f"Пользователь: {full_name_user} с ID {chat_id} был успешно записан в базу данных!")
        try:
            cursor.execute(create_users_table)
            connection.commit()
            print("Запрос выполнен успешно!")
        except Error as error:
            print(f"Обнаружена следующая ошибка: '{error}'")

        create_users = f"""
                INSERT INTO
                   username (user_id, nickname)
                VALUES
                   ({user_id}, '{user_nickname}');
                """
        database_connection(connection, create_users)
        connection.commit()
    else:
        print(f"Пользователь {full_name_user} обнаружен")


def sort_first_five_users():
    connection = create_connection("files/local_memory/username_info.db")
    cursor = connection.cursor()
    bad_chars = ['(', ')', ',']
    cursor.execute("SELECT id FROM username WHERE id<=6 ORDER BY id DESC")
    discount_users = str(cursor.fetchone())
    discount_users = filter(lambda i: i not in bad_chars, discount_users)
    discount_users = "".join(discount_users)
    print(f'Кандидатов на скидку в 30%: {discount_users}')
    return discount_users


def sort_current_users():
    connection = create_connection("files/local_memory/username_info.db")
    cursor = connection.cursor()
    bad_chars = ('[', ']')
    cursor.execute("SELECT * FROM username ORDER BY id ASC")
    current_users = str(cursor.fetchall())
    current_users = filter(lambda i: i not in bad_chars, current_users)
    current_users = "".join(current_users)
    return current_users


def read_current_users():
    connection = create_connection("files/local_memory/username_info.db")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM username")
    users_id = cursor.fetchall()
    print(f'Пользователи, авторизованные в системе: {users_id}')
    return users_id
