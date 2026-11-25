class cuenta:
    def __init__(self, saldo):
        self.saldo=saldo

    def depositar(self, cantidad):
        self.saldo+=cantidad

    def retirar(self,cantidad):
        if cantidad<=self.saldo:
            self.saldo-=cantidad
        else:
            print("Saldo insuficiente")