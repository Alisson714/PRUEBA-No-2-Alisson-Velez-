# Stack Setup para VPS - Lopez

## Configuración del Stack en el VPS

### 1. Estructura de directorios en el VPS
```bash
/opt/stacks/lopez-app/
├── docker-compose.yml
└── .env
```

### 2. Comandos para configurar el stack en el VPS

```bash
# Crear directorio del stack
sudo mkdir -p /opt/stacks/lopez-app

# Copiar docker-compose.yml al VPS
scp docker-compose.yml user@vps:/opt/stacks/lopez-app/

# Crear red externa para Traefik (si no existe)
docker network create web

# Iniciar el stack
cd /opt/stacks/lopez-app
docker-compose up -d
```

### 3. Variables de entorno necesarias en GitHub Secrets

- `VPS_HOST`: IP o dominio del VPS
- `VPS_USER`: Usuario SSH del VPS
- `VPS_SSH_KEY`: Clave privada SSH para acceder al VPS

### 4. Configuración del subdominio

El subdominio `lopez.byronrm.com` debe apuntar a la IP del VPS donde está configurado Traefik.

### 5. Verificación del despliegue

Una vez desplegado, la aplicación estará disponible en:
- https://lopez.byronrm.com

### 6. Logs y monitoreo

```bash
# Ver logs del contenedor
docker logs lopez-calculator

# Ver estado del stack
docker-compose ps