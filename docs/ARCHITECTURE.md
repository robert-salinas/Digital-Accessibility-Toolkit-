# Arquitectura del Sistema - DAT

## Descripción General
Digital Accessibility Toolkit (DAT) es una aplicación web diseñada para auditar la accesibilidad de sitios web de manera sencilla y educativa.

## Stack Tecnológico
- **Backend**: Python con FastAPI para una API rápida y tipada.
- **Análisis**: BeautifulSoup4 para parsing de HTML y reglas personalizadas basadas en WCAG 2.1.
- **Frontend**: HTML5, CSS3 y Vanilla JavaScript, priorizando la accesibilidad nativa y el bajo peso.
- **Base de Datos**: SQLite para el almacenamiento local de auditorías históricas.

## Componentes
1. **API (FastAPI)**: Maneja las solicitudes de auditoría y sirve el historial.
2. **Analyzer**: Clase core que coordina los diferentes chequeos.
3. **Checks**: Módulos independientes para cada regla de accesibilidad (Alt-text, Headings, etc.).
4. **Report Generator**: Transforma resultados técnicos en explicaciones claras y accionables.
5. **Frontend**: Interfaz de usuario de alto contraste y compatible con lectores de pantalla.

## Flujo de Datos
1. El usuario ingresa una URL en el Frontend.
2. El Frontend envía un POST a `/audit`.
3. El Backend descarga el HTML de la URL.
4. El Analyzer ejecuta cada chequeo sobre el DOM.
5. Los resultados se guardan en SQLite y se devuelven al Frontend.
6. El Frontend muestra los resultados de forma accesible.
