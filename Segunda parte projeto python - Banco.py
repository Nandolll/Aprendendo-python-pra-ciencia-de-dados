
from textwrap import dedent
def menu():
    opcoes = """
        [1][Depositar]
        [2][Sacar]
        [3][Extrato]
        [4][Nova conta]
        [5][Listar contas]
        [6][Novo usuário]
        [7][Sair]
    """
    opcao=int(input(opcoes))
    return opcao

saldo = 2000
LIMITE_S = 500
numero_s = 0
N_LIMITE_SAQUE = 3
extrato = ''
usuarios=[]
contas=[]
AGENCIA='0001'

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
    elif numero_s >= N_LIMITE_SAQUE:
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

def criar_usuario(usuarios):
    cpf = input("Insira seu CPF(somente números): ")
    usuario = filtrar_user(cpf,usuarios)
    if usuario:
        print(f'''Já existe um usuário com este CPF!''')
        return
    nome= input('Informe seu nome completo:')
    nascimento=input("Informe sua data de nascimento (dd-mm-aaaa):")
    endereco=input('Informe seu endereço (logradoro,nro-bairro-cidade-estado):')
    
    usuarios.append({'nome':nome,'nascimento':nascimento,'endereço':endereco,'cpf':cpf})

    print(f'''Você criou o usuário com sucesso!''')

def criar_conta(agencia,numero_c,usuarios):
    cpf = input("Insira seu CPF(somente números): ")
    usuario = filtrar_user(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{'agencia':agencia,'numero_conta':numero_c,'usuario':usuario}
    print(f"O seu usuario com o número de CPF {cpf} não está registado nos nosso banco de dados.")

def contas_l(contas):
    for conta in contas:
        l=f'''
           Agência:\t{conta['agencia']}
           C/c:\t{conta['numero_conta']} 
           Titular:\t{conta['usuario']['nome']}
           '''
        print('='*100)
        print(dedent(l))

def filtrar_user(cpf,usuarios):
    user_filter= [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return user_filter[0] if user_filter else None

while True:
    opcao=menu()
    if opcao == 1:
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == 2:
        saldo, extrato, numero_s = sacar(saldo, extrato, numero_s)
    elif opcao == 3:
        exibir_extrato(saldo, extrato)
    elif opcao==4:
        numero_c=len(contas)+1
        conta=criar_conta(AGENCIA,numero_c,usuarios)
        if conta:
            contas.append(conta)
    elif opcao==5:
        contas_l(contas)
    elif opcao==6:
        criar_usuario(usuarios) # type: ignore
    elif opcao == 7:
        print("Obrigado por utilizar o nosso banco")
        break 
    else:
        print('Operação inválida, por favor tente novamente')
