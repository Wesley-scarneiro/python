class Person():

    '''
    Crie uma classe que represente uma pessoa.
    Atributos: nome, gênero e idade.
    Métodos: apresentação pessoal, dados pessoais, interesses e métodos para manipulação e alteração dos dados.
    '''

    def __init__(self, name, gender, age, interests):

        '''
        Construtor da classe
        'self' é uma referência explícita de uma instância da classe (objeto criado).
        Os atributos são criados dinâmicamente quando o construtor é chamado.
        Atributos com '_atributo', por convenção, são privados e só podem ser acessados via métodos.
        '''

        self._name = name
        self._gender = gender
        self._age = age
        self._interests = interests
    
    # Imprindo os dados pessoais
    def getData(self):
        print("Name: {}\nGender: {}\nAge: {} years old".format(self._name, self._gender, self._age))

    # Exemplo de get
    def getInterests(self):
        return self._interests

    # Exemplo de get com decorator
    @property
    def interests(self):
        return self._interests

    # Adiciona novas coisas que uma pessoa se interessa.
    # Se na instanciação do objeto foi informado somente um único interesse, é preciso
    # converter o atributo '_interests' para uma lista.
    def add_interests(self, interest):
        if type(self._interests) == list:
            self._interests.append(interest)
        else:
            temp = self._interests
            self._interests = [temp, interest]

    # Verifica se uma pessoa possui interesse em um determinado assunto informado.
    # Retorna um valor booleano.
    def contains_interests(self, interest):
        if interest in self._interests:
            return True
        else:
            return False

    # Apresentação pessoal
    def greetings(self):
        print("Hello, my name is {}!\nI have {} years old\nMy interests are: {}".format(self._name, self._age, self._interests))

# Função main
def main():
    p = Person("Wesley", "male", 27, "Programming")
    p.getData()
    p.greetings()
    p.add_interests("Python")
    p.add_interests("IA")
    p.greetings()
    print("Contains the informed interest" if p.contains_interests("Java") else "Not contains the informed interest")   
if __name__ == "__main__":
    main()
