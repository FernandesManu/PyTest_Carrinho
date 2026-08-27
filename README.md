# PyTest Carrinho

Projeto didático em Python para praticar testes automatizados com `pytest` em um fluxo simples de compras.

## O que o projeto faz

### Carrinho

- `Produto` representa um item com `nome` e `preco`.
- `CarrinhoDeCompras` mantém uma lista de produtos.
- `adicionar_produto(produto)` adiciona um produto ao carrinho.
- `calcular_total(desconto_percentual=0)` soma os preços e aplica um desconto percentual opcional. A implementação atual não restringe o desconto ao intervalo de 0 a 100.

### Checkout

- `Checkout` recebe um gateway de pagamento por injeção de dependência.
- Para um carrinho com total positivo, delega a cobrança ao método `cobrar` do gateway.
- Retorna `"Sucesso: Pagamento aprovado"` quando a cobrança retorna `True`.
- Levanta `ValueError` com a mensagem `"Pagamento recusado pelo banco"` quando a cobrança retorna `False`.
- Carrinhos com total igual ou inferior a zero retornam `"Sucesso: Grátis"` sem chamar o gateway.

`GatewayDePagamento` é uma simulação: imprime a cobrança, aguarda 5 segundos e sempre retorna `True`. Nos testes, ele é substituído por um `Mock` para evitar essa espera e simular aprovação ou recusa.

## Estrutura

```text
modules/
	carrinho.py       # Produto e CarrinhoDeCompras
	checkout.py       # GatewayDePagamento e Checkout
tests/
	test_carrinho.py  # Totais e descontos válidos
	test_carrinho2.py # Casos esperados para descontos fora do intervalo
	test_checkout.py  # Aprovação, recusa e interação com o gateway
```

## Como executar

Tenha Python 3 instalado e instale o `pytest`:

```bash
python -m pip install pytest
```

Execute os testes a partir da raiz do projeto:

```bash
python -m pytest
```

## Exemplo de uso

```python
from modules.carrinho import CarrinhoDeCompras, Produto
from modules.checkout import Checkout, GatewayDePagamento

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(Produto("Notebook", 3000))
carrinho.adicionar_produto(Produto("Teclado", 500))

print(carrinho.calcular_total())                 # 3500
print(carrinho.calcular_total(desconto_percentual=10))  # 3150.0

checkout = Checkout(GatewayDePagamento())
print(checkout.finalizar_compra(carrinho, "1234-5678-9123-1234"))
```
