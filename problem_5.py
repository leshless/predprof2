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

def hash(s, p = 67, m = 1000000009):
    s = list(s)
    sum = 0
    for i in range(len(s)):
        sum += (ord(s[i]) * pow(p, i)) % m

    return sum

def change_id(data):
    for i in range(1, len(data)):
        sum = hash(data[i][1])
        data[i][0] = sum

def main():
    """Точка входа программы.
    """
    data = read()
    change_id(data)
    write(data, "students_with_hash.csv")

main()