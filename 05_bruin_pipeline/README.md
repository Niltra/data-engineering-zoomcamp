# Módulo 5: Data Quality y Linaje con Bruin

Este módulo explora una alternativa de pipeline de datos enfocada fuertemente en la validación y calidad de la información empleando **Bruin**.

## Propósito
Se implementa una pipeline robusta que no solo mueve datos, sino que realiza chequeos exhaustivos (Data Quality Checks) para garantizar la integridad de los mismos. Principalmente, aseguramos que las claves principales no contengan nulos y que el enrutamiento y procesamiento se realice de forma explícita en la región europea (`EU`) de BigQuery.

## Características de esta implementación
- **Validación incorporada**: Chequeos integrados antes y después de las transformaciones para detectar anomalías tempranas.
- **Enrutamiento geográfico**: Control explícito sobre dónde se ejecutan los cálculos y se almacenan los datos (región EU de GCP).
- **Linaje de datos**: Visibilidad end-to-end de cómo fluyen los datos desde su origen hasta la tabla final, facilitando la depuración y auditorías.

## Cómo ejecutarlo

1. **Instalar Bruin**:
   Si no lo tienes instalado, sigue la guía oficial en [getbruin.com](https://getbruin.com/docs/bruin/getting-started/introduction/installation.html) o instálalo vía su CLI.
2. **Configurar credenciales**:
   Asegúrate de tener las variables de entorno o configuraciones necesarias para conectar Bruin con tu proyecto de BigQuery.
3. **Ejecutar la pipeline**:
   Lanza la validación y transformación ejecutando el flujo definido en este directorio:
   ```bash
   bruin run
   ```
