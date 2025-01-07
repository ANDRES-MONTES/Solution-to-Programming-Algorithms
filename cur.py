class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def saludar(self):
        print(f'hola mi nombre es {self.name}')
        
      
class BankAccout:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self.is_active = True
        
    def depositar(self, amount):
        if self.is_active:
            self.balance += amount  
            print(f'se ha depositado {amount}, para un total de {self.balance}')

        else:
            print('no se puede depositar cuneta inactiva')
            
    def retirar(self, retiro):
        if self.is_active:
            if retiro <= self.balance:
                self.balance -= retiro
                print(f'su nuevo balance es {self.balance} se retiro {retiro}')
            else:
                print('cuenta inactiva')
    
    def deactivat(self):
        self.is_active = False
        print('se desactivo la cuenta')
        
    def activat(self):
        self.is_active = True
        print('se activo la cuenta')
        
    
            
account_1 = BankAccout('andres', 100000)
account_2 = BankAccout('laura', 500)


account_1.depositar(10)
account_1.retirar(500)
account_1.deactivat()
account_1.depositar(10)
account_1.retirar(20)
