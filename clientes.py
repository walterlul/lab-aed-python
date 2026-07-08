"""
Módulo de gestión de clientes.
Permite registrar clientes y validar su existencia antes de un alquiler.
"""

from validaciones import pedir_dni, pedir_texto_no_vacio


def registrar_cliente(clientes):
    """Registra un nuevo cliente o recupera uno ya existente por DNI."""
    print("\n--- Registro de cliente ---")
    dni = pedir_dni("Ingrese el DNI del cliente: ")

    if dni in clientes:
        print(f"  ℹ El cliente con DNI {dni} ya está registrado: {clientes[dni]['nombre']}.")
        return dni

    nombre = pedir_texto_no_vacio("Ingrese el nombre completo del cliente: ")
    clientes[dni] = {"dni": dni, "nombre": nombre, "cantidad_alquileres": 0}
    print(f"  ✔ Cliente '{nombre}' registrado con éxito.")
    return dni


def cliente_existe(clientes, dni):
    return dni in clientes


def incrementar_alquileres_cliente(clientes, dni):
    """Acumulador: suma un alquiler más al historial del cliente."""
    clientes[dni]["cantidad_alquileres"] += 1


def listar_clientes(clientes):
    print("\n--- Listado de clientes ---")
    if not clientes:
        print("  No hay clientes registrados todavía.")
        return
    for datos in clientes.values():
        print(f"  DNI: {datos['dni']} | Nombre: {datos['nombre']:<20} | "
              f"Alquileres realizados: {datos['cantidad_alquileres']}")
    print("---------------------------")