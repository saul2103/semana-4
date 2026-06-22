from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio principal que administra los productos y clientes del restaurante."""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo_productos = {}  # codigo -> Producto
        self.directorio_clientes = {}  # id_cliente -> Cliente

    #  Gestión de Productos 
    def agregar_producto(self, producto):
        """Registra un nuevo producto en el catálogo."""
        self.catalogo_productos[producto.codigo] = producto

    def buscar_producto(self, codigo):
        """Busca un producto por su código y lo retorna, o None si no existe."""
        return self.catalogo_productos.get(codigo, None)

    def eliminar_producto(self, codigo):
        """Elimina un producto del catálogo si existe."""
        if codigo in self.catalogo_productos:
            del self.catalogo_productos[codigo]
            return True
        return False

    def listar_productos(self):
        """Devuelve una lista con todos los productos del catálogo."""
        return list(self.catalogo_productos.values())

    #  Gestión de Clientes 
    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente en el directorio."""
        self.directorio_clientes[cliente.id_cliente] = cliente

    def buscar_cliente(self, id_cliente):
        """Busca un cliente por su ID y lo retorna, o None si no existe."""
        return self.directorio_clientes.get(id_cliente, None)

    def listar_clientes(self):
        """Devuelve una lista con todos los clientes registrados."""
        return list(self.directorio_clientes.values())

    #  Reportes 
    def productos_por_categoria(self, categoria):
        """Filtra el catálogo de productos por una categoría específica."""
        return [prod for prod in self.catalogo_productos.values() if prod.categoria == categoria]

    def __str__(self):
        return f"Restaurante: {self.nombre} | Productos: {len(self.catalogo_productos)} | Clientes: {len(self.directorio_clientes)}"