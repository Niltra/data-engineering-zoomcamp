""" @bruin
name: ingestion.trips
type: python
@bruin """

import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

print("=== INICIANDO DESCARGA DE DATOS ===")
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
df = pd.read_parquet(url)

print(f"=== DESCARGA COMPLETADA: {len(df)} registros ===")
print("=== SUBIENDO A BIGQUERY (MODO MANUAL EXPLÍCITO)... ===")

# 1. Leemos tus credenciales locales directamente
credenciales = service_account.Credentials.from_service_account_file(
    'de-zoomcamp-2026-500215-717c8ac5a5ef.json'
)

# 2. Subida explícita usando pandas_gbq directamente
pandas_gbq.to_gbq(
    df,
    destination_table='ingestion.trips',
    project_id='de-zoomcamp-2026-500215',
    if_exists='replace',
    credentials=credenciales,
    location='EU'
)

print("=== SUBIDA COMPLETADA CON ÉXITO ===")