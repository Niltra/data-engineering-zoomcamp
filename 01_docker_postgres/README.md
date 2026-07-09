# Módulo 1: Docker y PostgreSQL

Este módulo se centra en la configuración del entorno local y la primera ingesta de datos masivos. Utiliza **Docker** para contenerizar la base de datos y un script en Python para procesar e insertar los datos.

## Propósito
El objetivo principal es descargar un volumen considerable de datos (los viajes de taxi de NYC en formato `.csv.gz`), y cargarlos en una base de datos PostgreSQL alojada localmente mediante Docker, gestionando la memoria con lecturas particionadas.

## Archivos principales
- `docker-compose.yaml`: Archivo de orquestación local que levanta dos contenedores:
  - **PostgreSQL**: La base de datos relacional donde se almacenarán los viajes.
  - **pgAdmin**: Interfaz gráfica para gestionar e inspeccionar la base de datos PostgreSQL.
- `Dockerfile`: Archivo para crear una imagen personalizada (en caso de requerir un entorno Python aislado).
- `pipeline.py`: Script en Python que emplea Pandas para descargar los datos de internet, leerlos en bloques (chunks) de 100.000 filas (para no saturar la memoria RAM) y escribirlos en la base de datos usando SQLAlchemy.

## Cómo ejecutarlo

1. **Levantar la infraestructura**:
   ```bash
   docker-compose up -d
   ```
   Esto iniciará PostgreSQL en el puerto `5432` y pgAdmin en el puerto definido en el archivo `docker-compose.yaml`.

2. **Ejecutar la ingesta de datos**:
   Asegúrate de tener instaladas las librerías necesarias (`pandas`, `sqlalchemy`, `psycopg2-binary`) y ejecuta:
   ```bash
   python pipeline.py
   ```
   Verás en la consola cómo el script va insertando los datos por lotes y calculando el tiempo de ejecución.
