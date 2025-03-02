# IMPORTAÇÕES NECESSÁRIAS PARA O FUNCIONAMENTO DO SISTEMA
import textwrap # Biblioteca para manipulação de textos
from abc import ABC, abstractmethod # Módulo para criar classes abstratas
from datetime import datetime # Biblioteca para manipular datas e horários

# CABEÇALHO DO PROGRAMA
print("======================================") 
print("    SISTEMA BANCÁRIO v2.0     ")  
print("======================================")
# FIM DO CABEÇALHO

# CLASSE ITERADOR PARA LISTAR CONTAS
class ContasIterador:
    def __init__(self, contas): 
        """Inicializa o iterador de contas."""
        self.contas = contas
        self._index = 0

    def __iter__(self):
        """Retorna o objeto iterador."""
        return self

    def __next__(self):
        """Retorna a próxima conta na iteração."""
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


class Cliente:
    def __init__(self, endereco):
        """Inicializa um cliente com endereço e lista de contas."""
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        """Realiza uma transação na conta do cliente."""
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma conta à lista de contas do cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """Inicializa uma pessoa física com nome, data de nascimento, CPF e endereço."""
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        """Inicializa uma conta com número, cliente, agência e histórico."""
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Cria uma nova instância de Conta."""
        return cls(numero, cliente)

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self._saldo

    @property
    def numero(self):
        """Retorna o número da conta."""
        return self._numero

    @property
    def agencia(self):
        """Retorna a agência da conta."""
        return self._agencia

    @property
    def cliente(self):
        """Retorna o cliente titular da conta."""
        return self._cliente

    @property
    def historico(self):
        """Retorna o histórico da conta."""
        return self._historico

    def sacar(self, valor):
        """Realiza um saque na conta."""
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

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """Inicializa uma conta corrente com número, cliente, limite e limite de saques."""
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        """Cria uma nova instância de ContaCorrente."""
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        """Realiza um saque na conta corrente, verificando limite e limite de saques."""
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        """Retorna uma representação em string da conta corrente."""
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        """Inicializa um histórico de transações."""
        self._transacoes = []

    @property
    def transacoes(self):
        """Retorna a lista de transações."""
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico."""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        """Gera um relatório de transações."""
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        """Retorna as transações do dia atual."""
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Transacao(ABC):
    """Classe abstrata que define uma transação."""

    @property
    @abstractmethod
    def valor(self):
        """Propriedade abstrata para obter o valor da transação."""
        pass

    @abstractmethod
    def registrar(self, conta):
        """Método abstrato para registrar a transação em uma conta."""
        pass

class Saque(Transacao):
    """Classe que representa um saque."""

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Registra o saque na conta e adiciona ao histórico se bem-sucedido."""
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    """Classe que representa um depósito."""

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Registra o depósito na conta e adiciona ao histórico se bem-sucedido."""
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

def log_transacao(func):
    """Decorador para registrar um log da transação com a data e hora."""
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope

def menu():
    """Exibe o menu de opções para o usuário."""
    opcoes = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(opcoes))

def filtrar_cliente(cpf, clientes):
    """Busca um cliente pelo CPF na lista de clientes."""
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    """Recupera a conta do cliente. Se houver mais de uma, retorna a primeira."""
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]

@log_transacao
def depositar(clientes):
    """Realiza um depósito para um cliente específico."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    """Realiza um saque para um cliente específico."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    """Exibe o extrato bancário de um cliente."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if conta:
        print("\n================ EXTRATO ================")
        extrato = "".join(
            f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
            for transacao in conta.historico.gerar_relatorio()
        )
        print(extrato if extrato else "Não foram realizadas movimentações")
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("==========================================")

@log_transacao
def criar_cliente(clientes):
    """Cria um novo cliente e adiciona à lista de clientes."""
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    """Cria uma nova conta para um cliente existente."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente, numero_conta, limite=500, limite_saques=3)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    for conta in contas:
        print("=" * 100)
        print(conta)

def main():
    """Função principal para execução do sistema bancário."""
    clientes = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida! @@@")

if __name__ == "__main__":
    main()
