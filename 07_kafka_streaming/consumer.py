import json
from kafka import KafkaConsumer

# 1. Función para decodificar los bytes que llegan de Kafka de vuelta a un diccionario Python
def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# 2. Configurar el Consumidor apuntando a nuestro Topic
consumer = KafkaConsumer(
    'viajes_taxi_nyc',                     # El canal (Topic) al que nos suscribimos
    bootstrap_servers=['localhost:9092'],  # Nuestro clúster en Docker
    auto_offset_reset='earliest',          # Instrucción clave: "Si soy nuevo, dame todos los mensajes desde el principio"
    value_deserializer=json_deserializer
)

if __name__ == '__main__':
    print("🎧 Servicio de monitorización conectado al clúster...")
    print("Esperando nuevos viajes... (Pulsa Ctrl+C para detener el servicio)\n")
    
    # 3. Bucle infinito: el programa se queda escuchando para siempre
    for mensaje in consumer:
        viaje = mensaje.value
        print(f"📥 [ALERTA] Viaje recibido -> El {viaje['taxi_id']} acaba de cobrar {viaje['importe_total']}$")