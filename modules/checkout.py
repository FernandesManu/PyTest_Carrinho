import time

class GatewayDePagamento:
    def cobrar(self, valor, cartao):
        """Simula uma chamada real a uma API de banco."""
        print(f"\nConectando ao banco para cobrar R$ {valor}...")
        time.sleep(5)  # Simula a lentidão da internet/API
        # Aqui teria um código complexo fazendo um POST HTTP
        return True # Retorna True se aprovado, False se recusado

class Checkout:
    def __init__(self, gateway: GatewayDePagamento):
        # Recebemos o gateway como dependência
        self.gateway = gateway

    def finalizar_compra(self, carrinho, cartao):
        total = carrinho.calcular_total()
        
        if total <= 0:
            return "Sucesso: Grátis"
        
        # O Checkout delega a cobrança para o Gateway
        sucesso = self.gateway.cobrar(total, cartao)
        
        if sucesso:
            return "Sucesso: Pagamento aprovado"
        else:
            raise ValueError("Pagamento recusado pelo banco")