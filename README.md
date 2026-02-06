# 🚀 Digital Accessibility Toolkit (DAT) v0.1.0

**Digital Accessibility Toolkit (DAT)** es una herramienta de ingeniería diseñada para auditar, gestionar y optimizar la accesibilidad web mediante la extracción automática de barreras digitales, asegurando que cada sitio sea inclusivo y cumpla con los estándares internacionales WCAG 2.1.

## ✨ Características

- **🔒 Historial de Auditorías (SQLite):** Cada análisis cuenta con un registro completo de cambios, permitiendo el seguimiento de mejoras y retrocesos en la accesibilidad a lo largo del tiempo.
- **🧠 Análisis Automático de Accesibilidad:** Detecta automáticamente fallos en la estructura del proyecto (alt-text, jerarquía de encabezados, etiquetas de formularios, etc.) y genera recomendaciones técnicas precisas.
- **⚡ Motor de Auditoría de Alto Rendimiento:** Basado en parsing semántico del DOM para identificar problemas de contraste, navegación por teclado e idioma en milisegundos.
- **🛠️ Reportes Inteligentes y Políglotas:** Traduce problemas técnicos complejos en explicaciones claras ("por qué" y "cómo") en múltiples idiomas: Español, Portugués e Inglés.
- **🌐 Interfaz Accessible-First:** La herramienta misma es un modelo de accesibilidad AAA, diseñada para funcionar perfectamente con lectores de pantalla y navegación exclusiva por teclado.

## 🚀 Instalación Rápida

Para poner en marcha el proyecto en tu entorno local:

```bash
# 1. Clonar el repositorio
git clone https://github.com/robertesteban/Digital-Accessibility-Toolkit.git
cd Digital-Accessibility-Toolkit

# 2. Instalar dependencias en modo editable
pip install -e .
```

## 🕹️ Uso Básico

Para gestionar y optimizar la accesibilidad de tus sitios de forma eficiente:

### Inicialización y Servidor
```bash
# Iniciar el servidor de la API
uvicorn src.backend.api:app --reload

# Abrir el frontend accesible
# Abre src/frontend/index.html en tu navegador favorito
```

### Gestión de Auditorías
- **Auditar un sitio:** Pega la URL en la interfaz web para obtener un desglose detallado de los problemas encontrados.
- **Consultar Historial:** Accede a `/history` en la API para ver la evolución de los puntajes de accesibilidad.
- **Exportar Reportes:** Obtén resultados listos para compartir con desarrolladores o stakeholders.

## � Estructura de Decisiones (ADR)

El proyecto mantiene registros estructurados (Architecture Decision Records) para asegurar el rigor arquitectónico:

- **[ADR-0001: Accessible-First Design](docs/ADR/0001-why-accessible-first.md):** Justificación del uso de estándares AAA en la propia interfaz de la herramienta.
- **[ADR-0002: Análisis Semántico con BeautifulSoup](docs/ARCHITECTURE.md):** Racional detrás de la detección automática de barreras sin frameworks pesados.
- **[ADR-0003: Persistencia en SQLite](docs/ARCHITECTURE.md):** Diseño del sistema de seguimiento histórico para medir impacto social.

**Estados Soportados:**
- **Proposed:** La decisión está en fase de revisión.
- **Accepted:** La decisión ha sido aprobada e implementada.
- **Deprecated:** La decisión ya no es relevante.

## � Documentación Adicional

- [🏛️ Arquitectura y Decisiones de Diseño](docs/ARCHITECTURE.md)
- [🚀 Historias de Impacto Real](docs/IMPACT.md)
- [🤝 Guía de Contribución](docs/CONTRIBUTING.md)

---
Desarrollado con ❤️ para ingenieros y organizaciones que buscan elevar la calidad de la inclusión digital mediante el rigor técnico y la empatía.
