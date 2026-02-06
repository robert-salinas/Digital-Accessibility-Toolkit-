# ADR 0001: Enfoque "Accessible-First"

## Estado
Aceptado

## Contexto
Muchas herramientas de accesibilidad fallan en ser accesibles ellas mismas. Esto crea una barrera para los propios expertos o usuarios con discapacidad que quieren mejorar la web.

## Decisión
Hemos decidido que DAT debe cumplir estrictamente con WCAG 2.1 AAA en su propia interfaz. Esto incluye:
- Contraste superior a 7:1.
- Navegación completa por teclado.
- Etiquetas claras y semántica HTML correcta.
- Sin dependencia de frameworks de JS pesados que puedan romper la experiencia del lector de pantalla.

## Consecuencias
- La interfaz es simple y minimalista.
- El mantenimiento es más sencillo al usar estándares web puros.
- Demostramos con el ejemplo que la accesibilidad es posible y estética.
