class Person:
    '''
        Classe para representar uma pessoa.
        
        Atributos:
            - name
            - age
            - gender
            - CPF
            - interests
        
        Métodos:
            - greeting
            - add_interests
            - __str__ : retornar name, age, gender e cpf
    '''

    # Aytributo de classe (estático)
    _totalPeople = 0

    # Construtor da classe
    def __init__(self, name, age, gender, cpf):
        self._name = name
        self._age = age
        self._gender = gender
        self._cpf = cpf
        self._interests = []
        Person._totalPeople += 1
    
    # Método estático, com decorador.
    @classmethod
    def getTotalPeople1(cls):
        print(f"The number of people = {cls._totalPeople}")

    # Outra forma, para o mesmo resultado.
    @staticmethod
    def getTotalPeople2():
        print(f"The number of people = {Person._totalPeople}")
    
    # Saudação
    def greeting(self):
        if self._interests:
            print(f"Hello, my name is {self._name}!\nI have {self._age} years old.\nMy interests are: {self._print_interests()}")
        else:
            print(f"Hello, my name is {self._name}\nI have {self._age} years old.")
    
    # Retorna a lista de interesses por extenso.
    def _print_interests(self):
        size = len(self._interests)
        _str = ""
        for index, interest in enumerate(self._interests):
            if index == size - 1:
                _str += interest + "."
            elif index == size - 2:
                _str += interest + " and "
            else:
                _str += interest + ", "
        return _str

    # Adiciona intereses pessoais
    # Pode receber um interesse ou vários simultaneamente, como uma lista.
    def add_interests(self, *args):
        for interest in args:
            self._interests.append(interest)

    # Imprime os dados pessoais de uma pessoa
    # Sobrescrevendo o método padrão __str__ do objeto.
    def __str__(self):
        _str = f"Name: {self._name}\nAge: {self._age}\nGender: {self._gender}\nCPF: {self._cpf}"
        return _str

class Teacher(Person):
    '''
        Classe para representar um professor.
        Herda os atributos e métodos de Person.

        Atributos próprios: universidade que trabalha, lista de disciplinas que leciona e tempo de experiência.

        Métodos pŕoprios:
            - presentation_professional
            - add_disciplines
            - setUniversityWork
    '''

    def __init__(self, name, age, gender, cpf, universityWork, timeExp):
        super().__init__(name, age, gender, cpf)
        self._disciplines = []
        self._universityWork = universityWork
        self._timeExp = timeExp

    # Apresentação profissional.
    def professional_greeting(self):
        _str = f'''Hello, my name is {self._name}.
        I am teacher, have {self._timeExp} years of experience and work at {self._universityWork}.'''
        if self._disciplines: 
            _str += f"\nCurrently I teach: {self._print_disciplines()}"
        print(_str)

    # Imprime as disciplinas que um prof. leciona por extenso.
    def _print_disciplines(self):
        size = len(self._disciplines)
        _str = ""
        for index, discipline in enumerate(self._disciplines):
            if index == size - 1:
                _str += discipline + "."
            elif index == size - 2:
                _str += discipline + " and "
            else:
                _str += discipline + ", "
        return _str

    # Adiciona novas disciplinas que o prof. pode lecionar.
    # Pode receber uma ou mais disciplinas ao mesmo tempo.
    def add_disciplines(self, *args):
        for disciplines in args:
            self._disciplines.append(disciplines)        