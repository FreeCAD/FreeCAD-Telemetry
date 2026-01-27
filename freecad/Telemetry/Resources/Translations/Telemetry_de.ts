<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="de_DE" sourcelanguage="en_US">
  <context>
    <name>Dialog</name>
    <message>
      <location filename="../panels/first_start.ui" line="14"/>
      <source>Welcome to the Telemetry Addon!</source>
      <translation>Willkommen beim Telemetry-Addon!</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="23"/>
      <source>Thank you for installing the Telemetry addon! This addon will send data about each FreeCAD session to a central server. It can be disabled in Preferences, or by removing it entirely.</source>
      <translation>Danke für das Installieren des Telemetry-Addons! Dieses Addon sendet Daten zu jeder FreeCAD-Sitzung zu einem zentralen Server. Es kann entweder in den Voreinstellungen deaktiviert oder komplett gelöscht werden.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="33"/>
      <source>Enable Telemetry Addon</source>
      <translation>Telemetry-Addon aktivieren</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="42"/>
      <source>Transmit information about installed Addons</source>
      <translation>Informationen zu installierten Addons senden</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="45"/>
      <source>Addon list</source>
      <translation>Addon-Liste</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="55"/>
      <source>Transmit basic UI preferences such as theme and overlay settings</source>
      <translation>Grundlegende UI-Einstellungen, wie Theme- und Overlay-Einstellungen, senden</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="58"/>
      <source>Basic UI preferences</source>
      <translation>Grundlegende UI-Einstellungen</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="68"/>
      <source>Transmit system information like Python version, OS, and screen size</source>
      <translation>Systeminformationen, wie Python-Version und Bildschirmgröße, senden</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="71"/>
      <source>System information</source>
      <translation>Systeminformationen</translation>
    </message>
  </context>
  <context>
    <name>Gui::Dialog::DlgSettingsTelemetry</name>
    <message>
      <location filename="../panels/preferences.ui" line="14"/>
      <source>General settings</source>
      <translation>Allgemeine Einstellungen</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="20"/>
      <source>Globally enable or disable all telemetry: if disabled, no data is sent</source>
      <translation>Aktiviert bzw. deaktiviert global alle Telemetriefunktionen: Wenn deaktiviert, werden keine Daten gesendet</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="23"/>
      <source>Enable telemetry</source>
      <translation>Telemetrie aktivieren</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="36"/>
      <source>Metrics to send</source>
      <translation>Zu sendende Daten</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="42"/>
      <source>Allow sending OS, version, and system architecture information</source>
      <translation>Erlaubt das Senden von Betriebssystem, Version und System-Architektur-Informationen</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="45"/>
      <source>System information (processor, OS, etc.)</source>
      <translation>System-Informtionen (Prozessor, Betriebssystem, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="58"/>
      <source>Allow sending language, theme, navigation style, and related preferences settings</source>
      <translation>Erlaubt das Senden der Sprache, des Theme, Navigations-Stils und zugehöriger Einstellungen</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="61"/>
      <source>Basic preferences settings (language, theme, etc.)</source>
      <translation>Basis-Einstellungen (Sprache, Theme, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="74"/>
      <source>Allow sending a list of installed Addons</source>
      <translation>Erlaubt das Senden einer Liste der installierten Addons</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="77"/>
      <source>Addon list</source>
      <translation>Addon-Liste</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="93"/>
      <source>Advanced</source>
      <translation>Erweitert</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="99"/>
      <source>The URL data is sent to. Note that if you change this, the data is no longer sent to the FreeCAD project</source>
      <translation>Die URL-Daten werden ebenfalls gesendet. Beachte, dass bei Änderung dieser Einstellung, die Daten nicht mehr an das FreeCAD-Projekt gesendet werden</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="106"/>
      <source>PostHog URL</source>
      <translation>PostHog URL</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="113"/>
      <source>Sentry DSN</source>
      <translation>Sentry DSN</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="120"/>
      <source>Sentry Data Source Name is the URL that session and crash data is sent to. Fill in this field to override the built-in default and send data someplace other than the main FreeCAD Sentry server.</source>
      <translation>Der Name der Sentry-Datenquelle ist die URL, an die Sitzungs- und Absturzdaten gesendet werden. Fülle dieses Feld aus, um die integrierte Standardeinstellung zu überschreiben und Daten an einen anderen Ort als den Hauptserver von FreeCAD Sentry zu senden.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="133"/>
      <source>PostHog API Key</source>
      <translation>PostHog API-Schlüssel</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="148"/>
      <source>Request data removal...</source>
      <translation>Datenlöschung beantragen...</translation>
    </message>
  </context>
  <context>
    <name>Telemetry</name>
    <message>
      <location filename="../../TelemetryPreferences.py" line="135"/>
      <source>Deletion request response</source>
      <translation>Antwort zur Löschanfrage</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="152"/>
      <source>No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove</source>
      <translation>Es wurde keine UUID in FreeCADs Telemetrie-Einstellungen gefunden, daher gibt es keine Daten zum Entfernen</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="155"/>
      <source>There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}</source>
      <translation>Es gab ein Problem beim Entfernen Deiner Benutzerdaten: Bitte kontaktiere telemetry@freecad.org um das Entfernen von UUID {} zu beantragen</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="165"/>
      <source>Your user data was successfully removed from the database.</source>
      <translation>Dein Benutzer wurde erfolgreich aus der Datenbank entfernt.</translation>
    </message>
  </context>
</TS>
