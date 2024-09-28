#Questão 1

Idade1 = int(input(" Idade 1 :"),)
Idade2 = int(input("Idade 2: "))

Mais_velho= max(Idade1, Idade2)

print(f'A maior idade é {Mais_velho}')

#Questão 2
n=int(input("Quantos numeros inteiros você vai escrever?: "))
valores = list()
for i in range(0,n):
    x = int(input("Lista de valores:"))
    valores.append(x)
    soma=sum(valores)
print(f'A soma total é igual a {soma}')

#Questão 3

Texto = input("Frase: ")
vogais= "aeiouAEIOU"

for i in range(0, len(vogais)):
    Texto = Texto.replace(vogais[i],'')
    
print(Texto)

#questão 4
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)

#Questão 5

Numero = int(input('Número: '))

if Numero >= 1:
    if Numero % 2 == 0:
        print(f'O número não é primo')
    else:
        print(F'O número é primo')
else:
    print(f'O número não é primo')
    
#Questão 6

n=int(input("Quantos strings vc vai utilizar?: "))
valores = list()
for i in range(0,n):
    x = input("Objeto:")
    valores.append(x)
    ordenados = sorted(valores,key=len)
print(f'Lista ordenada por tamanhoa: {ordenados}')

#Questão 7

string = input("Digite uma string: ")
for char in string:
    if string.count(char) == 1:
        print(f"A primeira letra que não se repete é: {char}")
        break
    
#Questão 8    
n = int(input("Qual número você deseja saber o fatorial: "))

def fatorial(n):
    if n==0:
        return 1
    else:
        return n * fatorial(n-1)

print(f'O fatorial do número {n} é {fatorial(n)}')

#Questão 9

for i in range(5):
    chute = int(input(f"""       
        Bem vindo ao mini-game acerte o chute!!
        Você terá 5 chance de acertar um número de 0 a 100
        Dê seu chuteeee: """))
    if chute == 37:
        print(f"""
              Parabêns você acertouuuuu!!!!
                 O número era 37""")
        break
    else:
        print("Tente novamente")
else:
    print(f"""  
          GAME OVER 
        O NÚMERO ERA 37""")   
    
#QUESTÃO 10


valores = list()
for i in range(0,10):
    x = int(input("Números:"))
    valores.append(x)
    ordenados = sorted(valores)
print(f'Lista ordenada do menor para o maior: {ordenados}') 

#Questão 11

string11= "Inteligência de Negócio"
print(string11[::-1])

#Questão 12

def delta(a,b,c):
    return b**2 - 4*a*c
print(f'O delta da função é: {delta(2,2,2)}')

#Questão 13

from itertools import combinations

def verifica_subconjunto(numeros, alvo):
    for i in range(1, len(numeros) + 1):
        for comb in combinations(numeros, i):
            if sum(comb) == alvo:
                return True
    return False

numeros = [int(x) for x in input("Digite números separados por espaço: ").split()]
alvo = int(input("Digite o valor alvo: "))
resultado = verifica_subconjunto(numeros, alvo)
print(f"Existe subconjunto com soma igual ao alvo: {resultado}")