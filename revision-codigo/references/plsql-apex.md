# Checklist PL/SQL, SQL Oracle y APEX

Usar como guía de búsqueda; cada punto sigue necesitando escenario de fallo concreto.

## PL/SQL y SQL
- **SQL dinámico**: `EXECUTE IMMEDIATE`, `DBMS_SQL` u `OPEN FOR` con concatenación de entrada → usar bind variables; identificadores con `DBMS_ASSERT` (`SIMPLE_SQL_NAME`, `ENQUOTE_NAME`).
- **Excepciones**: `WHEN OTHERS THEN NULL`; `WHEN OTHERS` sin log ni re-raise; `SELECT INTO` sin controlar `NO_DATA_FOUND` / `TOO_MANY_ROWS`.
- **Transacciones**: `COMMIT`/`ROLLBACK` dentro de procedimientos reutilizables; `PRAGMA AUTONOMOUS_TRANSACTION` sin justificación; read-modify-write sin `SELECT ... FOR UPDATE`; `MAX(id)+1` en vez de secuencia.
- **Cursores y bucles**: cursores sin cerrar; `FETCH` sin comprobar `%NOTFOUND`; procesamiento fila a fila donde valdría una sola sentencia set-based o `BULK COLLECT` + `FORALL`; `BULK COLLECT` sin `LIMIT` sobre tablas grandes.
- **Tipos y NULL**: `TO_DATE`/`TO_CHAR` sin máscara (depende de NLS); conversiones implícitas; `= NULL` en vez de `IS NULL`; en Oracle `''` es NULL; concatenar con NULL.
- **Rendimiento**: función sobre columna indexada en el `WHERE`; `SELECT *`; consultas dentro de bucles (N+1); FKs sin índice; `COUNT(*)` solo para comprobar existencia.
- **Privilegios**: `AUTHID DEFINER` vs `CURRENT_USER` mal elegido; `GRANT` excesivos; secretos en el código.

## Oracle APEX
- **Salida sin escapar**: `htp.p` o `&ITEM.` en HTML con datos de usuario sin `apex_escape.html`; regiones de contenido dinámico PL/SQL; opciones de escape desactivadas en columnas/regiones.
- **Sustitución vs bind**: `&P1_X.` dentro de una consulta SQL en vez de `:P1_X` (inyección).
- **Autorización**: páginas, procesos, botones y callbacks AJAX sin esquema de autorización; usar `:APP_USER` como único control.
- **Estado de sesión**: Session State Protection desactivada; items ocultos o parámetros de URL tratados como fiables; validación solo en cliente.
- **Configuración**: credenciales en Shared Components o en el código; procesos que modifican datos sin comprobar pertenencia del registro al usuario.
