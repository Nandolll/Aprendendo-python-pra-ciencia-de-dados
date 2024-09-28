#old style 

#exemplo 1 

nome = 'Fenando'
idade = 24
profissao = 'Estatístico'
linguagem = 'Python e R'
#print("Olá eu me chamo %s. Tenho %d anos, trabalho na área de %s e sei as linguagens %s" %(nome,idade,profissao,linguagem)) 
#Exemplo método format

#print("olá, me chamo {}. Tenho {} anos de idade, sou da área de {} e sei as linguagens {}." .format(nome,idade,profissao,linguagem))
#print("olá, me chamo {3}. Tenho {2} anos de idade, sou da área de {1} e sei as linguagens {0}." .format(nome,idade,profissao,linguagem))

 #F-STRING
 
 #print(f"olá, me chamo {nome}. Tenho {idade} anos de idade, sou da área de {profissao} e sei as linguagens {linguagem}.")

curso ="Python"
print(f'Bem vindo ao curso de {curso.upper()}')
print(curso.lstrip())