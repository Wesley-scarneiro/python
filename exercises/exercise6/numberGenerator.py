import random
from typing import List, Dict, Union
from math import pow

class NumberGenerator:

    def __init__(self, total, digit):
        self.__total = total
        self.__digits = digit if digit else 1
        self.__file1 = f"1_{total}_{digit}"
        self.__file2 = f"2_{total}_{digit}"
        self.__file3 = f"3_{total}_{digit}"
        self._start()

    # Create the file
    def _create_file(self, fileName: str, numbers: Union[List[int], Dict[int, int]]) -> None:
        try:
            if fileName == self.__file1 or fileName == self.__file3:
                content = f"{len(numbers)}\n"
                content += "\n".join(map(str, numbers))
                with open(fileName, "w") as file:
                    file.write(content)
                print(f"File '{fileName}' created successfully")
            else:
                with open(fileName, "w") as file:
                    for key, value in numbers.items():
                        file.write(f"{key} -> {value}\n")
                print(f"File '{fileName}' created successfully")
        except Exception:
            print("Error when creating the file")

    # Generates random numbers
    def _numbers_generate(self) -> List[int]:
        numbers = []
        min = pow(10, self.__digits - 1)
        max = pow(10, self.__digits) - 1
        for _ in range(self.__total):
            number = random.randint(min, max)
            numbers.append(number)
        return numbers
    
    def _count_duplicates(self, numbers: List[int]) -> Dict[int, int]:
        numbers_dict = {}
        for i in set(numbers):
            numbers_dict[i] = numbers.count(i)
        return numbers_dict
    
    def _remove_duplicates(self, numbers: List[int]) -> List[int]:
        numbers = list(set(numbers))
        return numbers
    
    def _start(self):
        numbers = self._numbers_generate()
        self._create_file(self.__file1, numbers)
        numbersDuplicates = self._count_duplicates(numbers)
        self._create_file(self.__file2, numbersDuplicates)
        numbersNoDuplicates = self._remove_duplicates(numbers)
        self._create_file(self.__file3, numbersNoDuplicates)

