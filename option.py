import csv
import os

FILE = "films.csv"


# Read notes from .csv file and print to console
def read_notes(FILE):
    with open(FILE, encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            print("Film name:", row[0], '\n'
                  "Rating:", row[1], '\n',
                  "Note:", row[2], '\n')


# Add note to .csv file
def add_note(FILE, name, rate, note):
    with open(FILE, mode='a', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator="\r")
        file_writer.writerow([name, rate, note])
    print("Added to notes")


# Remove note from .csv file
def remove_note(FILE, name):
    with open(FILE) as prev, open("edited.csv", mode='w') as new:
        file_writer = csv.writer(new, lineterminator="\r", delimiter=';')
        file_reader = csv.reader(prev, delimiter=";")
        for row in file_reader:
            if row[0] != name:
                file_writer.writerow(row)
    os.remove(FILE)
    os.rename('edited.csv', FILE)
    print("File was updated")


# Get films with the highest,lowest rating and avg
def rating(FILE):
    with open(FILE, encoding="utf-8") as file:
        marks = []
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            marks.append(float(row[1]))

    with open(FILE, encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            if float(row[1]) == max(marks):
                print("Film '{0}' has the highest rating {1};".format(row[0], row[1]))
            if float(row[1]) == min(marks):
                print("Film '{0}' has the lowest rating {1};".format(row[0], row[1]))
        print("Average film rating is {0}. Rating among {1} films.".format(sum(marks)/len(marks),len(marks)))


if __name__ == '__main__':
    read_notes(FILE)
    add_note(FILE, "Good film", "3.4", "Very good")
    remove_note(FILE, "Good film")
    rating(FILE)
