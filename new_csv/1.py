a = [1, 4, 6, 2, 7, 8, 9, 10, 17, 13, 1, 3, 4]

new_arry = []
c = []
b = []
j = 0
for li in a:
    if li < 10:
        b.append(li)
    elif li > 10:
        c.append(li)
    if j < len(a):
        new_arry.append(a[j] * 10)
        j += 1
print(b, c, new_arry)
