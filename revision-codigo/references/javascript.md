# Checklist JavaScript

Usar como guía de búsqueda; cada punto sigue necesitando escenario de fallo concreto.

- **XSS**: `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write` con datos no confiables (→ `textContent`); `eval` / `new Function`; URLs `javascript:`.
- **Asincronía**: promesas sin `catch`; `fetch` sin comprobar `response.ok`; `await` secuencial en bucles que podrían ir en paralelo; respuestas antiguas que sobrescriben las nuevas (carrera entre peticiones).
- **Correctitud**: `querySelector` que devuelve null sin comprobar; `==` en vez de `===`; `parseInt` sin radix; comparación de floats; mutación de estado compartido; listeners duplicados o nunca eliminados (fugas); `this` perdido en callbacks.
- **Seguridad en cliente**: API keys o secretos en el JS; tokens en `localStorage`; CORS abierto con `*`; peticiones que cambian estado sin protección CSRF; cookies sin `HttpOnly` / `Secure` / `SameSite`; validación solo en cliente.
- **Rendimiento**: leer y escribir el DOM alternando en un bucle; listeners de scroll/resize sin throttle; librerías enteras para una sola función.
