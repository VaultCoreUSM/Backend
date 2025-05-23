# VaultCore MVP - Backend

Este es el backend para el proyecto VaultCore MVP, desarrollado con FastAPI y PostgreSQL.

## Prerrequisitos

- Docker y Docker Engine (o Docker Desktop) instalados y corriendo.

## Cómo Ejecutar la Aplicación (Usando Docker)

Recomendamos usar una red Docker personalizada para facilitar la comunicación entre el backend y la base de datos.

### Paso 1: Crear una Red Docker

Abre tu terminal y ejecuta:

```bash
docker network create vaultcore-net
```

### Paso 2: Ejecutar el Contenedor de PostgreSQL

Ejecuta el siguiente comando para iniciar un contenedor PostgreSQL en la red que acabas de crear. Este comando también crea un volumen para persistir los datos de la base de datos.

```bash
docker run -d --name vaultcore-postgres --network vaultcore-net -e POSTGRES_USER=tu_usuario_pg -e POSTGRES_PASSWORD=tu_contraseña_pg -e POSTGRES_DB=vaultcore_mvp_db -v vaultcore_pg_data:/var/lib/postgresql/data postgres:15
```

### Paso 3: Construir la Imagen Docker del Backend

Navega en tu terminal al directorio backend/. Luego, ejecuta el siguiente comando para construir la imagen Docker para la aplicación backend:

```bash
docker build -t vaultcore-backend .
```

### Paso 4: Ejecutar el Contenedor del Backend

Ahora, ejecuta el contenedor del backend, conectándolo a la misma red Docker y configurando la variable de entorno DATABASE_URL para que apunte al contenedor de PostgreSQL por su nombre (vaultcore-postgres).

```bash
docker run -d --name vaultcore-backend-app --network vaultcore-net -p 8000:8000 -e DATABASE_URL="postgresql://tu_usuario_pg:tu_contraseña_pg@vaultcore-postgres:5432/vaultcore_mvp_db" vaultcore-backend
```

### Paso 5: ¡Probar!

Una vez que ambos contenedores (vaultcore-postgres y vaultcore-backend-app) estén corriendo:

- Abre tu navegador y ve a http://localhost:8000/. Deberías ver el mensaje de bienvenida.
- Accede a la documentación interactiva de la API en http://localhost:8000/docs para probar los endpoints (por ejemplo, crear una cámara)

## Limpieza

Para detener y eliminar los contenedores y la red:

```bash
docker stop vaultcore-backend-app vaultcore-postgres
docker rm vaultcore-backend-app vaultcore-postgres
docker network rm vaultcore-net
```

Para eliminar también el volumen de datos de PostgreSQL (¡esto borrará los datos de la BD!):

```bash
docker volume rm vaultcore_pg_data
```

Para eliminar la imagen Docker del backend:

```bash
docker rmi vaultcore-backend
```
