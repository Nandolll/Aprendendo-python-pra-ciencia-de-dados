opcoes = """
    [1][Depositar]
    [2][Sacar]
    [3][Extrato]
    [4][Sair]
   """
   
saldo = 2000
LIMITE_S = 500
numero_s = 0
n_Limite_saque = 3
extrato = ''

def depositar(saldo, extrato):
    deposito = float(input("Qual o valor que deseja depositar?: "))
    if deposito > 0:
        saldo += deposito
        extrato += f'Seu deposito foi no valor de: R${deposito:.2f}\n'
        print(f'O deposito no valor de R$ {deposito:.2f} foi realizado com sucesso!')
    else:
        print("Operação falhou")
    return saldo, extrato

def sacar(saldo, extrato, numero_s):
    saca = float(input('Informe o valor do saque: '))
    if saca <= 0:
        print("Operação falhou")
    elif saca > saldo:
        print("Operação Falhou, Saldo insuficiente!") 
    elif saca > LIMITE_S:
        print('Operação falhou, o valor é maior que o limite de saque permitido')
    elif numero_s >= n_Limite_saque:
        print('Você excedeu o seu limite de operações diárias')
    else:
        saldo -= saca
        extrato += f'Saque no valor de: R$ {saca:.2f}\n'
        numero_s += 1
        print(f"Saque de R$ {saca:.2f} realizado com sucesso\n")
    return saldo, extrato, numero_s
                  
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")
    

while True:
    opcao = int(input(opcoes))
    if opcao == 1:
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == 2:
        saldo, extrato, numero_s = sacar(saldo, extrato, numero_s)
    elif opcao == 3:
        exibir_extrato(saldo, extrato)
    elif opcao == 4:
        print("Obrigado por utilizar o nosso banco")
        break 
    else:
        print('Operação inválida, por favor tente novamente')
