Nome = str(input("Qual o seu nome: "))
saldo = 2000
if Nome =="Fernando" or "fernando":
    saque = float(input("Quanto você deseja sacar: "))
    if saque <= saldo :
        print("Saque sendo realizado! ")
    else:
        print("Saldo insuficiente")