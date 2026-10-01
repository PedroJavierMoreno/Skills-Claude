# Fichas de repaso (Anki)

## Calidad de las fichas

- **Una idea por ficha.** Si el reverso necesita más de 5 líneas, divide la ficha.
- **El anverso se entiende solo,** sin depender de la ficha anterior ni del contexto del tema. Incluye el contexto mínimo: "En Estadística, ¿qué mide la desviación típica?".
- **Preguntas que obliguen a recordar,** no de sí o no. Prefiere "¿Qué diferencia hay entre X e Y?" a "¿X es distinto de Y?".
- **Variedad:** definiciones, diferencias, causas y consecuencias, fórmulas ("¿Cuál es la fórmula de X y qué significa cada símbolo?"), y en asignaturas técnicas comandos, sintaxis y casos de uso ("¿Qué comando muestra la tabla de rutas?").
- **Código y comandos:** en el reverso, tal cual aparecen en el material y con saltos de línea si hacen falta.
- **Cantidad:** unas 15 a 30 fichas por tema, según su densidad. No rellenes con detalles irrelevantes; prioriza lo que el material destaca.
- **Idioma:** el del resumen (español); si los apuntes están en inglés, el término original va entre paréntesis.

## Etiquetas

Tercera columna: `asignatura::tema`, sin espacios (el script los cambia por `_`). Ejemplo: `redes::vlan`.

## Formato del JSON

```json
[
  {
    "front": "En redes, ¿qué es una VLAN?",
    "back": "Segmento lógico de una red que separa dominios de broadcast sin cambiar el cableado físico.",
    "tags": "redes::vlan"
  }
]
```

## Importar en Anki

Archivo, Importar y elegir el CSV. Las tres primeras líneas del archivo son directivas que Anki lee (separador coma, sin HTML y etiquetas en la columna 3). El tipo de nota es "Básico" (anverso y reverso). Si usas una versión de Anki muy antigua que ignore esas directivas, indica manualmente el separador coma y la columna de etiquetas.
