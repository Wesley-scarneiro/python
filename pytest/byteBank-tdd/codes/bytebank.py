from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario, cargo=None):
        self._nome = nome.strip().split()
        self._data_nascimento = data_nascimento.split("/")
        self._salario = salario
        self._cargo = cargo

    @property
    def nome(self):
        return self._nome[0]

    @property
    def salario(self):
        return self._salario

    def idade(self):
        ano_atual = date.today().year
        return ano_atual - int(self._data_nascimento[-1])

    # refatorado
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor <= 1000:
            return valor
        else:
            raise Exception("10% do salário do funcionário é maior do que R$ 1000")

    def __str__(self):
        return f'Funcionario({" ".join(self._nome)}, {"/".join(self._data_nascimento)}, {self._salario})'
    
    def sobreNome(self):
        return " ".join(self._nome[1:])
    
    # Implementação pós-teste
    def reduzir_salario(self) -> float | None:
        if self._salario >= 100000.0 and self._cargo == 'diretor':
            self._salario = self._salario - self._salario*0.1
            return self._salario
        return None
