import os
import sys
from pyspark.sql import SparkSession

# 1. EL ESCUDO ANTI-MICROSOFT STORE
# Obligamos a Spark a usar el ejecutable exacto de nuestro entorno virtual (.venv)
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# 2. Levantar el Contexto de Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("TestDeTaxis") \
    .getOrCreate()

print("🔥 ¡Motor de Spark arrancado con éxito!")

# 3. Crear unos datos de prueba
datos = [
    ("TAXI-01", "Manhattan", 15.50),
    ("TAXI-02", "Brooklyn", 22.00),
    ("TAXI-03", "Queens", 10.75)
]
columnas = ["id_taxi", "zona", "importe"]

# 4. Construir el DataFrame distribuido y mostrarlo
df = spark.createDataFrame(datos, columnas)
print("\n--- Tabla de Taxis Procesada ---")
df.show()

# 5. Apagar el motor ordenadamente
spark.stop()