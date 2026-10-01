---
name: apex-plsql
description: Genera código Oracle PL/SQL y Oracle APEX con las convenciones de PJ (nombres, formato, manejo de errores y seguridad). Usar SIEMPRE que el usuario pida escribir, crear o completar una función, procedimiento, paquete, trigger, consulta SQL de Oracle, proceso o validación de página APEX, llamada REST desde APEX (APEX_WEB_SERVICE, Web Credentials, integración con la API de Claude) o JavaScript para acciones dinámicas de APEX, o resolver un ejercicio de PL/SQL, aunque no mencione "convenciones" ni "APEX". NO es para revisar código ya escrito (usar revision-codigo) ni para explicar conceptos paso a paso (usar aprende).
---

# Código Oracle PL/SQL y APEX (convenciones de PJ)

Escribe código PL/SQL, SQL y APEX con un estilo consistente. Sirve tanto para ejercicios de la universidad como para proyectos de clientes: comentarios didácticos breves y robustez de producción.

## Flujo

1. **Conoce el esquema.** Usa los nombres reales de tablas y columnas. Si PJ comparte el DDL, un diagrama o capturas, respétalos tal cual (incluidos prefijos como `cr_` en los ejercicios). **Nunca inventes tablas ni columnas**: si faltan, pregunta o declara el supuesto en una línea.
2. **Identifica el contexto:** código en base de datos (función, procedimiento, paquete, trigger), código de página APEX (proceso, validación, región, Ajax Callback), llamada REST o JavaScript de la página.
3. **Escribe el código** con las convenciones de abajo y las plantillas de `references/plantillas-plsql.md` (base de datos) y `references/plantillas-apex.md` (APEX, REST y JavaScript). Léelas antes de escribir.
4. **Autorrevisa** con la lista final y entrega.

## Convenciones

**Nombres.** `l_` variables locales, `p_` parámetros, `c_` constantes, `g_` variables globales de paquete, `e_` excepciones propias, `t_` tipos, `cur_` cursores explícitos. Objetos con prefijo: `fn_` funciones, `pr_` procedimientos, `trg_` triggers, `pkg_` paquetes. En ejercicios de la universidad respeta el esquema y los nombres que da el enunciado. En objetos nuevos usa `snake_case`, sin tildes ni ñ, y el idioma del esquema existente (español si el esquema está en español); un prefijo de tablas solo si el proyecto ya lo usa.

**Formato.** Palabras reservadas en MAYÚSCULAS, identificadores en minúsculas, indentación de 2 espacios, una sentencia por línea. Usa `%TYPE` y `%ROWTYPE` en lugar de tipos fijos.

**Errores.** En código de base de datos, `RAISE_APPLICATION_ERROR` con códigos entre -20000 y -20999 y un mensaje que incluya el nombre del objeto. En procesos y validaciones de página APEX, `apex_error.add_error` o una validación que devuelva el texto del error. Gestiona `NO_DATA_FOUND` y `TOO_MANY_ROWS` en los `SELECT INTO`. Nada de `WHEN OTHERS THEN NULL`: si capturas todo, regístralo con `apex_debug` y vuelve a lanzar o informa.

**Seguridad.** SQL dinámico solo con binds (`USING`) y `DBMS_ASSERT` para nombres de objetos. Las claves de API van en **Web Credentials** de APEX, nunca en el código. No uses `COMMIT` ni `ROLLBACK` dentro de procesos de página (APEX gestiona la transacción) ni dentro de triggers.

**Versiones.** Asume la versión más reciente de APEX y de Oracle Database. Si una función requiere una versión concreta (por ejemplo, `BOOLEAN` en SQL o `IF NOT EXISTS` en DDL, de 23ai en adelante), márcalo con un comentario `-- Requiere 23ai o superior` y da una alternativa compatible con 19c. Si PJ dice qué versión usa, ajústate a ella. Datos de versiones en `references/plantillas-apex.md`.

## Formato de salida

- **Código primero**, en bloques, y después **3 a 5 líneas** con las decisiones clave (por qué esa estructura, qué casos cubre, qué supuestos hiciste).
- **Solo comentarios `--`**, nunca `/* */` (dan problemas en la herramienta de PJ).
- Cada bloque PL/SQL termina con `/` en una línea aparte. **Indica el orden de ejecución** y que cada bloque se ejecuta por separado.
- Añade una **prueba breve** (un bloque anónimo o una consulta) para comprobar que funciona.
- No puedes ejecutar Oracle: no digas que el código está probado. Di qué debe comprobar PJ.

## Lista final

- Nombres y formato según las convenciones y los nombres reales del esquema.
- Excepciones controladas y sin `WHEN OTHERS THEN NULL`.
- Sin credenciales en el código ni SQL dinámico sin binds.
- Sin `COMMIT` en procesos de página ni triggers.
- Comentarios solo con `--`, `/` entre bloques y orden de ejecución indicado.
- Prueba incluida y funciones de versión marcadas.
