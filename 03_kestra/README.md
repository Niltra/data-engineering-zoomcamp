# Módulo 3: Orquestación de Workflows con Kestra

Este módulo implementa la automatización y calendarización de nuestros pipelines de datos mediante **Kestra**, una plataforma moderna de orquestación.

## Propósito
El objetivo de este módulo es dejar atrás los scripts manuales y establecer un sistema automatizado que se encargue de la extracción periódica de datos desde la web (fuentes públicas de taxis) y de su carga eficiente hacia el Data Lake en Google Cloud Storage.

## Archivos principales
- `docker-compose.yml`: Archivo de configuración que levanta todos los componentes necesarios para correr Kestra en local (servidor, base de datos de backend, etc.).
- `flows/`: Carpeta que contiene las definiciones de los pipelines en formato YAML. Estos archivos declaran los pasos (tareas) a ejecutar de forma secuencial o paralela.

## Cómo ejecutarlo

1. **Levantar el orquestador Kestra**:
   Sitúate en este directorio y ejecuta:
   ```bash
   docker-compose up -d
   ```
2. **Acceder a la interfaz de usuario**:
   Una vez que los contenedores estén en funcionamiento, abre tu navegador y dirígete a `http://localhost:8080`.
3. **Desplegar y ejecutar flujos**:
   Desde la interfaz web de Kestra, puedes importar el contenido de los archivos YAML de la carpeta `flows/` y pulsar el botón **Execute** para ver gráficamente cómo transcurre el flujo de datos.
