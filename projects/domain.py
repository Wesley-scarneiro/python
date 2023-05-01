from decimal import Decimal

class DataTable:

    '''
        Classe que representa uma tabela.
        É possível criar uma tabela, adicionar colunas e referências com outras tabelas.
    '''

    def __init__(self, name):
        '''
            Construtor da classe DataTable.

            Args:
                name: nome da tabela
        '''
    
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, description):
        '''
            Adiciona colunas na tabela.
            
            Args:
                name: nome da coluna
                kind: tipo de dado da coluna (domínio)
                description: breve descrição da coluna
        '''

        column = Column(name, kind, description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        '''
            Estabelece uma relação entre a tabela atual e outra informada.
            A tabela atual é a que referencia a outra.

            Args.:
                name: nome da relação
                to: nome da outra tabela que participará da relação
                on: coluna que contém a chave primária da outra relação
        '''
        
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        '''
            Estabelece uma relação entre outra tabela e a atual.
            A tabela atual é ferenciada por outra.

            Args:
                name: nome da relação
                by: a outra tabela que referenciará a atual
                on: coluna que referencia a chave primária da atual com chave estrangeira.
        '''

        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)

class Column:
    '''
        Classe que representa uma coluna de uma tabela.
    '''

    def __init__(self, name, kind, description):
        '''
            Construtor da classe Column.

            Args:
                name: nome da coluna
                kind: tipo de dado da coluna (domínio)
                description: breve descrição da coluna
        '''
        self._name = name
        self._kind = kind
        self._description = description

    def __str__(self):
        _str = "Col: {} : {} {}".format(
                self._name, self._kind, self._description
        )
        return _str

class Relationship:
    '''
        Classe para representar as relações entre diferentes tabelas.
    '''

    def __init__(self, name, _from, to, on):
        '''
            Construtor da classe Relationship.

            Args:
                name: nome da relação
                from: tabela origem da relação
                to: tabela destino da relação
                on: coluna da tabela origem que guardará a relação
        '''

        self._name = name
        self._from = _from
        self._to = to
        self._on = on

class PrimaryKey(Column):
    """
        Classe para representar as chaves primárias das tabelas.
    """

    def __init__(self, table, name, kind, description=""):
        '''
            Construtor da classe PrimaryKey.

            Args:
                table: referência de uma DataTable.
                name: nome da coluna
                kind: tipo de dado (domínio)
                description: breve descrição da coluna
        '''

        super().__init__(name, kind, description=description)
        self._is_pk = True

    def validate(self, data):
        if self._kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif self._kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif self._kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True