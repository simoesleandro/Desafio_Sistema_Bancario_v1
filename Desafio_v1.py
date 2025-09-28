from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereço = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero,cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia    

    @property
    def cliente(self):
        return self._cliente    

    @property    
    def historico(self):
        return self._historico      

    def sacar(self, valor):
        saldo = self.saldo
        execeu_saldo = valor > saldo

        if execeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo-= valor
            print("\n === Saque realizado com sucesso===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False        

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False        

    def ContasCorrente(Conta):
        def __init__(self, numero, cliente, limite=500, limite_saques=3):
            super().__init__(numero, cliente)
            self.limite = limite
            self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao[tipo] == Saque.__name__]
        )
        execedeu_limite = valor > self.limite
        execedeu_saques = numero_saques >= self.limite_saques

        if execedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif execedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            return super().sacar(valor)
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/c:\t\t{self.numero}   
            Titular:\t{self.cliente.nome}
            """
    class Historico:
        def __init__(self):
            self.transacoes = []

        @property
        def transacoes(self):
            return self._transacoes

        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                    "tipo": transacao.__class__.__name__,
                    "valor": transacao.valor,
                    "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                }
            )

        def Saque(Transacao):
            def __init__(self, valor):
                self.valor = valor

            @property
            def valor(self):
                return self._valor

            def registrar(self, conta):
                sucesso_transacao = conta.sacar(self.valor)
                if sucesso_transacao:
                    self.conta.adicionar_transacao(self)


        def Deposito(Transacao):
            def __init__(self, valor):
                self.valor = valor

            @property
            def valor(self):
                return self._valor

            def registrar(self, conta):
                sucesso_transacao = conta.depositar(self.valor)
                if sucesso_transacao:
                    self.conta.adicionar_transacao(self)

        def __str__(self):
            return f"""\
                Tipo:		{self.tipo}
                Valor:		{self.valor}
                Data:		{self.data}
                """                        