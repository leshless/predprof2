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

def remind(data):
    """Выводит информацию о проекте Хадарова Владимира.

    data – данные таблицы
    """

    name = "Хадаров Владимир"

    for row in data:
        if name in row[1]:
            print(f"Ты получил: {row[4]}, за проект - {row[2]}")
            return
        
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

def main():
    """Точка входа программы.
    """
    data = read()
    remind(data)
    fix(data)
    write(data, "student_new.csv")


main()