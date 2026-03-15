# 🚀 Digital Accessibility Toolkit (DAT) v0.2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![UI: Dark Engineering](https://img.shields.io/badge/UI-Dark%20Engineering-orange.svg)](#-estética-dark-engineering)

**Digital Accessibility Toolkit (DAT)** es una suite de ingeniería de alto rendimiento diseñada para auditar, gestionar y optimizar la accesibilidad web. Utiliza un motor de análisis semántico puro para detectar barreras digitales y asegurar el cumplimiento de los estándares **WCAG 2.1 AAA**.

---

## 🖥️ Interfaz de Escritorio (Native GUI)

A diferencia de las herramientas web convencionales, **DAT** se ejecuta como una aplicación de escritorio nativa, ofreciendo una experiencia de software de ingeniería robusta y profesional.

- **Ventana Independiente:** Ejecución fluida mediante `pywebview`.
- **Servidor Integrado:** Backend FastAPI que corre en segundo plano de forma automática.
- **Acceso Directo:** Launcher de un solo clic con creación automática de acceso directo en el escritorio.

## 🛠️ Características Principales

- **🎨 Estética "Dark Engineering":** Interfaz de alto contraste (#1A1F2E, #FFFFFF, #FF7A3D) diseñada para reducir la fatiga visual y maximizar la legibilidad (WCAG AAA).
- **🔒 Historial de Auditorías (SQLite):** Registro persistente de análisis para trackear la evolución de la accesibilidad.
- **🧠 Análisis Semántico Puro:** Detección de fallos en DOM (alt-text, jerarquía `H1-H6`, etiquetas de formularios, `tabindex`, etc.).
- **🌍 Motor Políglota:** Reportes técnicos explicativos en Español, Inglés y Portugués.
- **⚡ Performance de Ingeniería:** Análisis completo de sitios complejos en milisegundos.

## 🚀 Inicio Rápido (Windows)

La herramienta está optimizada para una experiencia "Zero Configuration" en Windows.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/robert-salinas/Digital-Accessibility-Toolkit-.git
   cd Digital-Accessibility-Toolkit-
   ```

2. **Lanzar la Aplicación:**
   Simplemente haz doble clic en el archivo:
   - 🕹️ **`run_app.bat`**

   *El launcher se encargará de crear el entorno virtual (.venv), instalar las dependencias y abrir la ventana de la aplicación automáticamente.*

## 🕹️ Uso de Ingeniería

- **Auditoría Central:** Pega la URL objetivo en la barra de entrada prominente.
- **Panel de Resultados:** Cuadrícula de tarjetas con desglose técnico de problemas (Críticos, Advertencias e Info).
- **Re-auditoría:** Acceso rápido desde el historial lateral para comparar cambios en tiempo real.

## 📝 Arquitectura y Decisiones (ADR)

- **[ADR-0001: Accessible-First Design](docs/ADR/0001-why-accessible-first.md):** Por qué la herramienta debe ser el estándar AAA que audita.
- **[ADR-0004: Unified GUI Strategy](docs/ARCHITECTURE.md):** Integración de FastAPI + PyWebView para una experiencia MVP profesional.

---

Desarrollado con el rigor técnico de **Robert Salinas** para ingenieros que no comprometen la calidad ni la inclusión digital.

> "La accesibilidad no es una característica, es un derecho fundamental de la arquitectura de software."
