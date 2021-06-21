a = [1, 4, 6, 2, 7, 8, 9, 10, 17, 13, 1, 3, 4]

c = []
b = []
for li in a:
    if li < 10:
        b.append(li)
print(b)

for li1 in a:
    if li1 > 10:
        c.append(li1)
print(c)

a = [i * 10 for i in a]
print(a)
