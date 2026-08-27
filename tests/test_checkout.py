from carrinho import Produto, CarrinhoDeCompras
from checkout import GatewayDePagamento, Checkout
import pytest
from unittest.mock import Mock

@pytest.fixture
def carrinho_cheio():
    carrinho = CarrinhoDeCompras()

    produto1 = Produto(nome="Notebook", preco=3000)
    produto2 = Produto(nome="Teclado", preco=500)

    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    return carrinho

def test_compra_com_sucesso(carrinho_cheio):
    mock_gateway = Mock(GatewayDePagamento)
    mock_gateway.cobrar.return_value = True

    checkout = Checkout(mock_gateway)
    cartao_falso = "1234-5678-9123-1234"

    resultado = checkout.finalizar_compra(carrinho_cheio, cartao_falso)
    assert resultado == "Sucesso: Pagamento aprovado"

    # testar se a função está passando os parametros corretos para o cobrar
    # e também se tá cobrando uma unica vez
    mock_gateway.cobrar.assert_called_once_with(3500, cartao_falso)

def test_compra_com_erro(carrinho_cheio):
    mock_gateway = Mock(GatewayDePagamento)
    mock_gateway.cobrar.return_value = False

    checkout = Checkout(mock_gateway)
    cartao_falso = "1234-5678-9123-1234"

    with pytest.raises(ValueError):
        resultado = checkout.finalizar_compra(carrinho_cheio, cartao_falso)
