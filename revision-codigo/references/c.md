# Checklist C

Usar como guía de búsqueda; cada punto sigue necesitando escenario de fallo concreto. Si hay entorno de ejecución, verificar compilando con `gcc -Wall -Wextra -g -fsanitize=address,undefined` (o `valgrind`) antes de afirmar un fallo de memoria.

## Memoria
- **Desbordamiento de buffer**: `gets`, `strcpy`, `strcat`, `sprintf`, `scanf("%s")` sin ancho → `fgets`, `snprintf`, `strncat`, `%Ns`. Off-by-one por olvidar el byte del `'\0'`.
- **malloc/realloc**: resultado sin comprobar contra NULL; `sizeof(puntero)` en vez de `sizeof(*puntero)` o del tipo; `n * size` que desborda; `p = realloc(p, ...)` (si falla, se pierde el original y se filtra memoria).
- **Ciclo de vida**: use-after-free; double free; `free` de memoria no dinámica; fugas en las rutas de error (return anticipado sin liberar); devolver puntero a variable local; memoria sin inicializar.
- **Límites**: índices fuera de rango o negativos; bucles con `<=` en vez de `<`; aritmética de punteros sin comprobar límites.

## Enteros y tipos
- Desbordamiento de enteros con signo (comportamiento indefinido); mezcla signed/unsigned en comparaciones; resta con `size_t` que da la vuelta; truncamiento al convertir a tipos más pequeños; división por cero; desplazamientos mayores que el ancho del tipo.
- Comparar floats con `==`; guardar el retorno de `getchar`/`fgetc` en `char` en vez de `int` (rompe la detección de EOF).

## Cadenas y E/S
- Cadenas sin terminador; `strlen` en la condición de un bucle (O(n²)); `fgets` deja el `'\n'`; retorno de `scanf`/`fscanf` sin comprobar; `fopen` sin comprobar NULL; `fclose` que falta; formato de `printf` controlado por el usuario (format string).
- Comparar cadenas con `==` en vez de `strcmp`.

## Correctitud
- `=` en vez de `==` dentro de condiciones; `;` tras `if`/`for`/`while`; `switch` sin `break` no intencionado; variables sin inicializar; macros sin paréntesis o con doble evaluación de argumentos; comportamiento indefinido en general.

## Seguridad y concurrencia
- `system()`/`popen()` con entrada de usuario; `rand()` para fines de seguridad; TOCTOU en archivos (`access` y luego `open`); acceso a datos compartidos entre hilos sin mutex.
