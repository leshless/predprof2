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

def fix(data):
    """Заменяет отсутствующие поля с отметками за проект на среднее значение по всем ученикам.

    data – данные таблицы
    """

    sum = 0
    num = 0

    for i in range(1, len(data)):
        if data[i][4] != "None":
            sum += int(data[i][4])
            num += 1
    
    mean = str(round(sum / num, 3))

    for i in range(1, len(data)):
        if data[i][4] == "None":
            data[i][4] = mean 

def insertion_sort(data):
    """Сортирует список учеников по убыванию оценки за проект.

    data – данные таблицы
    """
    for i in range(1, len(data)):
        for j in range(i-1, 0, -1):
            if float(data[j][4]) < float(data[j+1][4]):
                data[j+1], data[j] = data[j], data[j+1]

def shorten(fullname):
    """Возвращает имя в формате: И. Фамилия.

    fullname – полное имя
    """
    surname, name, _ = fullname.split(" ")
    return list(name)[0] + ". " + surname

def find(data):
    """Выводит результаты трех лучших десятиклассников за проект.

    data – данные таблицы
    """
    grade10 = []
    
    for row in data:
        if "10" in row[3]:
            grade10.append(row)

    print("10 класс:")
    for i in range(3):
        fullname = grade10[i][1]
        shortname = shorten(fullname)

        print(f"{i+1} место: {shortname}")

def main():
    """Точка входа программы.
    """
    data = read()
    
    fix(data)
    insertion_sort(data)
    find(data)

    


main()