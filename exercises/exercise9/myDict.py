from collections import UserDict
from typing import Union

class MyDict(UserDict):

    def __contains__(self, key: str) -> bool:
        return str(key) in self.data
    
    def __setitem__(self, key: str, value: Union[int, float, str]) -> None:
        self.data[str(key)] = value

    def get(self, key: str, default=None):
        return super().get(str(key), default)
    

def main():
    dct = MyDict(apple="maça", pineapple="abacaxi", strawberry="morango")
    dct[12] = "december"
    print(dct)

if __name__ == "__main__":
    main()

'''
{'apple': 'maça', 'pineapple': 'abacaxi', 'strawberry': 'morango', '12': 'december'}
'''