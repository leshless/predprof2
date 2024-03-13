import csv
import random

def read():
    """Открывает csv файл и считывает данные.
    """

    path = "students.csv"
    file = open(path)
    reader = csv.reader(file)

    data = []
    for line in reader:
        data.append(line)
    
    return data

    rows = []

    for obj in data:
        row = []
        for cell in obj:
            row.append(obj[cell])
        rows.append(row)

    return rows

def write(data, path):
    """Записывает данные в csv файл.

    data – данные для записи 
    path – путь к файлу для записи
    """

    file = open(path, "w")
    writer = csv.writer(file)

    for line in data:
        writer.writerow(line)

def format_login(fullname):
    """Возвращает имя в формате: Фамилия_ИО.

    fullname – полное имя
    """
    surname, name, parentname = fullname.split(" ")
    return surname + "_" + list(name)[0] + list(parentname)[0]

def generate_password():
    """Генерирует случайный пароль.
    """
    alph = ""
    for i in range(ord('0'), ord('9') + 1):
        alph += chr(i)
    for i in range(ord('a'), ord('z') + 1):
        alph += chr(i)
    for i in range(ord('A'), ord('Z') + 1):
        alph += chr(i)


    password = ""
    digits = False
    lower = False
    upper = False
    for i in range(8):
        char = alph[random.randint(0, len(alph)-1)]
        password += char

        digits = digits or ('0' <= char <= '9')
        lower = lower or ('a' <= char <= 'z')
        upper = upper or ('A' <= char <= 'Z')

    if digits and lower and upper:
        return password
    else:
        return generate_password()

def add_fields(data):
    """Добавляет к таблице поля с логином и паролем.

    data – данные таблицы
    """
    data[0].append("login")
    data[0].append("password")

    for i in range(1, len(data)):
        login = format_login(data[i][1])
        password = generate_password()
        data[i].append(login)
        data[i].append(password)

def main():
    """Точка входа программы.
    """
    data = read()
    add_fields(data)
    write(data, "students_password.csv")


main()