# Módulo 4: Analytics Engineering con dbt

Este módulo aborda la capa de transformación dentro del Data Warehouse (BigQuery) utilizando **dbt** (Data Build Tool), aplicando las mejores prácticas de ingeniería de software a los datos.

## Propósito
En lugar de escribir procedimientos almacenados complejos, utilizamos dbt para transformar los datos crudos almacenados en BigQuery, limpiándolos y estructurándolos para que estén listos para su explotación por herramientas de Inteligencia de Negocios (BI) o equipos de analítica.

## Estructura del proyecto dbt
- `dbt_project.yml`: Archivo maestro de configuración de dbt donde se definen los parámetros y variables a nivel global.
- `models/`: Carpeta que contiene los scripts SQL (con plantillas Jinja) que dbt compilará y ejecutará:
  - **Staging**: Modelos encargados de la ingesta inicial, casteo de tipos de datos y renombramiento de columnas.
  - **Core**: Modelos analíticos finales, como `fact_yellow_trips` (tabla de hechos de los viajes) y tablas de dimensiones (`dim_zones`), optimizados para un rendimiento de consulta rápido.
- `tests/`: Definiciones de pruebas de calidad de datos para asegurar integridad, unicidad y ausencia de nulos en columnas clave.
- `macros/`: Funciones reutilizables escritas en Jinja para simplificar transformaciones repetitivas en SQL.

## Cómo ejecutarlo

1. **Instalación**:
   Asegúrate de tener instalado dbt-bigquery:
   ```bash
   pip install dbt-bigquery
   ```
2. **Configurar el perfil**:
   Debes configurar tu archivo `profiles.yml` (normalmente en `~/.dbt/profiles.yml`) para apuntar al proyecto de GCP mediante las credenciales de tu Service Account.
3. **Ejecución y Testeo**:
   Dentro de este directorio, ejecuta la construcción completa del proyecto:
   ```bash
   dbt build
   ```
   Esto ejecutará tanto los modelos (compilando el SQL y ejecutándolo en BigQuery) como las pruebas asociadas a la calidad del dato.
