class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self, desconto_percentual=0):
        """Calcula o total do carrinho aplicando um desconto opcional."""
        total = sum(produto.preco for produto in self.produtos)
        
        # O cálculo perigoso feito às pressas
        valor_desconto = total * (desconto_percentual / 100)
        return total - valor_desconto