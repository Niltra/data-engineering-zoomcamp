# Módulo 7: Procesamiento en Tiempo Real con Apache Kafka

Este módulo cubre la ingesta, transporte y procesamiento continuo de datos utilizando arquitecturas orientadas a eventos en tiempo real (Streaming) con **Apache Kafka**.

## Propósito
Construir una infraestructura de streaming local para simular la recolección y análisis de viajes de taxi en vivo. En lugar de procesar lotes pasados (Batch), escuchamos un flujo constante de eventos e implementamos agrupaciones de estado (Stateful Aggregations) para tener métricas calculadas "al vuelo".

## Archivos principales
- `docker-compose.yml`: Archivo que despliega el *Broker* de Kafka utilizando KRaft (eliminando la antigua dependencia de Zookeeper).
- `producer.py`: Script en Python que actúa como origen de los datos. Simula la generación constante de eventos (nuevos viajes de taxi) y los inyecta en el *Topic* de Kafka.
- `stream_processor.py`: Script que consume los datos vivos procedentes del *Topic*, y realiza agregaciones en tiempo real (estado y métricas) sobre el flujo.
- `consumer.py`: (Opcional/Test) Consumidor básico para depurar o verificar la recepción pura de los mensajes generados por el productor.

## Cómo ejecutarlo

1. **Levantar el cluster de Kafka**:
   ```bash
   docker-compose up -d
   ```
2. **Iniciar el Procesador de Stream**:
   En una terminal, lanza el consumidor/procesador para que empiece a escuchar eventos (y se quede a la espera):
   ```bash
   python stream_processor.py
   ```
3. **Arrancar la Simulación (El Productor)**:
   En *otra terminal*, arranca el productor para comenzar a inyectar eventos de viajes:
   ```bash
   python producer.py
   ```
   Verás en la primera terminal cómo el procesador reacciona inmediatamente, extrayendo métricas y procesando la información sobre la marcha.
