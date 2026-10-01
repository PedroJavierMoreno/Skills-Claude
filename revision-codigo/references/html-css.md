# Checklist HTML/CSS

Usar como guía de búsqueda; cada punto sigue necesitando escenario de fallo concreto.

## Estructura y validez
- Falta `<!DOCTYPE html>`, `lang`, `<meta charset>` o `<title>`; `id` duplicados; etiquetas sin cerrar o mal anidadas; elementos interactivos anidados (`<a>` dentro de `<a>`, `<button>` dentro de `<a>`); jerarquía de encabezados saltada (`h1` → `h4`); `div`/`span` donde hay elemento semántico (`nav`, `main`, `button`, `ul`).

## Formularios
- Inputs sin `<label>` asociado; `type` inadecuado (`text` para email o número); `name` ausente (el campo no se envía); `method="get"` con datos sensibles; `autocomplete` mal usado en contraseñas; `required`/`pattern` como única validación (sin validar en servidor).

## Seguridad
- `<iframe>` sin `sandbox` o de origen no confiable; scripts o CSS externos sin `integrity` (SRI); manejadores `onclick=` inline que impiden una CSP estricta; contenido mixto (recursos `http://` en página `https://`); `target="_blank"` sin `rel="noopener"`.

## Accesibilidad
- `img` sin `alt` (o con `alt` inútil en imágenes informativas); `div` clicable sin rol ni teclado; ARIA mal usado (`role` contradictorio, `aria-hidden` en elementos con foco); contraste insuficiente; foco invisible (`outline: none` sin alternativa); orden de tabulación roto.

## CSS y responsive
- Falta `<meta name="viewport" content="width=device-width, initial-scale=1">`; anchos y altos fijos en px que desbordan en móvil; `!important` como parche; selectores muy específicos o duplicados; `100vh` en móvil sin considerar la barra del navegador; texto que no escala (`font-size` en px fijo con contenedores de altura fija).

## Rendimiento
- Imágenes sin `width`/`height` (saltos de layout) ni `loading="lazy"` bajo el pliegue; imágenes más grandes de lo que se muestra; scripts bloqueantes en el `<head>` sin `defer`/`async`; CSS sin usar.
