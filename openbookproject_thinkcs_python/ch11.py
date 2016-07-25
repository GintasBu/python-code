def swap(x, y):      # incorrect version
     print  "before swap statement: id(x):", id(x), "id(y):", id(y)
     x, y = y, x
     print  "after swap statement: id(x):", id(x), "id(y):", id(y)

a, b = 0, 1
print  "before swap function call: id(a):", id(a), "id(b):", id(b)
swap(a, b)
print  "after swap function call: id(a):", id(a), "id(b):", id(b)