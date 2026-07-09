import json
import time
from kafka import KafkaProducer

# 1. Función para convertir nuestro diccionario de Python a JSON (formato universal de Kafka)
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# 2. Configurar el Productor apuntando a tu contenedor de Docker
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer
)

if __name__ == '__main__':
    print("🚕 Iniciando centralita de taxis en tiempo real...")
    
    # Simular 10 viajes entrando al sistema
    for i in range(1, 11):
        viaje = {
            "taxi_id": f"TAXI-{1000 + i}",
            "distancia_millas": 2.5 + i,
            "importe_total": 15.0 + (i * 1.5)
        }
        
        print(f"Enviando evento al clúster: {viaje}")
        
        # 3. Enviar el mensaje al Topic (canal) llamado "viajes_taxi_nyc"
        producer.send("viajes_taxi_nyc", value=viaje)
        
        # Pausa de 1 segundo para simular el tiempo real
        time.sleep(1)

    # Asegurarnos de que todos los mensajes han salido de la memoria RAM hacia el clúster
    producer.flush()
    print("✅ ¡Todos los viajes emitidos con éxito!")