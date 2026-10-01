---
name: "revision-codigo"
description: Usar siempre que el usuario pida revisar, auditar, analizar o "mirar" código en busca de bugs, fallos de seguridad, mala legibilidad o problemas de rendimiento — un archivo, código pegado, un diff, un PR o una carpeta — en cualquier lenguaje (PL/SQL, Oracle APEX, SQL, JavaScript, HTML/CSS, Python, etc.). Activar también con frases como "code review", "revisa esto", "mira si hay errores", "es seguro este código", "qué falla aquí" o "audita mi PR", aunque no digan "revisión". No usar para escribir código nuevo, refactorizar sin revisión previa ni depurar un error ya identificado.
---

# Revisión de código

Objetivo: un informe de hallazgos reales, verificados y ordenados por severidad. No una lista de opiniones de estilo.

## 1. Alcance y lectura

- Código pegado o archivo adjunto: leerlo entero antes de opinar (qué hace, qué datos maneja, quién lo llama). Un hallazgo sin entender el flujo real es un falso positivo.
- Diff o PR: leer el diff y también el archivo completo alrededor; una línea cambiada puede romper algo que no aparece en el diff.
- Petición vaga («revisa mi proyecto»): preguntar qué archivos o carpeta antes de analizar todo el repo.
- Alcance grande: priorizar por este orden: entrada de datos externos (formularios, parámetros, APIs), código que toca base de datos, autenticación/autorización, datos personales o dinero. Indicar qué se revisó y qué no.
- Según el stack, leer solo la referencia que aplique: C → `references/c.md`; Java → `references/java.md`; HTML/CSS → `references/html-css.md`; JavaScript → `references/javascript.md`; PL/SQL, SQL Oracle o APEX → `references/plsql-apex.md`. Para otros lenguajes, aplicar las cuatro dimensiones de abajo.

## 2. Qué buscar (por orden de importancia)

**Bugs y correctitud**: errores lógicos, casos borde (listas vacías, null/undefined, división por cero), condiciones de carrera, off-by-one, manejo de errores ausente o incorrecto, estados inconsistentes.

**Seguridad**: inyección (SQL dinámico sin bind variables, comandos), XSS/CSRF, validación de entrada ausente, secretos hardcodeados, control de acceso incorrecto, datos sensibles en logs o respuestas.

**Rendimiento**: consultas ineficientes (sin índices, N+1, SELECT * innecesario), bucles con complejidad evitable, trabajo repetido cacheable.

**Legibilidad y mantenibilidad**: nombres confusos, lógica duplicada, funciones con demasiadas responsabilidades, código muerto, números o strings mágicos.

## 3. Verificar antes de reportar

Un hallazgo solo cuenta si se puede describir un escenario de fallo concreto: «con esta entrada / en este estado, pasa esto». Si hay entorno de ejecución y el código se puede correr, confirmarlo ejecutando el caso o pasando un linter en vez de solo razonarlo.

- Sin escenario trazable: es una sospecha. Va a «Dudas por confirmar», nunca mezclada con los confirmados.
- Una preferencia de estilo distinta a la del autor no es un hallazgo.
- Un mismo patrón repetido en varias líneas es un único hallazgo que referencia todas las líneas.

## 4. Severidad

- **Crítico**: pérdida o corrupción de datos, inyección o ejecución explotable, acceso sin autorización, credenciales expuestas.
- **Alto**: fallo probable en uso normal, o vulnerabilidad explotable con condiciones plausibles.
- **Medio**: fallo en casos borde realistas o degradación de rendimiento notable.
- **Bajo**: mantenibilidad con coste real (duplicación que ya causa inconsistencias, código muerto engañoso). La legibilidad pura rara vez pasa de Bajo.

## 5. Formato de salida

Empezar con una línea de resumen: alcance revisado y número de hallazgos por severidad. Después, hallazgos de más a menos grave, nunca en orden de aparición en el archivo. Cada hallazgo incluye: archivo y línea, qué falla, escenario concreto que lo demuestra y corrección propuesta (una o dos líneas, o un snippet mínimo).

Si la herramienta `ReportFindings` está disponible, usarla con los hallazgos ya verificados (más grave primero; array vacío si ninguno sobrevive), rellenando file, line, summary, failure_scenario, category y short_summary. Poner la corrección propuesta al final de `summary`. Las dudas van en el texto de la respuesta, no en la herramienta.

Si no está disponible, entregar un informe en markdown agrupado por Crítico / Alto / Medio / Bajo, cada hallazgo como un párrafo corto (sin viñetas por frase). Cerrar con «Dudas por confirmar», una línea por duda, solo si existen.

Si no hay ningún problema real, decirlo en una frase. No inventar hallazgos menores para rellenar.

## 6. Tono

Directo y técnico, en el idioma del usuario. Sin suavizar lo grave ni alarmismo en lo menor: que sepa qué arreglar primero.
