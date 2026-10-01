---
name: ingenieria
description: Flujos de ingeniería para un desarrollador web freelance y estudiante - documentación técnica, informes de incidencias y registro de decisiones de arquitectura. SOLO se activa cuando el usuario la invoca explícitamente por su nombre ("ingenieria", "/ingenieria", "usa la skill ingenieria", "modo ingenieria"). NO activar por iniciativa propia ni por coincidencia con peticiones de documentar, revisar código o diagnosticar si el usuario no ha nombrado la skill.
---

# Ingeniería

Tres flujos para trabajo técnico real: documentar, gestionar incidencias y registrar decisiones. Está pensada para proyectos web de clientes, aplicaciones Oracle APEX / PL/SQL y trabajos de la universidad.

## Activación

Usar solo cuando el usuario nombre la skill. Después de invocarla, elegir el flujo según lo que pida. Si no queda claro, preguntar cuál de los tres quiere.

No cubre la revisión de código: para eso existe la skill `revision-codigo`. Si el usuario pide revisar código dentro de este flujo, derivar a esa skill.

## Principios comunes

- Escribir para quien lo va a leer. Un cliente no técnico necesita saber qué pasó y qué hacer; otro desarrollador necesita detalles y comandos.
- Partir de datos reales que aporte el usuario. No inventar versiones, rutas, credenciales, causas ni fechas: si falta algo, dejar un marcador `[PENDIENTE: ...]` en lugar de rellenarlo.
- Nunca incluir contraseñas, tokens ni claves en la documentación; poner un marcador y explicar dónde se guardan.
- Ser breve. Un documento corto y usado vale más que uno largo que nadie lee.
- Responder en el idioma del usuario.

## Flujo 1: Documentación técnica

Sirve para README, documentación de entrega a clientes, manuales de una app APEX y memorias de trabajos.

1. Preguntar solo lo imprescindible: qué es el proyecto y quién leerá el documento.
2. Elegir la estructura según el destinatario:
   - **Desarrollador (README):** qué hace, requisitos, instalación, configuración, estructura del proyecto, cómo desplegar, problemas conocidos.
   - **Cliente (entrega):** qué se ha hecho, cómo se usa en el día a día, qué mantenimiento necesita, a quién avisar si falla, qué accesos existen (sin datos secretos).
3. Incluir comandos y ejemplos copiables y probados en lo que el usuario haya compartido.
4. Cerrar con una lista de lo que quedó marcado como pendiente.

## Flujo 2: Incidencias

Sirve cuando una web o app de un cliente falla, y para el informe posterior.

**Durante la incidencia (diagnóstico):**
1. Concretar síntoma, desde cuándo, qué cambió justo antes (despliegue, actualización, caducidad de certificado o dominio, cuota de hosting).
2. Proponer comprobaciones en orden de menor a mayor coste: estado del servidor y DNS, certificado SSL, logs de errores, base de datos, últimos cambios de código.
3. Distinguir entre **mitigar** (que vuelva a funcionar ya) y **corregir la causa**. Mitigar primero si el cliente está afectado.
4. No afirmar la causa hasta que un dato la respalde; presentar hipótesis como hipótesis.

**Después (informe):**
- Resumen en 2-3 frases para el cliente, sin jerga.
- Cronología: cuándo empezó, cuándo se detectó, cuándo se resolvió.
- Causa (o causa probable, si no está confirmada) y qué se hizo.
- Qué se cambia para que no se repita.
- Tono sereno y sin culpar a nadie.

## Flujo 3: Decisiones de arquitectura

Sirve para dejar por escrito por qué se eligió una tecnología o diseño.

Usar este formato:

```
# Decisión: [título corto]
Fecha: [fecha]
Estado: propuesta | aceptada | sustituida

## Contexto
[Qué problema hay y qué restricciones existen: plazo, presupuesto, hosting, nivel del cliente]

## Opciones consideradas
1. [Opción A]: ventajas / inconvenientes
2. [Opción B]: ventajas / inconvenientes

## Decisión
[Qué se elige y por qué]

## Consecuencias
[Qué se gana, qué se asume, cuándo habría que revisarla]
```

Comparar al menos dos opciones reales. Si el usuario ya decidió, documentar su decisión sin cuestionarla, pero indicar con claridad los inconvenientes si los hay.
