a = ['a', 'b', 'c', 'd', 'e']
b = ['i', 'k', 'l', 'm', 'n']

x = 0
c = 0
a = [i[x] + j[c] for i in a for j in b]
x += 1
c += 1
print(a)
