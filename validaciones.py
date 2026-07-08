"""
Módulo de validaciones.
Contiene funciones reutilizables para validar datos ingresados por el usuario.
"""


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Solicita un número entero al usuario, validando el rango si corresponde."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("  ⚠ Error: debe ingresar un número entero. Intente nuevamente.")
            continue

        if minimo is not None and valor < minimo:
            print(f"  ⚠ Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  ⚠ Error: el valor debe ser menor o igual a {maximo}.")
            continue

        return valor


def pedir_texto_no_vacio(mensaje):
    """Solicita una cadena de texto que no puede quedar vacía."""
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("  ⚠ Error: el campo no puede estar vacío. Intente nuevamente.")
            continue
        return entrada


def pedir_dni(mensaje):
    """Solicita un DNI: solo números, entre 6 y 9 dígitos."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("  ⚠ Error: el DNI debe contener solo números.")
            continue
        if not (6 <= len(entrada) <= 9):
            print("  ⚠ Error: el DNI debe tener entre 6 y 9 dígitos.")
            continue
        return entrada


def pedir_hora(mensaje):
    """Solicita una hora en formato HH:MM (24 horas) y la valida."""
    while True:
        entrada = input(mensaje).strip()
        partes = entrada.split(":")
        if len(partes) != 2:
            print("  ⚠ Error: formato inválido. Use HH:MM (ej: 14:30).")
            continue
        h_str, m_str = partes
        if not (h_str.isdigit() and m_str.isdigit()):
            print("  ⚠ Error: formato inválido. Use solo números en HH:MM.")
            continue
        h, m = int(h_str), int(m_str)
        if not (0 <= h <= 23 and 0 <= m <= 59):
            print("  ⚠ Error: hora fuera de rango. Use HH entre 00-23 y MM entre 00-59.")
            continue
        return h * 60 + m  # devuelve la hora convertida a minutos totales del día


def pedir_opcion_menu(mensaje, opciones_validas):
    """Solicita una opción de menú dentro de una lista de opciones válidas (strings)."""
    while True:
        entrada = input(mensaje).strip()
        if entrada in opciones_validas:
            return entrada
        print(f"  ⚠ Error: opción inválida. Opciones válidas: {', '.join(opciones_validas)}")
