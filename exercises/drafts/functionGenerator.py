# Função geradora
def numbers():
    for i in range(10):
        yield i

_list = []
for i in numbers():
    _list.append(i)
print(_list)


'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''