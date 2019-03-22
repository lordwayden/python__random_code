a = [3, 2, 5, 3, 9, 2, 9]
b = []

[b.append(x) for x in a if x not in b]
print(b)

c = set(a)
print(c)