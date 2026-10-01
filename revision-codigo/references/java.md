# Checklist Java

Usar como guía de búsqueda; cada punto sigue necesitando escenario de fallo concreto.

## Nulos e igualdad
- `NullPointerException` por retorno null no documentado, unboxing de `Integer` null o `Optional.get()` sin comprobar; devolver null en vez de colección vacía.
- `==` con `String`, `Integer` u objetos en vez de `equals`; `equals` sin `hashCode` (o al revés); campos mutables en `hashCode` de objetos usados como clave de `HashMap`/`HashSet`; `compareTo` incoherente con `equals`.

## Recursos y excepciones
- `Scanner`, streams, conexiones o `PreparedStatement` sin cerrar → `try-with-resources`.
- `catch (Exception e) {}` vacío o solo `printStackTrace`; capturas demasiado amplias; relanzar perdiendo la causa; `return` dentro de `finally`.

## POO y diseño
- Getters que devuelven colecciones o arrays internos sin copia defensiva (rompen el encapsulamiento); atributos públicos mutables.
- Métodos sobrescritos sin `@Override`; llamar a métodos sobrescribibles desde el constructor; herencia para reutilizar código donde encaja mejor la composición; subclases que rompen el contrato de la clase padre (Liskov).
- Estado estático mutable compartido; clases con demasiadas responsabilidades.
- Tipos crudos (`List` sin genéricos) y casts sin comprobar.

## Colecciones y concurrencia
- `ConcurrentModificationException` al modificar una colección mientras se itera; `HashMap`/`ArrayList` compartidos entre hilos; `SimpleDateFormat` compartido; check-then-act sin sincronizar; `synchronized` aplicado de forma inconsistente; double-checked locking sin `volatile`; `ExecutorService` sin `shutdown`.

## Numéricos
- División entera donde se esperaba decimal; desbordamiento de `int`; `Math.abs(Integer.MIN_VALUE)`; `double`/`float` para dinero (→ `BigDecimal`); `BigDecimal.equals` vs `compareTo` (escala distinta).

## Rendimiento
- Concatenación con `+` en bucles (→ `StringBuilder`); regex compilada dentro de bucles; autoboxing en bucles calientes; consultas dentro de bucles (N+1) en JDBC/JPA.

## Seguridad
- SQL construido con `Statement` y concatenación (→ `PreparedStatement`); deserialización de objetos no confiables; `Random` para tokens o contraseñas (→ `SecureRandom`); rutas de archivo con entrada de usuario (path traversal); contraseñas en `String` o en logs.
