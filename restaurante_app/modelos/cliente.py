class Cliente:
    """Representa una persona que realiza o consume un pedido en el restaurante."""
    
    def __init__(self, id_cliente, nombre, telefono, email=""):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.historial_pedidos = []  # Lista de referencias a pedidos realizados

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre} | Tel: {self.telefono} | Email: {self.email}"

    def agregar_pedido_historial(self, pedido):
        """Agrega un pedido al historial del cliente."""
        self.historial_pedidos.append(pedido)

    def consultar_historial(self):
        """Devuelve la cantidad de pedidos realizados."""
        return len(self.historial_pedidos)