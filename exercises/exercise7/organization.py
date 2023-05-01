from typing import List
import abc

class Employee(abc.ABC):

    __slots__ = ["__name", "__gender", "__age", "__id", "__salary"]
    
    def __init__(self, name: str, gender: str, age: int, id: int, salary: float) -> None:
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__id = id
        self.__salary = salary

    def __str__(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def gender(self) -> str:
        return self.__gender
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def salary(self) -> float:
        return self.__salary
    
    def record(self):
        return f"Name: {self.__name}\nGender: {self.__gender}\nAge: {self.__age}\nID: {self.__id}\nSalary: {self.__salary}\n"
    
    abc.abstractmethod
    def bonus(self):
        pass

class Organization:

    __slots__ = ["__name", "__employees", "__totalEmployees", "__formerEmployees", "__totalFemployees"]

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__employees = []
        self.__totalEmployees = 0
        self.__formerEmployees = []
        self.__totalFemployees = 0
    
    def __str__(self) -> str:
        return self.__name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def totalEmployees(self) -> int:
        return self.__totalEmployees
    
    @property
    def employees(self) -> List[Employee]:
        return self.__employees
    
    @property
    def formerEmployees(self) -> List[Employee]:
        return self.__formerEmployees
        
    def add_employee(self, job: str, name: str, gender: str, age: int, id: int, salary: float) -> None:
        if job == "Analyst":
            employee = Analyst(name, gender, age, id, salary)
            self.__employees.append(employee)
            self.__totalEmployees += 1
        elif job == "Supervisor":
            employee = Supervisor(name, gender, age, id, salary)
            self.__employees.append(employee)
            self.__totalEmployees += 1
        else:
            raise ValueError(f"Job '{job}' does not exist'")
        
    def dimiss_employee(self, employee: Employee) -> bool:
        if isinstance(employee, Employee):
            if employee in self.__employees:
                self.__employees.remove(employee)
                self.__totalEmployees -= 1
                self.__formerEmployees.append(employee)
                self.__totalFemployees += 1
                return True
            else:
                return False
        else:
            raise ValueError(f"'{employee}' is not an instance of type 'Employee'")


class Analyst(Employee):
    
    __slots__ = ["__supervisor"]

    def __init__(self, name: str, gender: str, age: int, id: int, salary: float, idSupervisor: int):
        super().__init__(name, gender, age, id, salary)
        self.__supervisor = idSupervisor

    @property
    def supervisor(self):
        return self.__supervisor
    
    def bonus(self):
        return self.__salary*0.05

class Supervisor(Employee):
    
    __slots__ = ["__team"]

    def __init__(self, name: str, gender: str, age: int, id: int, salary: float):
        super().__init__(name, gender, age, id, salary)
        self.__team = Team("Team - " + name)

    @property
    def analysts(self) -> List[Analyst]:
        return self.__team.analysts
    
    @property
    def totalAnalysts(self) -> int:
        return self.__team.totalAnalyst
    
    def add_analyst(self, analyst: Analyst) -> None:
        try:
            self.__team.add_analysts(analyst)
        except ValueError as e:
            print(e)

    def remove_analyst(self, analyst: Analyst) -> bool:
        try:
            if self.__team.remove__analyst(analyst):
                return True
            else:
                return False
        except ValueError as e:
            print(e)

    def bonus(self):
        return self.__salary*0.10

class Team:
    
    __slots__ = ["__name", "__analysts", "__totalAnalysts"]

    def __init__(self, name):
        self.__name = name
        self.__analysts = []
        self.__totalAnalysts = 0

    def __str__(self) -> str:
        return self.__name

    @property
    def analysts(self) -> List[Analyst]:
        return self.__analysts
    
    @property
    def totalAnalyst(self) -> int:
        return self.__totalAnalysts
    
    def add_analysts(self, analyst: Analyst) -> None:
        if isinstance(analyst, Analyst):
            self.__analysts.append(analyst)
            self.__totalAnalysts += 1
        else:
            raise ValueError(f"'{analyst}' is not an instance of type 'Analyst'")
        
    def remove__analyst(self, analyst: Analyst) -> bool:
        if isinstance(analyst, Analyst):
            if analyst in self.__analysts:
                self.__analysts.remove(analyst)
                self.__totalAnalysts -= 1
                return True
            else:
                return False
        else:
            raise ValueError(f"'{analyst}' is not an instance of type 'Analyst'")
