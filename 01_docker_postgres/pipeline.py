import pandas as pd
from sqlalchemy import create_engine
from time import time # Importamos esto para medir con un cronómetro cuánto tarda cada lote

engine = create_engine('postgresql://postgres:root@host.docker.internal:5432/postgres')
url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

# 1. EL DISPENSADOR (Iterator)
# Le decimos a Pandas: "No leas todo. Prepárate para darme bloques de 100.000 filas cada vez que te lo pida"
df_iter = pd.read_csv(url, iterator=True, chunksize=100000)

# 2. PREPARACIÓN DE LA TABLA (Primer bloque)
df = next(df_iter) # Extraemos el primer bloque de la cinta
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# Inyectamos solo la estructura vacía primero para asegurar que la tabla existe y está limpia
df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace', index=False)

# Metemos los datos de ese primer bloque. Fíjate que ahora usamos 'append' (añadir al final)
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append', index=False)
print("Estructura creada y primer lote inyectado. Arrancando motor masivo...")

# 3. EL BUCLE INFINITO (La cinta transportadora)
while True:
    try:
        t_start = time() # Pulsamos el cronómetro
        
        df = next(df_iter) # Pedimos el siguiente bloque de 100.000
        
        # Transformamos las fechas
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        # Inyectamos añadiendo al final (append)
        df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append', index=False)
        
        t_end = time() # Paramos el cronómetro
        print(f"Lote inyectado con éxito. Tiempo de procesado: {t_end - t_start:.3f} segundos")
        
    except StopIteration:
        # Cuando 'next(df_iter)' ya no tenga más datos, saltará este error. Lo capturamos para salir limpiamente.
        print("¡No quedan más datos! Ingesta masiva completada.")
        break