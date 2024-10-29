# class veiculo:
#     def __init__(self,cor,placa,numero_rodas):
#         self.cor = cor
#         self.placa= placa
#         self.numero_rodas=numero_rodas
    
#     def liga_motor(self):
#         print("Ligando motor")
    

# class motocicleta(veiculo):
#     pass

# class carro(veiculo):
#     pass

# class caminhao(veiculo):
#     def __init__(self, cor, placa, numero_rodas):
#         super().__init__(cor, placa, numero_rodas)
#         self.carregado= carregado

#     def esta_carregado(self):
#         print(f'{"Sim" if self.carregado else "Não"} estou carregando')

# caminhao= caminhao("roxo","123456",8,True)
# caminhao.liga_motor()
# caminhao.esta_carregado


# class Foo:
#     def __init__(self,x=None):
#         self._x=x

#     @property
#     def x(self):    
#         return self._x or 0
    
#     @x.setter
#     def x(self,value):

#     @x.deleter
#     def x(self):
#         self._x-=1



# foo=Foo(10)
# print(foo.x)


# class Estudante:
#     escola="Dio"

#     def __init__(self,nome,matricula):
#         self.nome= nome
#         self.matricula = matricula

#     def __str__(self):
#         return f'{self.nome}-{self.matricula}-{self.escola}'
        
# def mostrar_valores(*objs):
#     for obj in objs
#     print(obj)


class Pessoa:

    def __init__(self,nome,idade):
        self.nome= nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2022 - ano
        return cls(nome,idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade>=18
    
p=Pessoa.criar_de_data_nascimento(1994,3,21,"Fernando")
print(p.nome,p.idade)

print(Pessoa.e_maior_idade(18))