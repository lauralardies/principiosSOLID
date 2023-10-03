class Pedido():
    def __init__(self, cliente, importe, tipo_pizza):
        self.cliente = cliente
        self.importe = importe
        self.estado = 'PENDIENTE'
        self.tipo_pizza = tipo_pizza

    def paga(self):
        self.estado = 'PAGADO'

    def finaliza(self):
        self.estado = 'ENVIADO'
 
    def mostrar_pedido(self):
        print(f"Cliente: {self.cliente} tu pedido {self.tipo_pizza} de importe: {self.importe}, está {self.estado} ")