from codes.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:

    # O começo do método precisa obrigatoriamente começar com 'test_'
    # É uma boa prática que o nome do método seja exageradamente verboso
    # @mark.skip
    def test_idade_13_03_2000_igual_22(self):
        input = '13/03/2000'    # given
        expected = 23
        funcionario = Funcionario('teste1', input, 5000)
        output = funcionario.idade()    # when
        assert output == expected       # then

    @mark.testar_nome
    def test_nome_wesley_silva_carneiro_igual_wesley(self):
        input = '  wesley silva  '
        expected = 'wesley'
        funcionario = Funcionario(input, '06/04/2000', 2000)
        output = funcionario.nome
        assert output == expected
    
    @mark.testar_nome
    def test_sobrenome_wesley_silva_carneiro_igual_silva_carneiro(self):
        input = '    Wesley silva carneiro  '
        expected = 'silva carneiro'
        funcionario = Funcionario(input, '13/03/1995', 1500)
        output = funcionario.sobreNome()
        assert output == expected

    
    # Usando a metodologia do TDD
    def test_reduzir_salario_100000_diretor_retorna_90000(self):
        input = 100000.0
        expected = 90000.0
        funcionario = Funcionario('Rosalin Franklin', '18/04/1950', input, 'diretor')
        output = funcionario.reduzir_salario()
        assert output == expected

    def test_reduzir_salario_100000_nao_diretor_retorna_None(self):
        input = 100000.0
        expected = None
        funcionario = Funcionario('Rosalin Franklin', '18/04/1950', input)
        output = funcionario.reduzir_salario()
        assert output == expected

    def test_reduzir_salario_100000_nao_diretor_retorna_None(self):
        input = 99999.0
        expected = None
        funcionario = Funcionario('Rosalin Franklin', '18/04/1950', input)
        output = funcionario.reduzir_salario()
        assert output == expected

    def test_calcular_bonus_1000_retorna_100(self):
        input = 1000
        expected = 100
        funcionario = Funcionario('Augusta Ada Byron', '13/05/1850', input)
        output = funcionario.calcular_bonus()
        assert output == expected
    
    # with pytest.raises(<exceçãoEsperada>)
    # Cria um contexto para a captura da exceção esperada
    def test_calcular_bonus_11000_retorna_exception(self):
        with pytest.raises(Exception):
            input = 11000
            funcionario = Funcionario('Augusta Ada Byron', '13/05/1850', input)
            output = funcionario.calcular_bonus()
            assert output

    # Outra forma...
    def test_calcular_bonus_11000_retorna_exception2(self):
        with pytest.raises(Exception) as e:
            input = 11000
            funcionario = Funcionario('Augusta Ada Byron', '13/05/1850', input)
            funcionario.calcular_bonus()
            assert str(e.value) == "10% do salário do funcionário é maior do que R$ 1000"
    
    # Removido do coverge
    '''
        def test_str(self):
        input = ['Alan Turing', '13/03/1920', 6000]
        expected = f'Funcionario({input[0]}, {input[1]}, {input[2]})'
        funcionario = Funcionario(input[0], input[1], input[2])
        output = funcionario.__str__()
        assert output == expected
    '''

    def test_salario_5000_retorna_5000(self):
        input = 5000
        expected = 5000
        funcionario = Funcionario('Augusta Ada Byron', '13/05/1850', input)
        output = funcionario.salario
        assert output == expected