number = [3, 6, 9, 56, 66, 78, 102, 45, 69, 56, 2]

x = 0
while x < len(number):
    if number[x] % 3 == 0:
        print(number[x])
    x += 1

