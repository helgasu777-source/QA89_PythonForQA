import csv

def read_students("students.csv")
def read_students():
    with open("students.csv","r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']} ({row['age']})")
read_students()