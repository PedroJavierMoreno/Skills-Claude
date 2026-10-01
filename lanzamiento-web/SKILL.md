---
name: lanzamiento-web
description: Genera y, si hay URL, ejecuta la checklist de publicación de una web antes de lanzarla o entregarla al cliente (técnico, rendimiento, SEO básico, accesibilidad, seguridad y requisitos legales en España como RGPD, cookies y LSSI, más derecho de desistimiento si es tienda). Usar SIEMPRE que el usuario diga que va a publicar, lanzar, entregar, pasar a producción o dar de alta una web, tienda online o landing, o pida una revisión final, checklist de lanzamiento, "go-live" o preguntas del tipo "¿está lista para salir?", "¿qué me falta antes de entregarla?", aunque no mencione la palabra checklist. NO escribe textos legales completos ni cubre el mantenimiento posterior.
---

# Lanzamiento web (checklist previa a publicar)

Revisa que una web esté lista para salir y entregarse al cliente. El resultado es un **doc editable con una checklist** que PJ puede ir marcando, con un veredicto claro de qué bloquea el lanzamiento.

## Qué NO hacer

- No redactar los textos legales completos (aviso legal, privacidad, cookies, condiciones de venta): se comprueba que existen y que contienen lo necesario. Si faltan, recomienda un generador legal o un profesional.
- No presupuestar ni planificar mantenimiento (va en otra skill).
- No dar asesoramiento legal: señala lo que exige la normativa y recomienda confirmarlo con un gestor o abogado en los casos dudosos.
- No marcar como correcto lo que no se ha comprobado.

## Flujo

### 1. Contexto

Averigua, preguntando **en un solo mensaje** solo lo que falte:

- Tipo de web: informativa, landing, tienda online u otra (app, reservas, área de clientes).
- Tecnología (WordPress, WooCommerce, código propio, otra).
- URL de producción y, si existe, de staging o de pruebas.
- Quién gestiona dominio, hosting y correo (el cliente o PJ).
- Si recoge datos personales (formularios, registros, newsletter) y qué herramientas de analítica o publicidad usa.

Sin respuesta, continúa con supuestos declarados.

### 2. Comprobar lo que se pueda

Si hay una URL accesible, comprueba lo automatizable con `web_fetch` o, si está disponible, con las herramientas de navegador (HTTPS y redirecciones, `robots.txt`, `sitemap.xml`, títulos y metaetiquetas, etiqueta `noindex`, enlaces a textos legales, banner de cookies). Usa `references/checklist-tecnica.md` como lista de ítems.

Cada ítem lleva un estado: **OK**, **Falla** o **Sin comprobar** (requiere revisión manual de PJ). No des por bueno nada que no hayas visto. Si no hay URL o no se puede acceder, todo queda como **Sin comprobar** y la checklist funciona como guía manual.

### 3. Requisitos legales

Lee `references/legal-espana.md`. Contiene los requisitos y las fechas de aplicación, pero **antes de usarlo comprueba con una búsqueda** los puntos sujetos a cambio (en especial el estado en España del botón de desistimiento) y actualiza lo que haya cambiado. Cita las fuentes en el doc. Aplica solo lo que corresponda al tipo de web (los requisitos de tienda solo si hay ventas).

### 4. Clasificar

Agrupa lo pendiente en tres niveles:

- **Bloquea el lanzamiento:** fallos que no se deben publicar (sin HTTPS, sitio con `noindex` activo si debe indexarse, sin textos legales o banner de cookies conforme, pagos en modo de pruebas, formularios que no llegan, sin copias de seguridad).
- **Importante:** conviene corregirlo en los primeros días.
- **Mejora:** opcional.

## Formato de salida

Entrega un **doc editable** (Claude Doc). Usa las herramientas de Claude Docs y sigue sus instrucciones (si no las tienes en contexto, consulta la guía `topic.instructions` antes de crear el doc). Crea el doc **primero**, con el esquema, y rellénalo sección a sección; el veredicto va al final, cuando ya está todo revisado. Si no hay herramientas de Docs, genera un `.docx` con la skill `docx`.

Estructura:

1. **Título** con el nombre de la web y la fecha.
2. **Veredicto:** listo, listo con reservas o no listo, con el número de bloqueantes.
3. **Bloquea el lanzamiento:** lista de tareas (`- [ ]`) con qué falla y cómo arreglarlo.
4. **Importante** y **Mejoras:** listas de tareas.
5. **Checklist completa** por bloque (técnico, rendimiento, SEO, accesibilidad, seguridad, legal, tienda si aplica, entrega), con tareas marcables y el estado de cada ítem.
6. **Fuentes** de los puntos legales, con la fecha de consulta.

Mantén el doc breve y práctico, en español y con tono directo.

## Al terminar

Responde con una línea y el enlace al doc. Indica cuántos bloqueantes hay y qué no se pudo comprobar.
