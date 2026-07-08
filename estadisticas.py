"""
Módulo de estadísticas.
Calcula estadísticas básicas de utilización a partir de los alquileres finalizados.
"""
 
 
def mostrar_estadisticas(alquileres, inventario, clientes):
    print("\n--- Estadísticas de utilización ---")
 
    finalizados = [a for a in alquileres.values() if a["estado"] == "finalizado"]
 
    total_alquileres = len(finalizados)
    print(f"  Total de alquileres finalizados: {total_alquileres}")
 
    if total_alquileres == 0:
        print("  Aún no hay datos suficientes para generar estadísticas.")
        print("------------------------------------")
        return
 
    # Acumuladores
    total_recaudado = 0
    total_minutos = 0
    conteo_por_tipo = {}
    importe_por_tipo = {}
 
    for a in finalizados:
        total_recaudado += a["importe"]
        total_minutos += a["minutos_uso"]
        tipo = a["tipo_bici"]
        conteo_por_tipo[tipo] = conteo_por_tipo.get(tipo, 0) + 1
        importe_por_tipo[tipo] = importe_por_tipo.get(tipo, 0) + a["importe"]
 
    promedio_minutos = total_minutos / total_alquileres
    promedio_importe = total_recaudado / total_alquileres
 
    print(f"  Total recaudado: ${total_recaudado}")
    print(f"  Importe promedio por alquiler: ${promedio_importe:.2f}")
    print(f"  Tiempo promedio de uso por alquiler: {promedio_minutos:.1f} minutos")
 
    print("  Alquileres e importe recaudado por tipo de bicicleta:")
    for tipo, cantidad in conteo_por_tipo.items():
        print(f"    - {tipo}: {cantidad} alquiler(es) | Recaudado: ${importe_por_tipo[tipo]}")
 
    # Tipo de bicicleta más utilizado y el que más recaudó
    tipo_mas_usado = max(conteo_por_tipo, key=conteo_por_tipo.get)
    tipo_mas_recaudo = max(importe_por_tipo, key=importe_por_tipo.get)
    print(f"  Tipo de bicicleta más utilizada: {tipo_mas_usado}")
    print(f"  Tipo de bicicleta que más recaudó: {tipo_mas_recaudo} "
          f"(${importe_por_tipo[tipo_mas_recaudo]})")
 
    # Cliente con más alquileres
    if clientes:
        cliente_top_dni = max(clientes, key=lambda d: clientes[d]["cantidad_alquileres"])
        cliente_top = clientes[cliente_top_dni]
        if cliente_top["cantidad_alquileres"] > 0:
            print(f"  Cliente más frecuente: {cliente_top['nombre']} "
                  f"({cliente_top['cantidad_alquileres']} alquileres)")
 
    disponibles = sum(1 for b in inventario.values() if b["estado"] == "disponible")
    ocupadas = len(inventario) - disponibles
    print(f"  Bicicletas disponibles actualmente: {disponibles} / {len(inventario)}")
    print(f"  Bicicletas ocupadas actualmente: {ocupadas} / {len(inventario)}")
    print("------------------------------------")