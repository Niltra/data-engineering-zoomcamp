# Módulo 2: Infraestructura como Código (Terraform & GCP)

Este módulo gestiona el despliegue automático de toda la infraestructura necesaria en la nube (Google Cloud Platform) mediante **Terraform**.

## Propósito
En lugar de crear buckets de almacenamiento y bases de datos manualmente desde la consola web, utilizamos la Infraestructura como Código (IaC) para garantizar que el entorno sea reproducible, versionable y libre de errores humanos.

## Archivos principales
- `main.tf`: Es el script principal de Terraform. Contiene las directivas para:
  - Configurar el proveedor de Google Cloud.
  - Crear un **Data Lake** aprovisionando un bucket en Google Cloud Storage (GCS).
  - Crear un **Data Warehouse** declarando un dataset en Google BigQuery.
- `flows/`: Flujos adicionales o dependencias (si aplica).
- `keys/`: (Oculta por seguridad) Carpeta destinada a alojar el archivo de credenciales o Service Account JSON necesario para que Terraform se autentique con GCP.

## Cómo ejecutarlo

1. **Inicializar Terraform**:
   Prepara el directorio y descarga los proveedores necesarios.
   ```bash
   terraform init
   ```

2. **Previsualizar los cambios**:
   Muestra un plan de ejecución de lo que Terraform va a crear en GCP.
   ```bash
   terraform plan
   ```

3. **Aplicar la infraestructura**:
   Confirma y despliega los recursos en la nube.
   ```bash
   terraform apply
   ```
   *(Escribe `yes` cuando lo solicite).*

> **Nota de Seguridad**: Nunca subas el archivo de tu *Service Account* (`.json`) a GitHub. Asegúrate de que esté listado en el `.gitignore`.
