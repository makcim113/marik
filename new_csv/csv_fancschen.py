from Csv import *


def new_file():
    file_neme = input("Enter file name: ").strip()
    columns = input("Enter name columns ,: ")
    column = columns.split(',')
    new_colum = [col.strip() for col in column]
    file = New_csv(file_neme, new_colum)
    file.__init__(file_neme, new_colum)
    print("Create file with colums: ", file)
