from abc import ABC, abstractmethod
from datetime import datetime

# Definição da classe Cliente que gerencia o endereço e contas do cliente.
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço do cliente
        self.contas = []  # Lista para armazenar as contas do cliente

    # Método para realizar transações em uma conta
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Registra a transação na conta

    # Método para adicionar uma conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)  # Adiciona uma conta à lista de contas do cliente

# Classe PessoaFisica herda de Cliente e adiciona informações adicionais específicas de pessoas físicas
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente)
        self.nome = nome  # Nome do cliente
        self.data_nascimento = data_nascimento  # Data de nascimento do cliente
        self.cpf = cpf  # CPF do cliente

# Classe Conta que representa a conta bancária de um cliente
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial da conta
        self._numero = numero  # Número da conta
        self._agencia = "0001"  # Agência da conta
        self._cliente = cliente  # Cliente associado à conta
        self._historico = Historico()  # Histórico de transações da conta

    # Método para criar uma nova conta com o cliente e número fornecido
    @classmethod
    def no_conta(cls, cliente, numero):
        return cls(numero, cliente)  # Retorna uma nova conta associada ao cliente

    # Propriedade que retorna o saldo da conta
    @property
    def saldo(self):
        return self._saldo

    # Propriedade que retorna o número da conta
    @property
    def numero(self):
        return self._numero

    # Propriedade que retorna a agência da conta
    @property
    def agencia(self):
        return self._agencia

    # Propriedade que retorna o cliente associado à conta
    @property
    def cliente(self):
        return self._cliente

    # Propriedade que retorna o histórico de transações
    @property
    def historico(self):
        return self._historico

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        saldo = self.saldo  # Obtém o saldo atual da conta
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo
        if excedeu_saldo:
            print("\n --- Saldo Insuficiente! ---")
        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saldo
            print("\n *** Saque realizado com sucesso! ***")
            return True
        else:
            print("\n --- O valor informado é inválido! ---")
            return False

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor ao saldo da conta
            print("\n *** Depósito realizado com Sucesso! ***")
        else:
            print("\n --- O valor informado é inválido! ---")
            return False
        return True

# Classe ContaCorrente herda de Conta e adiciona limites para saques
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe pai (Conta)
        self.limite = limite  # Limite de crédito da conta
        self.limite_saques = limite_saques  # Número máximo de saques permitidos

    # Sobrescrita do método sacar para adicionar restrições específicas da Conta Corrente
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite  # Verifica se o valor do saque excede o limite
        excedeu_saques = numero_saques >= self.limite_saques  # Verifica se o número máximo de saques foi atingido

        if excedeu_limite:
            print("\n --- O valor do saque excedeu o limite. ---")
        elif excedeu_saques:
            print("\n --- Número máximo de saques excedido. ---")
        else:
            return super().sacar(valor)  # Chama o método sacar da classe pai (Conta)
        return False

    def __str__(self):
        return f"""\ 
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe Historico que armazena todas as transações realizadas
class Historico:
    def __init__(self):
        self._transacoes = []  # Lista para armazenar as transações

    @property
    def transacoes(self):
        return self._transacoes  # Retorna a lista de transações

    def adicionar_transacao(self, transacao, saldo_anterior, saldo_atual):
        # Adiciona uma transação ao histórico, incluindo o saldo antes e depois da transação
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),  # Corrigido o formato da data
                "saldo_anterior": saldo_anterior,
                "saldo_atual": saldo_atual
            }
        )

# Classe abstrata que define a estrutura das transações
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque que representa uma transação de saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do saque

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        saldo_anterior = conta.saldo  # Saldo antes da transação
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque na conta
        if sucesso_transacao:
            saldo_atual = conta.saldo  # Saldo após a transação
            conta.historico.adicionar_transacao(self, saldo_anterior, saldo_atual)  # Adiciona a transação ao histórico

# Classe Deposito que representa uma transação de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do depósito

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        saldo_anterior = conta.saldo  # Saldo antes da transação
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito na conta
        if sucesso_transacao:
            saldo_atual = conta.saldo  # Saldo após a transação
            conta.historico.adicionar_transacao(self, saldo_anterior, saldo_atual)  # Adiciona a transação ao histórico

# Função principal para interação com o usuário
def menu():
    clientes = []  # Lista para armazenar os clientes cadastrados

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar cliente")
        print("2. Criar conta corrente")
        print("3. Realizar transação")
        print("4. Exibir histórico")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            endereco = input("Endereço do cliente: ")

            cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
            clientes.append(cliente)  # Adiciona o cliente à lista

        elif opcao == "2":
            numero_conta = input("Número da conta: ")
            cliente_nome = input("Nome do cliente para associar a conta: ")
            cliente = next((c for c in clientes if c.nome == cliente_nome), None)

            if cliente:
                conta = ContaCorrente.no_conta(cliente, numero_conta)
                cliente.adicionar_conta(conta)  # Associa a conta ao cliente
                print(f"Conta {numero_conta} criada com sucesso para {cliente_nome}.")
            else:
                print("Cliente não encontrado.")

        elif opcao == "3":
            numero_conta = input("Número da conta para transação: ")
            cliente_nome = input("Nome do cliente para realizar a transação: ")
            cliente = next((c for c in clientes if c.nome == cliente_nome), None)

            if cliente:
                conta = next((c for c in cliente.contas if c.numero == numero_conta), None)
                if conta:
                    tipo_transacao = input("Tipo de transação (saque/deposito): ")
                    valor = float(input("Valor da transação: "))

                    if tipo_transacao == "saque":
                        transacao = Saque(valor)
                    elif tipo_transacao == "deposito":
                        transacao = Deposito(valor)
                    else:
                        print("Tipo de transação inválido.")
                        continue

                    cliente.realizar_transacao(conta, transacao)  # Realiza a transação
                else:
                    print("Conta não encontrada.")
            else:
                print("Cliente não encontrado.")

        elif opcao == "4":
            cliente_nome = input("Nome do cliente para exibir o histórico: ")
            cliente = next((c for c in clientes if c.nome == cliente_nome), None)

            if cliente:
                for conta in cliente.contas:
                    print(f"\nHistórico da conta {conta.numero} de {cliente_nome}:")
                    for transacao in conta.historico.transacoes:
                        print(f"Tipo: {transacao['tipo']} | Valor: {transacao['valor']} | Data: {transacao['data']} "
                              f"| Saldo Anterior: {transacao['saldo_anterior']} | Saldo Atual: {transacao['saldo_atual']}")
            else:
                print("Cliente não encontrado.")

        elif opcao == "5":
            print("Saindo...")
            break  # Encerra o programa

        else:
            print("Opção inválida!")

# Executa o menu principal
menu()
