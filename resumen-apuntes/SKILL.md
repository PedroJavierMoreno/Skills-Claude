---
name: resumen-apuntes
description: Convierte apuntes, temario, diapositivas o PDFs de una asignatura en un resumen estructurado (doc editable) y en fichas de repaso (CSV importable en Anki). Usar SIEMPRE que el usuario comparta o pegue apuntes, un tema, un PDF o diapositivas y pida resumirlos, hacer un resumen, un esquema, fichas, flashcards, tarjetas de Anki, repasar o "preparar el tema", aunque no diga "resumen". NO genera exámenes tipo test (usar test-examenes) ni explica conceptos paso a paso (usar aprende).
---

# Resumen de apuntes y fichas de repaso

Convierte el material de una asignatura en dos cosas: un **resumen estructurado** para estudiar y **fichas de repaso** para memorizar. Por defecto genera ambos; si el usuario pide solo uno, haz solo ese.

## Reglas de fondo

- **Fidelidad.** Usa solo el material del usuario. No inventes datos, fórmulas ni ejemplos. Si añades algo que no está en los apuntes (una definición para completar un hueco, por ejemplo), márcalo como **(añadido)**.
- **Cobertura.** Todo apartado del temario debe aparecer en el resumen. Si algo de los apuntes es ambiguo, está incompleto o parece un error, no lo arregles en silencio: lístalo en "Huecos y dudas".
- **Idioma.** Escribe en español. Si los apuntes están en inglés (por ejemplo, CCNA), conserva el término técnico original entre paréntesis.
- **Fórmulas.** En texto plano legible (por ejemplo, `F = m · a`) y define cada símbolo con sus unidades. El código, los comandos y las consultas SQL van en bloque de código y sin modificar.

## Flujo

### 1. Material y alcance

- Lee el material. Si es un archivo subido cuyo contenido no está en el contexto, usa la skill `file-reading`.
- Averigua lo que falte, **en un solo mensaje**: asignatura, temas incluidos, qué quiere (resumen, fichas o ambos) y si hay examen próximo. Sin respuesta, sigue con estos supuestos: ambos productos, profundidad concisa y todo el material.
- Si el material es largo, trabaja tema por tema sin pedir permiso para cada uno.

### 2. Estructura

Extrae los temas y apartados del material y úsalos como esqueleto. No reorganices el orden de la asignatura salvo que el usuario lo pida.

### 3. Resumen

Entrega un **doc editable** (Claude Doc). Usa las herramientas de Claude Docs y sigue sus instrucciones (si no las tienes en contexto, consulta la guía `topic.instructions` antes de crear el doc). Crea el doc **primero**, con un encabezado por tema y bloques pendientes, y rellénalo tema a tema. Si no hay herramientas de Docs, genera un `.docx` con la skill `docx`.

Estructura:

1. **Lo imprescindible:** las 5 a 10 ideas que no pueden faltar el día del examen.
2. **Por cada tema:** ideas clave, definiciones, fórmulas, comandos o código (según la asignatura), un ejemplo breve del material y errores típicos si el material los menciona.
3. **Huecos y dudas:** lo ambiguo o incompleto detectado en los apuntes.

Extensión por defecto: unas 4 a 6 líneas por concepto, y el resumen entero en torno a una cuarta parte del material. Prosa corta y listas; tablas para comparaciones.

### 4. Fichas

Lee `references/fichas-anki.md` para las reglas de calidad. Genera las fichas en un JSON y créalas con el script:

```bash
python /mnt/skills/user/resumen-apuntes/scripts/crear_csv_anki.py fichas.json /mnt/user-data/outputs/<asignatura>_fichas.csv
```

(Si la skill no está en esa ruta, usa la ruta donde esté instalada.) Revisa los avisos del script. Entrega el CSV con `present_files`.

### 5. Control de calidad

Antes de entregar, comprueba: ningún apartado del temario sin cubrir, ninguna cifra ni fórmula alterada respecto del material, lo añadido marcado como **(añadido)** y fichas sin duplicados.

## Qué NO hacer

- No generar exámenes ni tests: si el usuario quiere practicar, sugiere `test-examenes` al final.
- No explicar los conceptos paso a paso: eso es la skill `aprende`, que solo se usa si el usuario la invoca por su nombre.

## Al terminar

Responde con el enlace al doc y el CSV, sin repetir su contenido. Indica el número de temas y de fichas, y cuántos huecos o dudas detectaste. Si el usuario puede importar el CSV, recuérdale en una línea: Anki, Archivo, Importar.
