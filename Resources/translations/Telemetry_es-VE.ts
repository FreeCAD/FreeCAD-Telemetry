<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="es_VE" sourcelanguage="en_US">
  <context>
    <name>Dialog</name>
    <message>
      <location filename="../panels/first_start.ui" line="14"/>
      <source>Welcome to the Telemetry Addon!</source>
      <translation>¡Bienvenido al complemento Telemetría!</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="23"/>
      <source>Thank you for installing the Telemetry addon! This addon will send data about each FreeCAD session to a central server. It can be disabled in Preferences, or by removing it entirely.</source>
      <translation>¡Gracias por instalar el complemento Telemetría! Este complemento enviará datos sobre cada sesión de FreeCAD a un servidor central. Se puede deshabilitar en Preferencias, o eliminándolo por completo.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="33"/>
      <source>Enable Telemetry Addon</source>
      <translation>Habilitar el complemento Telemetría</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="42"/>
      <source>Transmit information about installed Addons</source>
      <translation>Transmitir información sobre complementos instalados</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="45"/>
      <source>Addon list</source>
      <translation>Lista de complementos</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="55"/>
      <source>Transmit basic UI preferences such as theme and overlay settings</source>
      <translation>Transmitir las preferencias básicas de la interfaz de usuario, como el tema y los ajustes de superposición</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="58"/>
      <source>Basic UI preferences</source>
      <translation>Preferencias de IU básicas</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="68"/>
      <source>Transmit system information like Python version, OS, and screen size</source>
      <translation>Transmitir información del sistema como la versión de Python, el sistema operativo y el tamaño de pantalla</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="71"/>
      <source>System information</source>
      <translation>Información del sistema</translation>
    </message>
  </context>
  <context>
    <name>Gui::Dialog::DlgSettingsTelemetry</name>
    <message>
      <location filename="../panels/preferences.ui" line="14"/>
      <source>General settings</source>
      <translation>Configuración general</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="20"/>
      <source>Globally enable or disable all telemetry: if disabled, no data is sent</source>
      <translation>Habilitar o deshabilitar globalmente toda la telemetría: si es deshabilitada, no se envían datos</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="23"/>
      <source>Enable telemetry</source>
      <translation>Habilitar telemetría</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="36"/>
      <source>Metrics to send</source>
      <translation>Métricas a enviar</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="42"/>
      <source>Allow sending OS, version, and system architecture information</source>
      <translation>Permitir el envío de información sobre el sistema operativo, versión y la arquitectura del sistema</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="45"/>
      <source>System information (processor, OS, etc.)</source>
      <translation>Información del sistema (procesador, SO, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="58"/>
      <source>Allow sending language, theme, navigation style, and related preferences settings</source>
      <translation>Permitir el envío de idioma, tema, estilo de navegación y ajustes de preferencias relacionadas</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="61"/>
      <source>Basic preferences settings (language, theme, etc.)</source>
      <translation>Ajustes de preferencias básicas (idioma, tema, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="74"/>
      <source>Allow sending a list of installed Addons</source>
      <translation>Permitir enviar una lista de los complementos instalados</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="77"/>
      <source>Addon list</source>
      <translation>Lista de complementos</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="93"/>
      <source>Advanced</source>
      <translation>Avanzado</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="99"/>
      <source>The URL data is sent to. Note that if you change this, the data is no longer sent to the FreeCAD project</source>
      <translation>La URL a la cual se envían los datos. Tenga en cuenta que si cambia esto, los datos ya no se envíarán al proyecto FreeCAD</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="106"/>
      <source>PostHog URL</source>
      <translation>URL de PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="113"/>
      <source>Sentry DSN</source>
      <translation>DSN de Sentry</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="120"/>
      <source>Sentry Data Source Name is the URL that session and crash data is sent to. Fill in this field to override the built-in default and send data someplace other than the main FreeCAD Sentry server.</source>
      <translation>El nombre de origen de datos de Sentry es la URL a la que se envía datos de sesión y fallos. Llene este campo para sobreescribir el valor predeterminado y enviar los datos en otro lugar que no sea el servidor Sentry principal de FreeCAD.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="133"/>
      <source>PostHog API Key</source>
      <translation>Clave API de PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="148"/>
      <source>Request data removal...</source>
      <translation>Solicitar eliminación de datos...</translation>
    </message>
  </context>
  <context>
    <name>Telemetry</name>
    <message>
      <location filename="../../TelemetryPreferences.py" line="135"/>
      <source>Deletion request response</source>
      <translation>Respuesta de solicitud de eliminación</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="152"/>
      <source>No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove</source>
      <translation>No se encontró UUID en su configuración de telemetría de FreeCAD, por lo que no hay datos para eliminar</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="155"/>
      <source>There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}</source>
      <translation>Hubo un problema al eliminar sus datos de usuario: comuníquese con telemetry@freecad.org para solicitar la eliminación del UUID {}</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="165"/>
      <source>Your user data was successfully removed from the database.</source>
      <translation>Sus datos de usuario se eliminaron correctamente de la base de datos.</translation>
    </message>
  </context>
</TS>
