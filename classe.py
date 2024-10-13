class Cliente:
    def __init__(self, n, fone):
        
        self.nome = n
        self.telefone = fone

    # metodo get

    def get_nome(self):
        return self._nome
    
    # metodo set

    def set_nome(self, nome):
        self._nome = nome

c1 = Cliente("Jõao", "114444-2222")

print(c1)
print(c1.nome, " e ",c1.telefone)

class Conta:
    def __init__(self, titular, numero, saldo):
        
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativado!")
        else:
            self._saldo = saldo

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.nome,6565,0)

print(conta.titular," Número: ",conta.numero," Seu saldo: ",conta.saldo)