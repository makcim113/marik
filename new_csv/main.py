from csv_fancschen import *

if __name__ == '__main__':
    arry_comand = ['save_file', 'new_fail', 'open_file', 'delit_file']
    print("Команды программы: ", arry_comand)
    while True:
        str1 = input('Введите команду: ').strip()
        if str1 == 'exit':
            print("Exit")
            break
        elif str1 == arry_comand[1]:
            print("Выполнилась команда: ", new_file())
