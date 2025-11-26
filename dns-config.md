# Configuración DNS - lopez.byronrm.com

## Configuración del Subdominio

### Registro DNS Requerido:
```
Tipo: A
Nombre: lopez
Dominio: byronrm.com
Valor: [IP_DEL_VPS]
TTL: 300
```

### Resultado Final:
- **Subdominio**: lopez.byronrm.com
- **Apunta a**: IP del VPS donde está configurado Traefik
- **SSL**: Automático con Let's Encrypt
- **Puerto**: 443 (HTTPS)

## Verificación del DNS

### Comandos para verificar:
```bash
# Verificar resolución DNS
nslookup lopez.byronrm.com

# Verificar conectividad
ping lopez.byronrm.com

# Verificar certificado SSL
curl -I https://lopez.byronrm.com
```

## Configuración en Traefik

El archivo `docker-compose.yml` ya incluye las etiquetas necesarias para Traefik:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.lopez.rule=Host(`lopez.byronrm.com`)"
  - "traefik.http.routers.lopez.tls=true"
  - "traefik.http.routers.lopez.tls.certresolver=letsencrypt"
  - "traefik.http.services.lopez.loadbalancer.server.port=5000"
```

## Estado del Despliegue

Una vez configurado correctamente:
- ✅ DNS apunta al VPS
- ✅ Traefik maneja el routing
- ✅ SSL automático
- ✅ Aplicación accesible en https://lopez.byronrm.com

## Troubleshooting

### Si el subdominio no funciona:
1. Verificar que el DNS esté propagado
2. Comprobar que Traefik esté ejecutándose
3. Verificar logs del contenedor: `docker logs lopez-calculator`
4. Comprobar red Docker: `docker network ls`