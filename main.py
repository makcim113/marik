import re


def numbers_reg(str2):
    st = re.fullmatch(r"(\d+)", str2)
    return st


numbers = []
strings = []


while True:

    str1 = input("Enter: ")
    if str1 == 'exit':
        print("Programm exit code")
        break
    elif numbers_reg(str1):
        numbers.append(str1)
    elif type(str1) == str:
        strings.append(str1)
print(numbers, strings)
