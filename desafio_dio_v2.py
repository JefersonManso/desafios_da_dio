# Importações
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\            
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.contas):
            raise StopIteration
        conta = self.contas[self._index]
        self._index += 1
        return f"""
        Agência:\t{conta.agencia}
        Número:\t\t{conta.numero}
        Titular:\t{conta.cliente.nome}
        Saldo:\t\tR$ {conta.saldo:.2f}
        """
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif valor > 0:
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return False
def sacar(self, valor):
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

    if valor > self.saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        return False

    self._saldo -= valor
    print("\n=== Saque realizado com sucesso! ===")
    return True
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
def adicionar_transacao(self, transacao):
    self._transacoes.append(
        {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
    )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    if len(cliente.contas) == 1:
        return cliente.contas[0]

    print("\nSelecione a conta:")
    for i, conta in enumerate(cliente.contas, 1):
        print(f"{i} - Conta {conta.numero} (Saldo: R$ {conta.saldo:.2f})")

    while True:
        try:
            escolha = int(input("Digite o número da conta desejada: ")) - 1
            return cliente.contas[escolha] if 0 <= escolha < len(cliente.contas) else None
        except (ValueError, IndexError):
            print("\n@@@ Escolha inválida. Tente novamente. @@@")
