t = (10, 20, 30, "Python")
print(t)
print(type(t))

a = t[0]
b = t[1]
print(a)
print(b)

a, b, c, d = t
print(a, b, c, d)

aList = [10, 20, 30, "python"]

h, i, j, k = aList
print(aList)

t = (1, 2, 3)

print("====================")
s = set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

t = tuple(l)
print(t, type(t))


