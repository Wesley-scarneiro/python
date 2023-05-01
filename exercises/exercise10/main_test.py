'''
    Módulo para executar os testes sem ser por linha de comando.
'''

import unittest

def main():
    # unittest.TestLoader(): retorna uma instância de carregamento dos testes
    # unittest.TestLoader().discover("exercise10"): carrega todos os testes que estão no diretório atual
    suite = unittest.TestLoader().discover("exercise10")

    # unittest.TextTestRunner(verbosity=2): retorna uma instancia de execução dos testes e
    # recebe verbosity=2 como argumento para realizar uma saída detalhada dos testes
    # unittest.TextTestRunner(verbosity=2).run(suite): executa todos os testes carregados em 'suite'
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

'''
test_validation_bool (test_case.TestTypeValidation) ... ok
test_validation_complex (test_case.TestTypeValidation) ... ok
test_validation_float (test_case.TestTypeValidation) ... ok
test_validation_int (test_case.TestTypeValidation) ... ok
test_validation_str (test_case.TestTypeValidation) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
'''