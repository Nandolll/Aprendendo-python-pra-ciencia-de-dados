# class animal:
#     def __init__(self,n_patas):
#         self.n_patas=n_patas
        

# class mamifero(animal):
#     def __init__(self, n_patas):
#         super().__init__(n_patas)

# class Ave(animal):
#     def __init__(self, n_patas):
#         super().__init__(n_patas)


# class cachorro(animal):
#     pass

# class gato(animal):
#     pass

# class leao(animal):
#     pass

# class animal:
#     def __init__(self,n_patas):
#         self.n_patas=n_patas
        

# class mamifero(animal):
#     def __init__(self, n_patas):
#         super().__init__(n_patas)

# class Ave(animal):
#     def __init__(self, n_patas):
#         super().__init__(n_patas)


# class cachorro(animal):
#     pass

# class gato(animal):
#     pass

# class leao(animal):
#     pass



class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # Método para adicionar uma venda à lista de vendas
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("Erro: o objeto não é uma venda.")

    # Método para calcular e retornar o total das vendas
    def total_vendas(self):
        total = sum(venda.valor for venda in self.vendas)
        return total

def main():
    categorias = []

    # Lê categorias e suas vendas
    for i in range(2):  # Ajuste o número de categorias conforme necessário
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2):  # Ajuste o número de vendas conforme necessário
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adiciona a venda à categoria
            categoria.adicionar_venda(venda)

        categorias.append(categoria)

    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total:.1f}")

if __name__ == "__main__":
    main()
