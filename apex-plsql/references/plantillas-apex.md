# Plantillas APEX, REST y JavaScript

## Versiones (consultado el 1 de octubre de 2026)

Oracle APEX 26.1 se publicó el 14 de mayo de 2026 y está soportado con Oracle Database 19c y con Oracle AI Database 26ai (que sustituye a 23ai). Fuente: [Oracle APEX Downloads](https://www.oracle.com/tools/downloads/apex-downloads.html). Si PJ pregunta por novedades o por una versión concreta, comprueba con una búsqueda en lugar de fiarte de esta nota.

## Validación de página (tipo "Function Body (returning error text)")

```sql
DECLARE
  l_existe NUMBER;
BEGIN
  SELECT COUNT(*)
    INTO l_existe
    FROM usuario
   WHERE email = :P10_EMAIL
     AND id <> NVL(:P10_ID, -1);

  IF l_existe > 0 THEN
    RETURN 'El correo ya está registrado';
  END IF;

  RETURN NULL;
END;
```

## Proceso de página

```sql
BEGIN
  pr_ajustar_saldo(
    p_usuario_id => :P10_ID,
    p_importe    => :P10_IMPORTE
  );
EXCEPTION
  WHEN OTHERS THEN
    apex_debug.error('Error en el proceso de saldo: ' || SQLERRM);
    apex_error.add_error(
      p_message          => 'No se pudo actualizar el saldo.',
      p_display_location => apex_error.c_inline_in_notification
    );
END;
```

Reglas: en SQL de regiones usa binds (`:P10_ID`); no hagas `COMMIT`; los elementos de página se leen con `:P10_X` o `V('P10_X')` y se escriben con `:P10_X := ...` o `apex_util.set_session_state`.

## Ajax Callback (proceso "Ajax Callback") y su llamada desde JavaScript

PL/SQL (proceso a petición con nombre `GUARDAR_NOTA`):

```sql
DECLARE
  l_id   NUMBER        := apex_application.g_x01;
  l_nota VARCHAR2(500) := apex_application.g_x02;
BEGIN
  UPDATE tarea SET nota = l_nota WHERE id = l_id;

  apex_json.open_object;
  apex_json.write('ok', TRUE);
  apex_json.close_object;
EXCEPTION
  WHEN OTHERS THEN
    apex_debug.error('GUARDAR_NOTA: ' || SQLERRM);
    apex_json.open_object;
    apex_json.write('ok', FALSE);
    apex_json.write('mensaje', 'No se pudo guardar la nota');
    apex_json.close_object;
END;
```

JavaScript de la acción dinámica:

```javascript
apex.server.process(
  'GUARDAR_NOTA',
  {
    x01: apex.item('P10_ID').getValue(),
    x02: apex.item('P10_NOTA').getValue()
  },
  {
    success: function (pData) {
      if (pData.ok) {
        apex.message.showPageSuccess('Nota guardada');
      } else {
        apex.message.alert(pData.mensaje);
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      apex.message.alert('Error: ' + errorThrown);
    }
  }
);
```

## Llamada REST con Web Credentials (por ejemplo, la API de Claude)

Preparación en APEX: crea una **Web Credential** (Configuración del espacio de trabajo, Credenciales web) de tipo "HTTP Header" con el nombre de cabecera `x-api-key` y la clave como secreto, con identificador estático `ANTHROPIC_KEY`. La clave no aparece en el código. Si la base de datos no es un servicio gestionado de Oracle, el usuario del esquema necesita una ACL de red para el host de la API (`DBMS_NETWORK_ACL_ADMIN`).

```sql
DECLARE
  c_url      CONSTANT VARCHAR2(200) := 'https://api.anthropic.com/v1/messages';
  l_body     CLOB;
  l_response CLOB;
  l_texto    VARCHAR2(4000);
BEGIN
  -- Sustituye MODEL_ID por el identificador de modelo vigente (consúltalo en la documentación de Anthropic)
  l_body := json_object(
              'model'      VALUE 'MODEL_ID',
              'max_tokens' VALUE 1000,
              'messages'   VALUE json_array(
                                   json_object(
                                     'role'    VALUE 'user',
                                     'content' VALUE :P1_PREGUNTA
                                   ) FORMAT JSON
                                 ) FORMAT JSON
              RETURNING CLOB
            );

  apex_web_service.g_request_headers.DELETE;
  apex_web_service.g_request_headers(1).name  := 'Content-Type';
  apex_web_service.g_request_headers(1).value := 'application/json';
  apex_web_service.g_request_headers(2).name  := 'anthropic-version';
  apex_web_service.g_request_headers(2).value := '2023-06-01';

  l_response := apex_web_service.make_rest_request(
                  p_url                  => c_url,
                  p_http_method          => 'POST',
                  p_body                 => l_body,
                  p_credential_static_id => 'ANTHROPIC_KEY'
                );

  IF apex_web_service.g_status_code <> 200 THEN
    RAISE_APPLICATION_ERROR(-20100, 'Claude API: respuesta HTTP ' || apex_web_service.g_status_code);
  END IF;

  l_texto := JSON_VALUE(l_response, '$.content[0].text');
  :P1_RESPUESTA := l_texto;
END;
```

Notas: para un servicio que se usa en varias páginas, valora una **REST Data Source** de APEX en lugar de código a mano. Comprueba siempre `g_status_code` y no registres el cuerpo con datos sensibles.
