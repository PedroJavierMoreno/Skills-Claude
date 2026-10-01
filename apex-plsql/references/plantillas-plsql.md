# Plantillas PL/SQL (base de datos)

Nombres de tablas y columnas de ejemplo: sustitúyelos por los del esquema real.

## Función

```sql
CREATE OR REPLACE FUNCTION fn_obtener_saldo (
  p_usuario_id IN usuario.id%TYPE
) RETURN usuario.saldo%TYPE
IS
  l_saldo usuario.saldo%TYPE;
BEGIN
  SELECT u.saldo
    INTO l_saldo
    FROM usuario u
   WHERE u.id = p_usuario_id;

  RETURN l_saldo;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    RAISE_APPLICATION_ERROR(-20001, 'fn_obtener_saldo: no existe el usuario ' || p_usuario_id);
  WHEN TOO_MANY_ROWS THEN
    RAISE_APPLICATION_ERROR(-20002, 'fn_obtener_saldo: hay más de un usuario con el id ' || p_usuario_id);
END fn_obtener_saldo;
/
```

## Procedimiento con validación

```sql
CREATE OR REPLACE PROCEDURE pr_ajustar_saldo (
  p_usuario_id IN usuario.id%TYPE,
  p_importe    IN NUMBER
)
IS
BEGIN
  IF p_importe IS NULL OR p_importe = 0 THEN
    RAISE_APPLICATION_ERROR(-20010, 'pr_ajustar_saldo: el importe no puede ser nulo ni cero');
  END IF;

  UPDATE usuario
     SET saldo = saldo + p_importe
   WHERE id = p_usuario_id;

  IF SQL%ROWCOUNT = 0 THEN
    RAISE_APPLICATION_ERROR(-20011, 'pr_ajustar_saldo: no existe el usuario ' || p_usuario_id);
  END IF;
END pr_ajustar_saldo;
/
```

## Trigger

```sql
CREATE OR REPLACE TRIGGER trg_transaccion_bi
BEFORE INSERT ON transaccion
FOR EACH ROW
BEGIN
  IF :NEW.importe <= 0 THEN
    RAISE_APPLICATION_ERROR(-20020, 'trg_transaccion_bi: el importe debe ser positivo');
  END IF;
END trg_transaccion_bi;
/
```

Reglas: no hagas `COMMIT` dentro del trigger; para evitar el error de tabla mutante no consultes la propia tabla del trigger en un trigger de fila (usa un trigger compuesto si hace falta). Nombre: `trg_<tabla>_<momento><evento>` (`bi` = before insert, `au` = after update).

## Paquete

```sql
CREATE OR REPLACE PACKAGE pkg_usuario IS
  FUNCTION  fn_obtener_saldo (p_usuario_id IN usuario.id%TYPE) RETURN usuario.saldo%TYPE;
  PROCEDURE pr_ajustar_saldo (p_usuario_id IN usuario.id%TYPE, p_importe IN NUMBER);
END pkg_usuario;
/

CREATE OR REPLACE PACKAGE BODY pkg_usuario IS
  FUNCTION fn_obtener_saldo (p_usuario_id IN usuario.id%TYPE) RETURN usuario.saldo%TYPE IS
    l_saldo usuario.saldo%TYPE;
  BEGIN
    SELECT saldo INTO l_saldo FROM usuario WHERE id = p_usuario_id;
    RETURN l_saldo;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      RAISE_APPLICATION_ERROR(-20001, 'pkg_usuario.fn_obtener_saldo: no existe el usuario ' || p_usuario_id);
  END fn_obtener_saldo;

  PROCEDURE pr_ajustar_saldo (p_usuario_id IN usuario.id%TYPE, p_importe IN NUMBER) IS
  BEGIN
    UPDATE usuario SET saldo = saldo + p_importe WHERE id = p_usuario_id;
    IF SQL%ROWCOUNT = 0 THEN
      RAISE_APPLICATION_ERROR(-20011, 'pkg_usuario.pr_ajustar_saldo: no existe el usuario ' || p_usuario_id);
    END IF;
  END pr_ajustar_saldo;
END pkg_usuario;
/
```

## Cursor explícito con bucle

```sql
DECLARE
  CURSOR cur_ranking IS
    SELECT u.id,
           u.nombre,
           SUM(CASE WHEN t.tipo = 'VENTA' THEN t.importe ELSE -t.importe END) AS beneficio
      FROM usuario u
      JOIN transaccion t ON t.usuario_id = u.id
     GROUP BY u.id, u.nombre
     ORDER BY beneficio DESC;
BEGIN
  FOR r IN cur_ranking LOOP
    DBMS_OUTPUT.PUT_LINE(r.nombre || ': ' || r.beneficio);
  END LOOP;
END;
/
```

## SQL dinámico seguro

```sql
DECLARE
  l_tabla  VARCHAR2(128) := DBMS_ASSERT.SQL_OBJECT_NAME('usuario');
  l_total  NUMBER;
BEGIN
  EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || l_tabla || ' WHERE estado = :1'
    INTO l_total
    USING 'ACTIVO';
END;
/
```
