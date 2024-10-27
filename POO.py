class bike:#self é a instancia(ou referencia )
    def __init__(self ,cor,modelo,ano,valor):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
    
    def buzinas(self):
        print("ouou")

    def parar(self):
        print("Parando poha")
        print("parou caralho")

    def correr(self):
        print("Corre")

    #def __str__(self):
     #   return f'bike:{self.cor},{self.modelo},{self.ano},{self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"


caloi = bike("roxa",'caloi',2002,50000)
print(caloi)