import os
import sys
import urllib.request
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. EL ESCUDO ANTI-MICROSOFT STORE
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# 2. DESCARGA DE DATOS REALES (Enero 2023 - ~3 millones de registros)
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
file_name = "yellow_tripdata_2023-01.parquet"

if not os.path.exists(file_name):
    print(f"📥 Descargando {file_name} de internet... (Unos 50MB, dale un momento)")
    urllib.request.urlretrieve(url, file_name)
    print("✅ ¡Descarga completada!")

# 3. LEVANTAR EL MOTOR SPARK
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("ProcesamientoBatchTaxis") \
    .getOrCreate()

print("🔥 Motor Spark listo. Leyendo millones de registros...")

# 4. LEER DATOS MASIVOS
# En Pandas esto ahogaría la RAM. En Spark, es instantáneo porque usa evaluación perezosa (Lazy Evaluation)
df = spark.read.parquet(file_name)

# 5. TRANSFORMACIÓN Y CÁLCULO
# Como si fuera un GROUP BY en SQL, pero ejecutado en paralelo por tu CPU
print("\n--- Calculando métricas de 3 millones de viajes ---")
df.groupBy("VendorID").agg(
    F.count("*").alias("total_viajes"),
    F.round(F.avg("total_amount"), 2).alias("importe_medio_usd")
).show()

# 6. PARTICIONADO (La magia de Spark)
# En un entorno real (Linux/Docker) aquí guardaríamos el archivo con .write.parquet()
# Como estamos en Windows local, simplemente particionamos en memoria y contamos las particiones.
df_particionado = df.repartition(4)

print("\n--- Demostración de particionado en memoria ---")
print(f"Número de particiones listas para ser enviadas a una base de datos: {df_particionado.rdd.getNumPartitions()}")

print("\n🚀 ¡Procesamiento Batch completado con éxito! (Sin usar el disco duro)")
spark.stop()