# Ejemplos de Uso - DAT

## Escenario 1: Auditoría Web Rápida
1. Inicia el servidor: `uvicorn src.backend.api:app --reload`
2. Abre `src/frontend/index.html`.
3. Ingresa la URL: `https://example.com`.
4. Visualiza el reporte de problemas de contraste y etiquetas faltantes.

## Escenario 2: Uso de la API (cURL)
Puedes auditar un sitio directamente desde la terminal:

```bash
curl -X POST "http://localhost:8000/audit" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com", "lang": "es"}'
```

## Escenario 3: Consulta de Historial
Para ver auditorías pasadas y comparar el progreso:

```bash
curl "http://localhost:8000/history?limit=5"
```
