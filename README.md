# 🧮 Calculadora Flask - Proyecto CI/CD Lopez

Una aplicación web de calculadora construida con Flask que implementa un flujo completo de integración continua y entrega continua (CI/CD).

## 📁 Estructura del Proyecto

```
├── app.py                    # Aplicación Flask principal
├── calculator.py             # Lógica de la calculadora
├── templates/
│   └── index.html           # Interfaz web de la calculadora
├── requirements.txt          # Dependencias de Python
├── test_calculator.py        # Pruebas unitarias completas
├── Dockerfile               # Configuración de Docker
├── docker-compose.yml       # Stack para despliegue en VPS
├── stack-setup.md           # Instrucciones de configuración del VPS
└── .github/
    └── workflows/
        └── ci.yml           # Pipeline CI/CD completo
```

## 🚀 Pipeline CI/CD

### Características del Pipeline:
- ✅ **Tests automatizados**: Ejecuta pytest con 7 tests completos
- ✅ **Build de imagen Docker**: Construye imagen con tag `lopez:1.0.5`
- ✅ **Publicación en GHCR**: Sube imagen a GitHub Container Registry
- ✅ **Despliegue automático**: Deploy automático al VPS sin intervención manual
- ✅ **Rama específica**: Trabaja exclusivamente en rama `lopez`

### Flujo del Pipeline:
1. **Test Stage**: Ejecuta todas las pruebas unitarias
2. **Build Stage**: Construye y publica imagen Docker
3. **Deploy Stage**: Despliega automáticamente al VPS

## 🌐 Despliegue en Producción

### URL de Producción:
**https://lopez.byronrm.com**

### Configuración del VPS:
- **Stack**: Docker Compose con Traefik
- **Imagen**: `ghcr.io/alisson714/alissonvelez5tob-alisson/lopez:1.0.5`
- **Puerto interno**: 5000
- **Subdominio**: lopez.byronrm.com
- **SSL**: Automático con Let's Encrypt

## 🧪 Tests Automatizados

El proyecto incluye 7 tests completos que validan:
- ✅ Suma de números positivos y negativos
- ✅ Resta de números
- ✅ Multiplicación
- ✅ División normal
- ✅ División por cero (manejo de errores)
- ✅ Operaciones con cero

```bash
python -m pytest test_calculator.py -v
```

## 🚀 Instalación Local

### Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar repositorio:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   git checkout lopez
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar tests:**
   ```bash
   python -m pytest test_calculator.py -v
   ```

4. **Ejecutar aplicación:**
   ```bash
   python app.py
   ```
   La aplicación estará disponible en: http://localhost:5000

## 🌟 Características

### Aplicación Flask
- ✅ Interfaz web moderna y responsive
- ✅ Operaciones: suma, resta, multiplicación, división
- ✅ Validación de errores (división por cero, entradas inválidas)
- ✅ API REST JSON
- ✅ Diseño atractivo con CSS

### Operaciones Disponibles
- **Suma** ➕
- **Resta** ➖ 
- **Multiplicación** ✖️
- **División** ➗ (con protección contra división por cero)

## 🔧 API Endpoints

### POST /calculate
Realiza cálculos matemáticos.

**Request Body:**
```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

**Operaciones disponibles:**
- `add` - Suma
- `subtract` - Resta
- `multiply` - Multiplicación
- `divide` - División

**Response (éxito):**
```json
{
  "result": 15
}
```

**Response (error):**
```json
{
  "error": "No se puede dividir por cero"
}
```

## 🧪 Pruebas

Ejecutar las pruebas unitarias:
```bash
python -m pytest test_calculator.py
```

## 🚀 Despliegue en Render (Gratuito)

### Opción 1: Deploy desde GitHub (Recomendado)
1. Ve a [Render.com](https://render.com)
2. Crea una cuenta gratuita
3. Haz clic en "New +" → "Web Service"
4. Conecta tu repositorio de GitHub: `Alisson714/AlissonVelez5toB`
5. Selecciona la rama `alisson`
6. Render detectará automáticamente tu Dockerfile
7. Configura:
   - **Name:** calculadora-alisson
   - **Environment:** Docker
   - **Plan:** Free
8. ¡Deploy automático!

### Opción 2: Deploy con render.yaml
Tu proyecto incluye `render.yaml` para configuración automática:
- **Puerto:** 10000 (estándar de Render)
- **Build:** Dockerfile
- **Start Command:** `python app.py`
- **Health Check:** Configurado en `/`
- **Auto Deploy:** Habilitado

### Configuración Render
- **Plan gratuito:** Ilimitado
- **Sleep:** Después de 15 min de inactividad
- **SSL:** Gratuito y automático
- **Dominio:** `tu-app.onrender.com`

## 🐳 Docker Local

Para pruebas locales con Docker:
```bash
docker build -t calculadora-flask .
docker run -p 5000:5000 calculadora-flask
```

## 📱 Uso de la Interfaz Web

1. Abre tu navegador en http://localhost:5000
2. Ingresa el primer número
3. Selecciona la operación deseada
4. Ingresa el segundo número
5. Haz clic en "Calcular"
6. Ve el resultado instantáneamente

## 🛠️ Desarrollo

La aplicación está estructurada de manera modular:

- **`Calculator` class**: Contiene la lógica de las operaciones matemáticas
- **Flask app**: Maneja las rutas web y la API REST
- **Templates**: Interfaz HTML con JavaScript para interactividad
- **Tests**: Pruebas unitarias para validar la funcionalidad

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.