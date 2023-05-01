from datetime import date

class Bank:
    '''
        Class that represents a bank.

         Attributes:
                 * Bank name
                 * Total registered customers
                 * List of registered customers
                 *Total bank balance
                 * Log file name
         Methods:
             * register customers
             * Cancellation of customer accounts
             * Customer account upgrade
             * register logs
    '''

    def __init__(self, name):
        self.__name = name
        self.__clientList = {}
        self.__totalClients = 0
        self.__fileName = "log_" + name + ".txt"

    def __str__(self):
        return self.__name

    # Realiza a escrita no arquivo de log
    def _writeLog(self, log:str):
        with open(self.__fileName, "a") as file:
            file.write(log + "\n")


    # Registra os clientes e grava no log
    def add_client(self, cls, name, numberAccount, typeAccount):
        if typeAccount == "SalaryAccount":
            client = SalaryAccount(cls, name, numberAccount)
            log = f"Number account {numberAccount} - {typeAccount} registered"
            self.__totalClients += 1
            self.__clientList[numberAccount] = client
            self._writeLog(log)
            return client
        elif typeAccount == "CheckingAccount":
            client = CheckingAccount(cls, name, numberAccount)
            log = f"Number account {numberAccount} - {typeAccount} registered"
            self.__totalClients += 1
            self.__clientList[numberAccount] = client
            self._writeLog(log)
            return client
        else:
            log = f"Number account {numberAccount} - (??){typeAccount}(??) not registered"
            self._writeLog(log)
            return None


    # Cancela a conta de um cliente, se ele existir
    def cancel_account(self, numberAccount):
        if numberAccount in self.__clientList:
            self.__clientList.pop(numberAccount)
            self.__totalClients -= 1
            log = f"Number account {numberAccount} removed"
            self._writeLog(log)
        else:
            log = f"Number account {numberAccount} not exist for be removed"
            self._writeLog(log)

    # Realiza o upgrade de conta
    # O upgrade só pode ser feito na SalaryAccount
    def upgrade_account(self, numberAccount):
        if numberAccount in self.__clientList:
            client = self.__clientList[numberAccount]
            if type(client) is SalaryAccount:
                newClient = CheckingAccount.upgrade_account(client)
                self.__clientList[numberAccount] = newClient
                log = f"Number account {numberAccount} updated for checking-account"
                self._writeLog(log)
                return newClient
            else:
                log = f"Number account {numberAccount} is already a checking-account"
                self._writeLog(log)
                return client
    
    def client_exist(self, numberAccount):
        return numberAccount in self.__clientList

    def get_client_object(self, numberAccount):
        if numberAccount in self.__clientList:
            return self.__clientList[numberAccount]
        else:
            return None
    
    def print_clients(self):
        log = str(len(self.__clientList)) + " clients registered:\n"
        for client in self.__clientList.values():
            log += "\t" + str(client.numberAccount) + "\t" + client.name + "\n"
        self._writeLog(log)

    @property
    def totalBalance(self):
        total = 0.0
        for client in self.__clientList.values():
            if type(client) is SalaryAccount:
                total += client.balance
            else:
                total += client.totalBalance
        return total
    
    @property
    def totalclient(self):
        return self.__totalClients

# balance - setter e getter - instancia e classe
class SalaryAccount:
    '''
        SalaryAccount: bank salary account, with basic services.
            
            Attributes:
                * Name
                * Account number
                * Transaction history
            Methods:
                * Make deposit
                * Perform withdrawal
                * Perform transfer
                * Print transaction history
    '''

    def __init__(self, bank: Bank, name: str, numberAccount: int):
        self.__name = name
        self.__numberAccount = numberAccount
        self.__balance = 0.0
        self.__transactions = []
        self.__bank = bank
    
    def __str__(self):
        return self.__numberAccount

    @property
    def name(self):
        return self.__name
    
    @property
    def numberAccount(self):
        return self.__numberAccount
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def _balance(self, value):
        self.__balance = value
    
    @property
    def bank(self):
        return self.__bank
    
    @property
    def _transactions(self):
        return self.__transactions
    
    @_transactions.setter
    def _transactions(self, transaction):
        self.__transactions = transaction
    
    def print_transactions(self):
        log = f"Printing the transactions of customer {self.__numberAccount}:\n"
        for transaction in self.__transactions:
            log += "\t" + transaction + "\n"
        self.__bank._writeLog(log)
    
    def deposit(self, value):
        if value > 0:
            self.__balance += value
            self.__transactions.append((str(date.today()) + f": +R$ {float(value)}"))
            log = f"Deposit of R$ {float(value)} made successfully in the account {self.__numberAccount}"
            self.__bank._writeLog(log)
    
    def _deposit_by_transfer(self, value):
            self.__balance += value
            self.__transactions.append((str(date.today()) + f": +R$ {float(value)}"))
            log = f"Transfer of R$ {float(value)} received successfully in the account {self.__numberAccount}"
            self.__bank._writeLog(log)
    
    def withdraw(self, value):
        if value > 0 and value <= self.__balance:
            self.__balance -= value
            self.__transactions.append((str(date.today()) + f": -R$ {float(value)}"))
            log = f"Withdraw of R$ {float(value)} made successfully in the account {self.__numberAccount}"
            self.__bank._writeLog(log)

    def transfer(self, value, numberAccount):
        if value > 0 and value <= self.__balance:
            if self.__bank.client_exist(numberAccount):
                recipient = self.__bank.get_client_object(numberAccount)
                self.__balance -= value
                self.__transactions.append((str(date.today()) + f": -R$ {float(value)}"))
                recipient._deposit_by_transfer(value)
                log = f'Transfer of R$ {value} of the account {self.__numberAccount} for {numberAccount} made successfully'
                self.__bank._writeLog(log)
            else:
                log = f"The account {numberAccount} does not exist for made the transfer"
                self.__bank._writeLog(log)

# balance - setter e getter - instancia e classe
class CheckingAccount(SalaryAccount):

    '''
        CheckingAccount: bank current account, with basic and specialized services,
            
             Attributes:
                 * Balance in investments
                 
             Methods:
                 * Make investments
    '''
    
    def __init__(self, bank: Bank, name: str, numberAccount: int):
        super().__init__(bank, name, numberAccount)
        self.__investimentBalance = 0.0

    @property
    def totalBalance(self):
        return (self.balance + self.__investimentBalance)

    @property
    def investimentBalance(self):
        return self.__investimentBalance
    
    @classmethod
    def upgrade_account(cls, client: SalaryAccount):
        newClient = cls(client.bank, client.name, client.numberAccount)
        newClient._transactions = client._transactions
        newClient._balance = client._balance
        return newClient

    def make_investiment(self, value):
        if value > 0 and value <= self.balance:
            self._balance -= value
            self.__investimentBalance += value
            self._transactions.append(str(date.today()) + f": ^R$ {float(value)}")
            log = f"Investiment of R$ {float(value)} made successfully in the account {self.numberAccount}"
            self.bank._writeLog(log)