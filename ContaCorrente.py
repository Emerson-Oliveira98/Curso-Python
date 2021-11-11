class ContaCorrente:
    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._saldo = 0

    def _checar_saldo(self, valor):
        return self._saldo >= valor

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False

    def obter_saldo(self):
        return self._saldo

class ContaPF(ContaCorrente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

    def solicitar_emprestimo(self, valor):
        return self.obter_saldo() >= 500

class ContaPJ(ContaCorrente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def sacar_emprestimo(self, valor):
        return valor <= 5000

conta_pf1 = ContaPF("João",'111.111.111-11')
conta_pf1.depositar(1000)
print('Saldo atual é', conta_pf1.obter_saldo())
print('Receberá emprestimo = ', conta_pf1.solicitar_emprestimo(2000))

conta_pf1.sacar(800)
print('Saldo Atual é', conta_pf1.obter_saldo())
print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))








