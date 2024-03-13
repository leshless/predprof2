import csv
import random

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

def format_login(fullname):


def generate_password():
    alph = ""


def main():
    data = read()
    search(data)


main()