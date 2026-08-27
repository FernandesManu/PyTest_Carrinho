from carrinho import Produto, CarrinhoDeCompras
import pytest

@pytest.fixture
def carrinho_cheio():
    carrinho = CarrinhoDeCompras()

    produto1 = Produto(nome="Notebook", preco=3000)
    produto2 = Produto(nome="Teclado", preco=500)

    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    return carrinho


@pytest.mark.parametrize("valor_desconto", [-10, 150, 500, 1500, -300])
def test_desconto_fora_intervalo(carrinho_cheio, valor_desconto):
    with pytest.raises(ValueError):
        carrinho_cheio.calcular_total(desconto_percentual=valor_desconto)
