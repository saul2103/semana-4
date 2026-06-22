# Sistema de Gestión de Restaurante

**Estudiante:** [Bryan Saul Iza Llano]

---

## Descripción del Sistema

Este proyecto implementa un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos en Python. El sistema permite administrar el catálogo de productos (platos, bebidas, postres, etc.) y el directorio de clientes del establecimiento.

Las funcionalidades principales incluyen:

- Registrar, buscar, listar y eliminar productos del menú.
- Alternar la disponibilidad de un producto y modificar sus precios.
- Registrar, buscar y listar clientes.
- Filtrar productos por categoría.
- Visualizar reportes organizados desde la consola.

El programa se ejecuta desde `main.py`, donde se crean instancias de prueba y se invocan los métodos del servicio principal para demostrar el correcto funcionamiento del sistema.

---

## Estructura del Proyecto


### Responsabilidad de cada módulo

| Archivo | Clase | Descripción |
|---|---|---|
| `modelos/producto.py` | `Producto` | Representa un plato o bebida del restaurante. Almacena código, nombre, precio, categoría y disponibilidad. Incluye métodos para modificar precio y alternar disponibilidad. |
| `modelos/cliente.py` | `Cliente` | Representa un cliente del restaurante. Contiene ID, nombre, teléfono, correo electrónico y un historial de pedidos. |
| `servicios/restaurante.py` | `Restaurante` | Clase principal de servicio que administra las colecciones de productos y clientes. Contiene métodos para registrar, buscar, listar y filtrar tanto productos como clientes. |
| `main.py` | — | Punto de entrada del programa. Crea objetos de prueba, los registra en el servicio y ejecuta los métodos principales para mostrar resultados en consola. |

---

## Reflexión sobre Modularización y Separación de Responsabilidades

La organización del software en módulos independientes es una práctica fundamental en el desarrollo de aplicaciones mantenibles y escalables. Al separar las clases `Producto`, `Cliente` y `Restaurante` en archivos distintos dentro de carpetas con responsabilidades bien definidas (`modelos` para las entidades del dominio y `servicios` para la lógica de gestión), se logran varios beneficios:

1. **Reutilización:** las clases pueden importarse y utilizarse en diferentes partes del proyecto sin duplicar código.
2. **Mantenibilidad:** cada módulo puede modificarse de forma aislada, reduciendo el riesgo de introducir errores en otras partes del sistema.
3. **Legibilidad:** la estructura del proyecto comunica de forma inmediata la arquitectura del software a cualquier desarrollador que se una al proyecto.
4. **Separación de responsabilidades:** `Producto` y `Cliente` solo se preocupan por sus propios datos y comportamiento, mientras que `Restaurante` actúa como coordinador. Esto evita clases sobrecargadas con múltiples responsabilidades (principio SRP de SOLID).
5. **Pruebas unitarias simplificadas:** al estar las clases desacopladas, se pueden probar individualmente simulando dependencias.

En conclusión, modularizar el software y asignar responsabilidades claras a cada componente no es solo una buena práctica académica, sino una necesidad real para construir sistemas robustos que puedan crecer y adaptarse con el tiempo.