"""
Módulo de gestión de bicicletas.
Mantiene el inventario de bicicletas y su disponibilidad.
"""
 
# Tarifas por tipo de bicicleta (importe por minuto de uso)
TARIFAS_POR_MINUTO = {
    "urbana": 15,
    "montania": 20,
    "electrica": 35,
}
 
 
def crear_inventario_inicial():
    """
    Crea un inventario inicial de bicicletas de ejemplo.
    Cada bicicleta es un diccionario con: id, tipo, estado ('disponible' u 'ocupada').
    """
    inventario = {}
    tipos_iniciales = (
        ["urbana"] * 4 +
        ["montania"] * 3 +
        ["electrica"] * 3
    )
    for i, tipo in enumerate(tipos_iniciales, start=1):
        inventario[i] = {"id": i, "tipo": tipo, "estado": "disponible"}
    return inventario
 
 
def listar_bicicletas(inventario, solo_disponibles=False):
    """Muestra por pantalla el listado de bicicletas, opcionalmente filtrado."""
    print("\n--- Listado de bicicletas ---")
    encontrada = False
    for bici in inventario.values():
        if solo_disponibles and bici["estado"] != "disponible":
            continue
        encontrada = True
        tarifa = obtener_tarifa(bici["tipo"])
        print(f"  ID {bici['id']:>2} | Tipo: {bici['tipo']:<10} | "
              f"Tarifa: ${tarifa}/min | Estado: {bici['estado']}")
    if not encontrada:
        print("  No hay bicicletas para mostrar con ese criterio.")
    print("-----------------------------")
 
 
def contar_disponibles(inventario):
    """Cuenta cuántas bicicletas están disponibles (uso de contador/acumulador)."""
    contador = 0
    for bici in inventario.values():
        if bici["estado"] == "disponible":
            contador += 1
    return contador
 
 
def bicicleta_existe(inventario, id_bici):
    return id_bici in inventario
 
 
def bicicleta_disponible(inventario, id_bici):
    return inventario[id_bici]["estado"] == "disponible"
 
 
def marcar_ocupada(inventario, id_bici):
    inventario[id_bici]["estado"] = "ocupada"
 
 
def marcar_disponible(inventario, id_bici):
    inventario[id_bici]["estado"] = "disponible"
 
 
def obtener_tarifa(tipo_bici):
    """Devuelve la tarifa por minuto según el tipo de bicicleta."""
    return TARIFAS_POR_MINUTO.get(tipo_bici, 15)