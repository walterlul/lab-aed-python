"""
Sistema de Alquiler de Bicicletas
----------------------------------
Trabajo Final Integrador - Laboratorio de Python
Algoritmos y Estructuras de Datos - ISI

Escenario 11: Sistema de alquiler de bicicletas.

Este programa permite:
  - Registrar clientes.
  - Ver el estado de las bicicletas disponibles.
  - Iniciar y finalizar alquileres.
  - Calcular el tiempo de uso y el importe a cobrar.
  - Consultar estadísticas de utilización.
"""

from validaciones import pedir_opcion_menu
from bicicletas import crear_inventario_inicial, listar_bicicletas
from clientes import registrar_cliente, listar_clientes
from alquileres import iniciar_alquiler, finalizar_alquiler, listar_alquileres
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n============================================")
    print("   SISTEMA DE ALQUILER DE BICICLETAS")
    print("============================================")
    print(" 1. Registrar cliente")
    print(" 2. Ver bicicletas disponibles")
    print(" 3. Ver todas las bicicletas")
    print(" 4. Iniciar alquiler")
    print(" 5. Finalizar alquiler")
    print(" 6. Ver historial de alquileres")
    print(" 7. Ver listado de clientes")
    print(" 8. Ver estadísticas de utilización")
    print(" 9. Salir")
    print("============================================")


def main():
    # Estructuras de datos centrales del sistema
    inventario = crear_inventario_inicial()
    clientes = {}
    alquileres = {}
    contador_id_alquiler = 1  # contador utilizado como ID incremental de alquiler

    print("Bienvenido/a al Sistema de Alquiler de Bicicletas.")

    opciones_validas = [str(n) for n in range(1, 10)]

    while True:
        mostrar_menu()
        opcion = pedir_opcion_menu("Seleccione una opción: ", opciones_validas)

        if opcion == "1":
            registrar_cliente(clientes)

        elif opcion == "2":
            listar_bicicletas(inventario, solo_disponibles=True)

        elif opcion == "3":
            listar_bicicletas(inventario, solo_disponibles=False)

        elif opcion == "4":
            contador_id_alquiler = iniciar_alquiler(
                alquileres, inventario, clientes, contador_id_alquiler
            )

        elif opcion == "5":
            finalizar_alquiler(alquileres, inventario, clientes)

        elif opcion == "6":
            listar_alquileres(alquileres)

        elif opcion == "7":
            listar_clientes(clientes)

        elif opcion == "8":
            mostrar_estadisticas(alquileres, inventario, clientes)

        elif opcion == "9":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()