# Uma função de filtro simples
def _filter(function, _list):
    newList = []
    for i in _list:
        if function(i):
            newList.append(i)
    return newList

_list = [i for i in range(10)]
print("List: ", _list)
even  = _filter(lambda x: x%2 == 0, _list)
print("Even: ", even)
odd = _filter(lambda x: not x%2 == 0, _list)
print("Odd: ", odd)