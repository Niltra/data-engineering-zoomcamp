# Módulo 6: Procesamiento Batch con Apache Spark

Este módulo demuestra la capacidad de procesar grandes volúmenes de información en modo *Batch* utilizando procesamiento distribuido en memoria mediante **Apache Spark** (con PySpark).

## Propósito
El objetivo es demostrar cómo lidiar con archivos inmensos (millones de registros) que ahogarían la RAM tradicional utilizando herramientas como Pandas. Al emplear Spark, aprovechamos la *evaluación perezosa* y el *particionado* para calcular agregaciones sobre millones de filas de manera casi instantánea usando el clúster local de nuestra CPU.

## Archivos principales
- `procesamiento_batch.py`: Script de PySpark que:
  - Se encarga de descargar un archivo inmenso (`.parquet` con datos de Enero 2023, ~3M de registros) si no existe.
  - Inicia una sesión local de Spark empleando todos los núcleos disponibles (`local[*]`).
  - Ejecuta agregaciones (como número de viajes y promedios) utilizando procesamiento distribuido.
  - Demuestra cómo realizar el particionado de datos (ej. re-particionar en 4 fragmentos) simulando un flujo para Data Lakes o Data Warehouses.
- `test_spark.py`: Pequeño script para comprobar y testear que el motor de Spark está correctamente configurado y funcionando en la máquina host.

## Cómo ejecutarlo

1. **Requisitos Previos**:
   - Tener instalado Java (JDK 8 o superior).
   - Tener instaladas las librerías de Python requeridas (`pyspark`).
2. **Ejecución**:
   Simplemente ejecuta el script de procesamiento:
   ```bash
   python procesamiento_batch.py
   ```
   El script se encargará automáticamente de conseguir los datos y calcular las métricas reportando los resultados en consola.
