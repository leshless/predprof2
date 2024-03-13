import csv

def read():
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
    file = open(path, "w")
    writer = csv.writer(file)

    for line in data:
        writer.writerow(line)

def shorten(fullname):
    surname, name, _ = fullname.split(" ")
    return list(name)[0] + ". " + surname

def search(data):
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
    data = read()
    search(data)


main()