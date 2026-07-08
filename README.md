# Sistema de Alquiler de Bicicletas

Trabajo Final Integrador - Laboratorio de Python
Algoritmos y Estructuras de Datos - ISI - Ciclo 2026

## Integrantes
- Benitez Walter David
- Acevedo Delgado Santiago
- Contrera Santiago Bruno
- Dabski Santiago Daniel

## Comisión
k 1.1

## Descripción general del sistema

El sistema simula la gestión de un servicio de alquiler de bicicletas dentro de un
parque o ciudad. Permite:

- Registrar clientes (validando DNI y nombre).
- Consultar el inventario de bicicletas (disponibles u ocupadas), con tres tipos:
  urbana, montaña y eléctrica, cada una con su propia tarifa por minuto.
- Iniciar un alquiler: se elige cliente, bicicleta y hora de inicio. La bicicleta
  queda marcada como "ocupada".
- Finalizar un alquiler: se ingresa la hora de finalización, y el sistema calcula
  automáticamente el tiempo de uso (en minutos) y el importe a cobrar según la
  tarifa del tipo de bicicleta. La bicicleta vuelve a quedar "disponible".
- Consultar el historial completo de alquileres (en curso y finalizados).
- Consultar estadísticas de utilización: total recaudado, tiempo promedio de uso,
  cantidad de alquileres por tipo de bicicleta, tipo más utilizado, cliente más
  frecuente y disponibilidad actual de bicicletas.

## Estructura del proyecto

```
alquiler_bicicletas/
├── main.py            # Punto de entrada, contiene el menú principal
├── validaciones.py     # Funciones genéricas de validación de datos ingresados
├── bicicletas.py       # Gestión del inventario de bicicletas y tarifas
├── clientes.py         # Registro y consulta de clientes
├── alquileres.py       # Lógica de inicio/fin de alquiler, cálculo de tiempo e importe
├── estadisticas.py     # Cálculo de estadísticas de utilización
└── README.md
```

## Requisitos técnicos cumplidos

- **Estructuras condicionales**: validación de opciones de menú, estados de
  bicicleta, existencia de cliente/bicicleta, etc.
- **Estructuras repetitivas**: bucles del menú principal, validaciones con
  reintento (`while True`), recorridos de diccionarios para listar y calcular
  estadísticas.
- **Funciones**: cada operación del sistema está modularizada en funciones
  específicas dentro de su propio módulo.
- **Validaciones**: DNI (solo números, longitud), horarios (formato HH:MM y
  rangos válidos), IDs de bicicleta existentes, opciones de menú válidas, etc.
- **Acumuladores y contadores**: cantidad de alquileres por cliente, total
  recaudado, total de minutos, conteo de alquileres por tipo de bicicleta,
  bicicletas disponibles/ocupadas.
- **Manejo básico de errores y mensajes al usuario**: mensajes claros ante
  DNIs inválidos, bicicletas inexistentes u ocupadas, alquileres inexistentes,
  formatos de hora incorrectos, opciones de menú inválidas.

## Instrucciones de ejecución

1. Asegurarse de tener Python 3.8 o superior instalado.
2. Ubicarse en la carpeta del proyecto desde la terminal:
   ```
   cd alquiler_bicicletas
   ```
3. Ejecutar el programa:
   ```
   python3 main.py
   ```
4. Seguir las instrucciones del menú interactivo por consola.

### Ejemplo de uso rápido

1. Elegir opción `1` para registrar un cliente (ingresar DNI y nombre).
2. Elegir opción `2` para ver las bicicletas disponibles.
3. Elegir opción `4` para iniciar un alquiler (DNI del cliente, ID de bicicleta,
   hora de inicio en formato HH:MM).
4. Elegir opción `5` para finalizar el alquiler (número de alquiler y hora de
   finalización). El sistema calculará el tiempo de uso y el importe.
5. Elegir opción `8` para ver las estadísticas generales de utilización.
6. Elegir opción `9` para salir del sistema.

## Uso de Inteligencia Artificial

Este proyecto fue desarrollado con asistencia de Claude (Anthropic) como
herramienta de apoyo. Se utilizó para:

- Proponer la estructura modular inicial del proyecto (separación en archivos
  por responsabilidad: clientes, bicicletas, alquileres, estadísticas,
  validaciones).
- Generar una primera versión del código de cada módulo.
- Sugerir validaciones de datos (DNI, horarios, opciones de menú) y mensajes
  de error claros para el usuario.
- Realizar pruebas automatizadas del flujo del programa (caso válido y caso
  con error) para verificar su correcto funcionamiento.

Todo el equipo revisó, ejecutó y comprende el funcionamiento completo del
código, pudiendo justificar las decisiones de diseño tomadas (modularización,
tipos de datos utilizados, lógica de cálculo de tiempo e importe, y manejo de
errores) ante el tribunal evaluador.



