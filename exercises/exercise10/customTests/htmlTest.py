import unittest

# Define o corpo da página
HTML = '''\
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Unittest output</title>
    </head>
    <body>
        <table>
            {}
        </table>
    </body>
</html>
'''

# Define uma linha e uma célula na tabela se o teste está ok ou se deu erro
OK_TD = "<tr><td style='color:green;'>{}</td></tr>"
ERR_TD = "<tr><td style='color:green;'>{}</td></tr>"

class HTMLTestResult(unittest.TestResult):
    
    '''
        Inicializa a classe que registrará os testes.
        self.runner: objeto que executará os testes, uma instancia de HTMLTestRunner
        self.infos: uma lista que armazena os dicionários que contém os dados de cada teste.
        self.current: os dados de um teste (id e result) são armazenados temporariamente como um dicionário.
    '''
    def __init__(self, runner):
        unittest.TestResult.__init__(self)
        self.runner = runner
        self.infos = []
        self.current = {}

    '''
        Salva os dados de um teste, contidos no dicionário, e os armazena na lista.
        O dicionário da classe é esvaziado para o próximo teste utilizá-lo.
    '''
    def newTest(self):
        self.infos.append(self.current)
        self.current = {}
    
    def startTest(self, test):
        self.current['id'] = test.id()

    def addSuccess(self, test):
        self.current['result'] = 'ok'
        self.newTest()
    
    def addError(self, test):
        self.current['result'] = 'error'
        self.newTest()
    
    def addFailure(self, test):
        self.current['result'] = 'fail'
        self.newTest()
    
    def addSkip(self, test, err):
        self.current['result'] = 'skipped'
        self.current['reason'] = err
        self.newTest()

class HTMLTestRunner:

    def run(self, suite):
        result = HTMLTestResult(self)
        suite.run(result)
        dataTable = ''
        for item in result.infos:
            if item['result'] == 'ok':
                dataTable += OK_TD.format(item['id'])
            else:
                dataTable += ERR_TD.format(item['id'])
        global HTML
        HTML = HTML.format(dataTable)
        return result
    

if __name__ == "__main__":
    suite = unittest.TestLoader().discover("exercise10")
    HTMLTestRunner().run(suite)
    with open('unittestOutput.html', "w") as file:
        file.write(HTML)