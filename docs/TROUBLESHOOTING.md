# Solución de Problemas (Troubleshooting)

## Errores Comunes

### 1. Error: `ModuleNotFoundError: No module named 'src'`
**Causa:** El directorio raíz no está en el `PYTHONPATH`.
**Solución:** Ejecuta los comandos desde la raíz del proyecto o usa `$env:PYTHONPATH="."` en Windows.

### 2. El servidor no inicia (Puerto 8000 ocupado)
**Causa:** Otra aplicación está usando el puerto por defecto de FastAPI.
**Solución:** Cambia el puerto: `uvicorn src.backend.api:app --reload --port 8001`.

### 3. Resultados de auditoría vacíos
**Causa:** El sitio web bloquea las peticiones automáticas (Scraping).
**Solución:** DAT intenta usar headers de navegador básicos, pero algunos sitios con protección avanzada (Cloudflare) pueden bloquear el análisis automático.

### 4. Base de datos bloqueada
**Causa:** Dos procesos intentando escribir en `accessibility_toolkit.db` al mismo tiempo.
**Solución:** Asegúrate de no tener múltiples instancias del servidor corriendo.
