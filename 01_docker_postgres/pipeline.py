import pandas as pd
from sqlalchemy import create_engine

# 1. CREACIÓN DEL PUENTE (Engine)
# Formato: dialecto://usuario:contraseña@host:puerto/base_de_datos
engine = create_engine('postgresql://postgres:root@host.docker.internal:5432/postgres')

# 2. EXTRACCIÓN Y TRANSFORMACIÓN
url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
df = pd.read_csv(url, nrows=100)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# 3. CARGA (Inyección en la Base de Datos)
# if_exists='replace' destruye la tabla si ya existía y la vuelve a crear limpia
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='replace', index=False)

print("¡Extracción, transformación e inyección completadas con éxito!")