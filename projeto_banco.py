# autor: @Gustavo (GH)

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
            print(f'Saque realiazdo no valor de R${valor}')
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

    

saldo = 0

while True:
    # interface do programa
    menu = """"
====================================
BEM VINDO AO BANCO X
[1] SAQUE
[2] DEPOSITO
[3] VISUALIZAR SALDO
[0] SAIR
====================================
"""
    print(menu)

    # Escolha das opções
    escolha_menu = int(input("\nComo podemos te ajudar: "))

    if escolha_menu == 1: # saque
        fun_saque = Saque(saldo)
        fun_saque.executar_saque()

    elif escolha_menu == 2: # deposito
        saldo = depositar(saldo)

    elif escolha_menu == 3: # visualziar saldo
        print(f'Seu saldo é de R${saldo}')
        escolha_3 = int(input('Você deseja fazer um saque ou deposito:\n[1] SAQUE\n[2] DEPOSITO\n R: '))

        if escolha_3 == 1: # opção de saque
            fun_saque = Saque(saldo)
            fun_saque.executar_saque()

        elif escolha_3 == 2: # opção de deposito
            saldo = depositar(saldo)

        else:
            print('Opção invalida')


    elif escolha_menu == 0: # sair
        break

    else: # sair 
        print('Desculpe, não existe essa opção, tente novamente.')