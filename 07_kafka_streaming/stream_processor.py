import json
from kafka import KafkaConsumer

# Función para decodificar los bytes que llegan de Kafka
def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Nos conectamos al clúster
consumer = KafkaConsumer(
    'viajes_taxi_nyc',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # Para leer todo el histórico si es necesario
    value_deserializer=json_deserializer
)

print("📊 Iniciando Motor de Stream Processing...")
print("Calculando métricas de negocio en tiempo real... (Pulsa Ctrl+C para salir)\n")

# Variables de ESTADO (se mantienen en memoria mientras fluyen los datos)
facturacion_total = 0.0
viajes_procesados = 0

# Bucle infinito procesando el stream
for mensaje in consumer:
    viaje = mensaje.value
    
    # 1. Transformación / Agregación al vuelo
    facturacion_total += viaje['importe_total']
    viajes_procesados += 1
    
    # 2. Output del procesamiento (Sink)
    print(f"🚕 [PROCESADO] Viaje de {viaje['taxi_id']} | 💰 Recaudación acumulada: {facturacion_total:.2f}$ | 📈 Total viajes: {viajes_procesados}")