class Producto:
    """Representa un plato o bebida disponible en el restaurante."""
    
    def __init__(self, codigo, nombre, precio, categoria, disponible=True):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ejemplo: 'Entrada', 'Plato Fuerte', 'Bebida', 'Postre'
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} ({self.categoria}) -> {estado}"

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def cambiar_disponibilidad(self):
        """Alterna el estado de disponibilidad del producto."""
        self.disponible = not self.disponible