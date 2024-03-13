import csv

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

def shorten(fullname):
    """Возвращает имя в формате: И. Фамилия.

    fullname – полное имя
    """
    surname, name, _ = fullname.split(" ")
    return list(name)[0] + ". " + surname

def search(data):
    """Осуществляет интерактивное взаимодействие с поиском по id проекта.

    data – данные таблицы
    """
    while True:
        id = input()

        if id == "СТОП":
            break
        
        found = False
        for row in data:
            if row[2] == id:
                print(f"Проект №{row[2]} делал: {shorten(row[1])} он(а) получил(а) оценку - {row[4]}.")
                found = True
        
        if not found:
            print("Ничего не найдено.")

def main():
    """Точка входа программы.
    """
    data = read()
    search(data)


main()