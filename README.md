# Data Engineering Zoomcamp Portfolio 🚀

¡Bienvenido/a a mi repositorio del Data Engineering Zoomcamp! Aquí he documentado e implementado mi propia versión de los módulos del curso, construyendo una infraestructura completa de datos desde cero, pasando por la orquestación, transformación y procesamiento tanto en batch como en streaming.

## 🏗 Arquitectura del Proyecto

Este repositorio contiene múltiples pipelines y despliegues de infraestructura divididos en 7 módulos lógicos:

### [01] Docker y PostgreSQL (`/01_docker_postgres`)
- **Objetivo**: Configuración del entorno local y primera ingesta de datos.
- **Tecnologías**: Docker, Docker Compose, PostgreSQL, pgAdmin, Python (Pandas/SQLAlchemy).
- **Detalle**: Pipeline en Python que descarga datos masivos de los taxis de NYC en formato `.csv.gz`, los lee en trozos (chunks) usando Pandas y los inyecta secuencialmente en una base de datos PostgreSQL local contenerizada.

### [02] Infraestructura en la Nube (`/02_terraform_gcp`)
- **Objetivo**: Despliegue de Infraestructura como Código (IaC).
- **Tecnologías**: Terraform, Google Cloud Platform (GCP), Google Cloud Storage (Data Lake), BigQuery (Data Warehouse).
- **Detalle**: Scripts de Terraform para automatizar la creación de un Data Lake en Google Cloud Storage y el conjunto de datos en BigQuery de forma reproducible, aplicando buenas prácticas de estado y variables.

### [03] Orquestación de Workflows (`/03_kestra`)
- **Objetivo**: Automatización de los pipelines de datos.
- **Tecnologías**: Kestra.
- **Detalle**: Incluye el archivo de despliegue `docker-compose.yml` para levantar Kestra y una carpeta `flows/` con los flujos (pipelines) YAML que automatizan la extracción de datos web y su carga a GCS de forma calendarizada.

### [04] Analytics Engineering (`/04_dbt_analytics`)
- **Objetivo**: Transformación de datos en el Data Warehouse.
- **Tecnologías**: dbt (Data Build Tool), SQL.
- **Detalle**: Modelos de dbt para limpiar, transformar y agregar los datos crudos de BigQuery. Contiene modelos `staging` (limpieza y casteo de tipos) y modelos `core` (`fact_yellow_trips` y `dim_zones`) listos para ser consumidos por herramientas de BI.

### [05] Calidad de Datos (`/05_bruin_pipeline`)
- **Objetivo**: Validación de datos y linaje.
- **Tecnologías**: Bruin.
- **Detalle**: Implementación de una pipeline alternativa y chequeos de calidad de datos (Data Quality) garantizando que no haya nulos en claves principales y asegurando el enrutamiento correcto hacia EU en BigQuery.

### [06] Procesamiento Batch (`/06_spark_batch`)
- **Objetivo**: Procesamiento distribuido de datos masivos.
- **Tecnologías**: Apache Spark, PySpark.
- **Detalle**: Scripts (`procesamiento_batch.py`) para leer archivos Parquet masivos (millones de registros) mediante evaluación perezosa y particionado en memoria de clústeres locales, extrayendo métricas y agrupaciones en tiempo récord.

### [07] Procesamiento en Tiempo Real (`/07_kafka_streaming`)
- **Objetivo**: Ingesta y consumo de flujos de eventos.
- **Tecnologías**: Apache Kafka (KRaft), Python.
- **Detalle**: Arquitectura de streaming local usando contenedores Docker. Contiene un `producer.py` que simula viajes de taxi en tiempo real y scripts consumidores/procesadores (`stream_processor.py`) que realizan agregaciones con estado (Stateful Aggregations) sobre el flujo vivo.

## 🔐 Seguridad y Privacidad
La seguridad ha sido una prioridad a lo largo de este proyecto:
- Los identificadores de proyecto (Project IDs) y nombres de Buckets en repositorios públicos han sido parametrizados o tapados.
- Las contraseñas, claves `.pem` y `.json` (Service Accounts) están estrictamente ignoradas a nivel de Git mediante un exhaustivo `.gitignore`.
- Los datos crudos pesados (`.parquet` o `.csv` de más de 50MB) tampoco se suben al repositorio.

---

*Desarrollado durante la edición del Data Engineering Zoomcamp.*
