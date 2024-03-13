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

def remind(data):
    name = "Хадаров Владимир"

    for row in data:
        if name in row[1]:
            print(f"Ты получил: {row[4]}, за проект - {row[2]}")
            return
        
def fix(data):
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
    data = read()
    remind(data)
    fix(data)
    write(data, "student_new.csv")


main()