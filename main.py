import re


def numbers_reg(str2):
    st = re.fullmatch(r"(\d+)", str2)
    return st


numbers = []
strings = []
new_arry = []

while True:

    str1 = input("Enter: ")
    if str1 == 'exit':
        print("Programm exit code")
        break
    elif numbers_reg(str1):
        numbers.append(str1)
    elif type(str1) == str:
        strings.append(str1)

j = 0
while j < len(strings):
    if len(numbers) <= j:
        strings[j] += "!"
        j += 1
    else:
        strings[j] += numbers[j]
        j += 1

print(strings)
