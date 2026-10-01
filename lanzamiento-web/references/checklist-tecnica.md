# Checklist técnica

Ítems por bloque. Marca cada uno como OK, Falla o Sin comprobar.

## Dominio, HTTPS y entorno
- El dominio apunta al hosting correcto y el DNS está propagado.
- Certificado SSL válido y redirección de http a https.
- Una única versión canónica (con o sin `www`) con redirección de la otra.
- La web de producción no es una copia de staging ni tiene contenido de prueba (textos tipo lorem ipsum, usuarios de prueba, pedidos de prueba).
- Sin avisos de contenido mixto ni errores en la consola.

## Contenido y funcionamiento
- Todos los enlaces internos funcionan; página 404 personalizada.
- Formularios probados de extremo a extremo y los mensajes llegan al correo correcto.
- Correos del sitio (contacto, pedidos) con SPF, DKIM y DMARC configurados para no caer en spam.
- Favicon, logo y datos de contacto correctos.
- Probado en móvil y en los navegadores principales.

## Rendimiento
- Objetivo de Core Web Vitals en el rango "bueno" de Google: LCP de 2,5 s o menos, INP de 200 ms o menos y CLS de 0,1 o menos. Medir con PageSpeed Insights.
- Imágenes comprimidas, en formato moderno y con dimensiones definidas.
- Caché activa y sin plugins o scripts innecesarios.

## SEO básico
- Una etiqueta `title` y una `meta description` únicas por página, y un único `h1`.
- Sin `noindex` en producción (en WordPress, "Disuadir a los motores de búsqueda" desactivado).
- `robots.txt` y `sitemap.xml` correctos y accesibles.
- Alta en Google Search Console y envío del sitemap.
- Redirecciones 301 si se sustituye una web anterior.
- Etiquetas Open Graph para compartir en redes.

## Accesibilidad
- Navegación completa con teclado y foco visible.
- Contraste de texto suficiente, textos alternativos en imágenes y etiquetas en los campos de formulario.
- Estructura de encabezados coherente. Objetivo: WCAG 2.2 nivel AA.

## Seguridad
- WordPress, tema y plugins actualizados; sin plugins ni temas sin usar.
- Usuario administrador distinto de "admin", contraseña robusta y doble factor si es posible.
- Limitación de intentos de acceso y protección contra spam en formularios.
- Copias de seguridad automáticas activas y **restauración probada**.

## Tienda online (si aplica)
- Pasarelas de pago en **modo real** (no de pruebas) y una compra real de prueba realizada y, si procede, reembolsada.
- Impuestos, envíos y zonas configurados y comprobados con un pedido de ejemplo.
- Correos de confirmación de pedido, cambio de estado y recuperación de contraseña funcionando.
- Stock, variaciones y precios de los productos revisados.
- Proceso de compra completo probado en móvil.

## Entrega al cliente
- Credenciales de WordPress, hosting, dominio y correo traspasadas por un medio seguro.
- El dominio y el hosting están a nombre del cliente (o se ha acordado quién los gestiona).
- Breve guía o sesión de formación sobre cómo editar contenido.
- Confirmación escrita de la entrega y del inicio del periodo de revisiones acordado.
