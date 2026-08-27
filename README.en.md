# PyTest Shopping Cart

[🇧🇷](README.md) [🇺🇸](README.en.md)

Educational Python project for practicing automated tests with `pytest` in a simple shopping flow.

## What the project does

### Shopping cart

- `Produto` represents an item with `nome` and `preco`.
- `CarrinhoDeCompras` keeps a list of products.
- `adicionar_produto(produto)` adds a product to the cart.
- `calcular_total(desconto_percentual=0)` adds the prices and applies an optional percentage discount. The current implementation does not restrict the discount to the range from 0 to 100.

### Checkout

- `Checkout` receives a payment gateway through dependency injection.
- For a cart with a positive total, it delegates the charge to the gateway's `cobrar` method.
- Returns `"Sucesso: Pagamento aprovado"` when the charge returns `True`.
- Raises `ValueError` with the message `"Pagamento recusado pelo banco"` when the charge returns `False`.
- Carts with a total equal to or below zero return `"Sucesso: Grátis"` without calling the gateway.

`GatewayDePagamento` is a simulation: it prints the charge, waits 5 seconds, and always returns `True`. In the tests, it is replaced with a `Mock` to avoid this wait and simulate approval or rejection.

## Structure

```text
modules/
	carrinho.py       # Produto and CarrinhoDeCompras
	checkout.py       # GatewayDePagamento and Checkout
tests/
	test_carrinho.py  # Valid totals and discounts
	test_carrinho2.py # Expected cases for discounts outside the range
	test_checkout.py  # Approval, rejection, and gateway interaction
```

## How to run

Have Python 3 installed and install `pytest`:

```bash
python -m pip install pytest
```

Run the tests from the project root:

```bash
python -m pytest
```

## Usage example

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
