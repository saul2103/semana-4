from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # 1. Crear la instancia principal del restaurante
    mi_restaurante = Restaurante("Sabor Manabita")
    print(f"\n--- {mi_restaurante.nombre} ---")

    # 2. Crear objetos Producto
    p1 = Producto("P001", "Ceviche de Camarón", 12.50, "Entrada")
    p2 = Producto("P002", "Arroz Marinero", 15.99, "Plato Fuerte")
    p3 = Producto("P003", "Jugo de Maracuyá", 3.50, "Bebida")
    p4 = Producto("P004", "Tres Leches", 6.00, "Postre", disponible=False)  # Producto agotado inicialmente
    p5 = Producto("P005", "Aji de Gallina", 13.50, "Plato Fuerte")

    # 3. Agregar los productos al servicio (Restaurante)
    productos_prueba = [p1, p2, p3, p4, p5]
    for prod in productos_prueba:
        mi_restaurante.agregar_producto(prod)

    # 4. Crear objetos Cliente
    c1 = Cliente("C100", "Ana Morales", "0987654321", "ana.m@email.com")
    c2 = Cliente("C101", "Carlos Pérez", "0998877665")
    c3 = Cliente("C102", "Lucía Fernanda", "0976543210", "lucy.f@correo.com")

    # 5. Registrar los clientes en el servicio
    clientes_prueba = [c1, c2, c3]
    for cli in clientes_prueba:
        mi_restaurante.registrar_cliente(cli)

    # 6. Demostrar funcionamiento: mostrar datos organizados
    print("\n   CATÁLOGO DE PRODUCTOS   ")
    for producto in mi_restaurante.listar_productos():
        print(f"  {producto}")

    print("\n    DIRECTORIO DE CLIENTES    ")
    for cliente in mi_restaurante.listar_clientes():
        print(f"  {cliente}")

    # 7. Demostrar métodos específicos
    print("\n    BÚSQUEDAS Y REPORTES    ")
    producto_buscado = mi_restaurante.buscar_producto("P002")
    print(f"Producto encontrado: {producto_buscado}")

    cliente_buscado = mi_restaurante.buscar_cliente("C101")
    print(f"Cliente encontrado: {cliente_buscado}")

    print("\n--- Productos en categoría 'Plato Fuerte' ---")
    for prod in mi_restaurante.productos_por_categoria("Plato Fuerte"):
        print(f"  {prod}")

    # 8. Demostrar modificación de atributos mediante métodos
    print("\n    MODIFICACIONES    ")
    print(f"Antes: {p4}")
    p4.cambiar_disponibilidad()  # Ahora se marca como disponible
    print(f"Después de cambiar disponibilidad: {p4}")

    p1.actualizar_precio(14.00)
    print(f"Precio actualizado de '{p1.nombre}': ${p1.precio:.2f}")

    # 9. Estado final del servicio
    print(f"\nResumen del sistema: {mi_restaurante}")


if __name__ == "__main__":
    main()