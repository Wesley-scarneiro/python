def calc(x, y):
    if y:
        return (x+y, x-y, x*y, x/y)
    else:
        return (x+y, x-y, x*y)

print(calc(10, 5))
print(calc(25,0))