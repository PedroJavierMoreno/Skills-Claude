---
name: test-examenes
description: Usar SIEMPRE que el usuario pida generar un examen, test, simulacro o batería de preguntas para estudiar o practicar para sus asignaturas o certificaciones (ej. CCNA). Aplica tanto si el usuario sube un documento con una batería de preguntas ya hecha como si solo proporciona el temario o apuntes de una asignatura. Define el formato exacto exigido, incluyendo examen interactivo en HTML, bloques de 20 preguntas ampliables a +20, navegación libre entre preguntas, contador de aciertos y fallos acumulativo, feedback con explicación breve, y reglas distintas según el origen del contenido. Consultar este SKILL.md ANTES de generar cualquier examen tipo test, incluso si el usuario no menciona la palabra "skill".
---

# Generador de exámenes tipo test

El usuario pide constantemente exámenes tipo test para practicar para la universidad (UCAM) o certificaciones (ej. CCNA). Esta skill define el formato exacto y fijo que debe tener siempre el examen, para no tener que volver a especificarlo cada vez.

## Paso 0: identificar el modo

Antes de generar nada, determina cuál de los dos modos aplica:

- **MODO BATERÍA**: el usuario ha proporcionado un documento/archivo con preguntas ya redactadas (una batería de preguntas existente).
- **MODO CONTENIDO LIBRE**: el usuario ha proporcionado temario, apuntes o material teórico de una asignatura, sin preguntas ya formuladas.

Si no está claro cuál de los dos es, pregúntalo antes de generar el examen.

## MODO BATERÍA — reglas estrictas

- Las preguntas se extraen **literalmente** de la batería proporcionada: mismo enunciado, mismas opciones, misma respuesta correcta. No parafrasear, no "mejorar" la redacción, no corregir aunque parezca haber un error en el original.
- El formato de presentación (tipo de pregunta: única opción, multi-respuesta, verdadero/falso, etc.) debe respetar el de la batería original.
- Selecciona las preguntas del bloque en orden aleatorio dentro de la batería, no en el orden en que aparecen en el documento.
- Si falla una pregunta: mostrar el indicador de fallo + una explicación breve (1-2 líneas) de por qué la opción correcta es la correcta, aunque la batería original no traiga explicación (en ese caso, generarla tú con tu conocimiento del tema).

## MODO CONTENIDO LIBRE — reglas estrictas

- Las preguntas se generan a partir del temario/material proporcionado. No te salgas de esos contenidos ni añadas información externa no presente en el material.
- Cada pregunta tiene **4 opciones, una sola correcta**.
- **Importante**: la posición de la opción correcta debe variar entre preguntas (A, B, C o D de forma distribuida). Nunca dejes que la correcta caiga sistemáticamente en la misma letra — varíala conscientemente pregunta a pregunta.
- Si falla una pregunta: mostrar el indicador de fallo + explicación breve (1-2 líneas) de por qué la opción correcta es la correcta.

## Estructura del examen (ambos modos)

- **Primer bloque**: 20 preguntas.
- Al terminar las 20, ofrecer botón **"Añadir 20 preguntas más"**, que amplía el mismo examen sin reiniciarlo.
- **Navegación libre**: el usuario puede moverse hacia adelante y hacia atrás entre preguntas ya generadas en cualquier momento (botones "Anterior" / "Siguiente"), no es un flujo solo-hacia-adelante.
- **Repetición espaciada**: al ampliar con +20, las preguntas falladas previamente tienen más probabilidad de volver a aparecer que las acertadas. Esto aplica tanto en modo batería (repitiendo preguntas de la misma batería) como en modo contenido libre (regenerando sobre los mismos puntos del temario que se fallaron).

## Contador de aciertos/fallos

- Visible en todo momento durante el examen.
- **Acumulativo dentro del mismo examen**: si el usuario lleva 17 aciertos y 3 fallos en el primer bloque de 20 y pide ampliar con +20 más, el contador sigue desde 17/3, no se reinicia.
- Se reinicia a 0/0 únicamente cuando se genera un **examen nuevo** (nueva sesión de generación, no una ampliación del actual).

## Feedback por pregunta

- Indicador visual claro de acierto (✅) o fallo (❌) inmediatamente después de responder.
- Si es fallo: resaltar la opción correcta además de la elegida.
- Explicación breve (1-2 líneas, no más) de por qué esa es la respuesta correcta — en ambos modos, batería y contenido libre.

## Implementación técnica

- Generar siempre como **artifact HTML interactivo** (autocontenido, sin dependencias externas más allá de lo permitido en el entorno).
- Diseño limpio y legible, con indicador de progreso (ej. "Pregunta 5 de 20") y el contador de aciertos/fallos siempre visible.
- Nunca mostrar todas las preguntas a la vez como formulario estático: es un flujo interactivo pregunta a pregunta, pero con navegación libre hacia atrás/adelante una vez generadas.
- Nunca revelar la respuesta correcta antes de que el usuario responda esa pregunta.

## Lo que nunca debe hacer

- ❌ Modificar, parafrasear o "corregir" preguntas/opciones en modo batería.
- ❌ Inventar contenido fuera del material proporcionado en modo contenido libre.
- ❌ Dejar la opción correcta siempre en la misma posición en modo contenido libre.
- ❌ Reiniciar el contador de aciertos/fallos al ampliar con +20 dentro del mismo examen.
- ❌ Generar el examen como texto plano o lista estática en vez de artifact interactivo.
