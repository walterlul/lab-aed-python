"""
Módulo de gestión de alquileres.
Se encarga de iniciar y finalizar alquileres, calcular el tiempo de uso
y el importe a cobrar según la tarifa de cada tipo de bicicleta.
"""

from validaciones import pedir_entero, pedir_hora
from bicicletas import (
    bicicleta_existe,
    bicicleta_disponible,
    marcar_ocupada,
    marcar_disponible,
    obtener_tarifa,
)
from clientes import cliente_existe, incrementar_alquileres_cliente


def iniciar_alquiler(alquileres, inventario, clientes, contador_id):
    """
    Inicia un nuevo alquiler: pide DNI del cliente, ID de bicicleta y hora de inicio.
    Devuelve el nuevo contador_id (para el próximo alquiler).
    """
    print("\n--- Iniciar alquiler ---")

    dni = input("Ingrese el DNI del cliente (debe estar registrado): ").strip()
    if not cliente_existe(clientes, dni):
        print("  ⚠ Error: no existe un cliente registrado con ese DNI. "
              "Registrelo primero desde el menú de clientes.")
        return contador_id

    id_bici = pedir_entero("Ingrese el ID de la bicicleta a alquilar: ", minimo=1)
    if not bicicleta_existe(inventario, id_bici):
        print("  ⚠ Error: no existe una bicicleta con ese ID.")
        return contador_id

    if not bicicleta_disponible(inventario, id_bici):
        print("  ⚠ Error: la bicicleta seleccionada no está disponible en este momento.")
        return contador_id

    hora_inicio = pedir_hora("Ingrese la hora de inicio (HH:MM): ")

    id_alquiler = contador_id
    alquileres[id_alquiler] = {
        "id": id_alquiler,
        "dni_cliente": dni,
        "id_bici": id_bici,
        "tipo_bici": inventario[id_bici]["tipo"],
        "hora_inicio": hora_inicio,
        "hora_fin": None,
        "minutos_uso": None,
        "importe": None,
        "estado": "en curso",
    }

    marcar_ocupada(inventario, id_bici)
    print(f"  ✔ Alquiler #{id_alquiler} iniciado. Bicicleta {id_bici} marcada como ocupada.")
    return contador_id + 1

def finalizar_alquiler(alquileres, inventario, clientes):
    """Finaliza un alquiler en curso: calcula tiempo de uso e importe a cobrar."""
    print("\n--- Finalizar alquiler ---")

    alquileres_en_curso = [a for a in alquileres.values() if a["estado"] == "en curso"]
    if not alquileres_en_curso:
        print("  ℹ No hay alquileres en curso para finalizar.")
        return

    print("Alquileres en curso:")
    for a in alquileres_en_curso:
        print(f"  #{a['id']} | Bicicleta {a['id_bici']} | Cliente DNI {a['dni_cliente']}")

    id_alquiler = pedir_entero("Ingrese el número de alquiler a finalizar: ", minimo=1)

    if id_alquiler not in alquileres or alquileres[id_alquiler]["estado"] != "en curso":
        print("  ⚠ Error: ese número de alquiler no existe o ya fue finalizado.")
        return

    hora_fin = pedir_hora("Ingrese la hora de finalización (HH:MM): ")
    alquiler = alquileres[id_alquiler]

    minutos_uso = hora_fin - alquiler["hora_inicio"]
    if minutos_uso < 0:
        # Contempla el caso de que el alquiler cruce la medianoche
        minutos_uso += 24 * 60

    if minutos_uso == 0:
        minutos_uso = 1  # se cobra un mínimo de 1 minuto para evitar importe $0

    tarifa = obtener_tarifa(alquiler["tipo_bici"])
    importe = minutos_uso * tarifa

    alquiler["hora_fin"] = hora_fin
    alquiler["minutos_uso"] = minutos_uso
    alquiler["importe"] = importe
    alquiler["estado"] = "finalizado"

    marcar_disponible(inventario, alquiler["id_bici"])
    incrementar_alquileres_cliente(clientes, alquiler["dni_cliente"])

    print(f"  ✔ Alquiler #{id_alquiler} finalizado.")
    print(f"    Tiempo de uso: {minutos_uso} minutos")
    print(f"    Importe a cobrar: ${importe}")


def listar_alquileres(alquileres):
    print("\n--- Historial de alquileres ---")
    if not alquileres:
        print("  Todavía no se registraron alquileres.")
        return

    for a in alquileres.values():
        estado = a["estado"]
        linea = (f"  #{a['id']:>3} | Cliente DNI: {a['dni_cliente']} | "
                  f"Bici: {a['id_bici']} ({a['tipo_bici']}) | Estado: {estado}")
        if estado == "finalizado":
            linea += f" | Tiempo: {a['minutos_uso']} min | Importe: ${a['importe']}"
        print(linea)
    print("--------------------------------")