# autor: @Gustavo (GH)

# importação de bibliotecas
from datetime import datetime
import random

class Saque:
    # parâmetros
    def __init__(self, saldo):
        self.saldo = saldo
        self.saques_realizados = 0
        self.limite_saque = 3

    # função de saque
    def saque(self):
        if self.saques_realizados >= self.limite_saque:
            print('Limite de saque (3/3) atingido. \n')
            return

        print("\nVocê está na aba SAQUE")
        valor = float(input('Qual o valor do saque: R$'))

        if valor > 500:
            print('Seu limite de saque é de R$500')

        elif valor <= 0:
            print('Não é possível fazer saque para valores negativos')

        elif valor > self.saldo:
            print('Não possui saldo suficiente, faça um deposito')
            return # voltar ao menu

        else:
            self.saldo -= valor
            self.saques_realizados += 1
            print(f'Saque realizado no valor de R${valor}')
            print(f'Seu saldo atual R${self.saldo}')
            print(f'Saques realizado: {self.saques_realizados}/3\n')

    # função para executar o saque e fazer as verficações dentro dos parâmetros
    def executar_saque(self):
        while self.saques_realizados < self.limite_saque:
            self.saque()
            continuar = input('Deseja fazer outro saque? (s/n): ').lower() # veficicar se deseja sair do loop
            if continuar != 's':
                break

def depositar(saldo):
    print('\nVocê está na aba de Deposito')

    valor = float(input('Qual o valor do deposito: R$'))

    if valor > 0:
        saldo += valor
        print(f'\nDeposito de R${valor} realizado \nEsse valor vai estar em sua conta em até 10 min')
    else:
        print('Não é possível fazer deposito de valores negativos')
    
    return saldo

# Validar CPF
def validar_cpf(cpf):
    # verificar se CPF tem 11 digitos
    return cpf.isdigit() and len(cpf) == 11

def criar_ContaBancaria():
    agencia = "0001"
    numero_conta = str(random.randint(100000, 999999))
    return agencia, numero_conta

# Função de criação de usário
def criar_usuario():

    nome = input("Qual é o seu nome: ")

    # verificar se é de maior
    while True:

        nascimento = input('Digite sua data de nascimento (dd/mm/aaaa):' )
        
        try:
            nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
            hoje = datetime.today()

            # calculo da idade
            idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

            if idade >= 18:
                break
            else:
                print('Você não pode criar uma conta, por ser menor de idade')
                voltar_menu = login()
                break

        except ValueError:
            print('Data invalida!')
    
    # validação do CPF
    while True:
        cpf = input('Digite seu CPF: ')
        
        if validar_cpf(cpf):
            break
        else:
            print('CPF invalido! Digite apenas números e com 11 digitos')
    
    # dados de endereço
    cidade = input('Qual é a sua cidade: ')
    estado = input('Qual é o estado da sua cidade: ')
    rua = input('Qual é a sua rua: ')
    numero_casa = int(input('Qual é o número da sua casa: '))
    bairro = input('Qual é o seu bairro: ')

    senha = input('Digite a sua senha: ')
    
    agencia, numero_conta = criar_ContaBancaria()

    novo_usuario = {
        'Nome': nome,
        'Data de nascimento': nascimento,
        'CPF': cpf,
        'endereço': {
            'Cidade': cidade,
            'Estado': estado,
            'Rua': rua,
            'Número': numero_casa,
            'Bairro': bairro,
        },
        'Senha': senha,
        'Agência': agencia,
        'Número da conta': numero_conta,
        'Saldo': 0.0 
    }

    usuarios.append(novo_usuario) 
    print(f"\nUsuário criado com sucesso! Agência: {agencia}, Conta: {numero_conta}")

def interface_menu(usuario):
    saldo = usuario.get('Saldo', 0.0)

    while True:
        print("""
====================================
MENU BANCO X
[1] SAQUE
[2] DEPOSITO
[3] VISUALIZAR SALDO
[0] SAIR
====================================
        """)
        # proteger de entradas invalidas
        try:
            escolha_menu = int(input("\nComo podemos te ajudar: "))
        except ValueError:
            print('Digite apenas números')
            continue

        if escolha_menu == 1:
            fun_saque = Saque(saldo)
            fun_saque.executar_saque()
            saldo = fun_saque.saldo  # Atualiza saldo
            usuario['Saldo'] = saldo  # Salva no dicionário

        elif escolha_menu == 2:
            saldo = depositar(saldo)
            usuario['Saldo'] = saldo

        elif escolha_menu == 3:
            print(f'Seu saldo é de R${saldo:.2f}')
            escolha_3 = int(input('Deseja realizar:\n[1] SAQUE\n[2] DEPOSITO\n R: '))
            if escolha_3 == 1:
                fun_saque = Saque(saldo)
                fun_saque.executar_saque()
                saldo = fun_saque.saldo
                usuario['Saldo'] = saldo
            elif escolha_3 == 2:
                saldo = depositar(saldo)
                usuario['Saldo'] = saldo
            else:
                print('Opção inválida')

        elif escolha_menu == 0:
            print("Saindo do menu...")
            break

        else:
            print('Desculpe, essa opção não existe.')

def login():
    menu_login = """
BEM VINDO AO BANCO X
[1] Fazer login (Já tenho uma conta)
[2] Criar uma conta (Não tenho conta)
"""
    print(menu_login)

    while True:
        escolha_login = int(input('Faça a sua escolha: '))

        if escolha_login == 1:
            fazer_login()
        
        elif escolha_login == 2:
            print('Vamos criar a sua conta!\n')
            criar_usuario()
            fazer_login()  # <- isso garante que o usuário já logue
            break

def fazer_login():
    print('Bem-vindo de volta!')
    cpf_login = input('Digite seu CPF: ')

    # Verificar se o CPF está cadastrado
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['CPF'] == cpf_login:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print('CPF não cadastrado! Por favor, crie uma conta antes de tentar logar.\n')
        return  # Volta ao menu de login

    senha_login = input('Digite sua senha: ')

    # Verificar a senha
    if usuario_encontrado['Senha'] == senha_login:
        print(f"\nLogin realizado com sucesso, {usuario_encontrado['Nome']}!\n")
        interface_menu(usuario_encontrado)
    else:
        print('Senha incorreta! Tente novamente.\n')
    

saldo = 0

# Dados de usuários do banco
usuarios = []


login()