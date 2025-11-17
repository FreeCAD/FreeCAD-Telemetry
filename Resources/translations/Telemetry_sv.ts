<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="sv_SE" sourcelanguage="en_US">
  <context>
    <name>Dialog</name>
    <message>
      <location filename="../panels/first_start.ui" line="14"/>
      <source>Welcome to the Telemetry Addon!</source>
      <translation>Välkommen till tillägget Telemetry!</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="23"/>
      <source>Thank you for installing the Telemetry addon! This addon will send data about each FreeCAD session to a central server. It can be disabled in Preferences, or by removing it entirely.</source>
      <translation>Tack för att du installerar Telemetry-tillägget! Detta tillägg kommer att skicka data om varje FreeCAD-session till en central server. Det kan inaktiveras i inställningarna eller genom att ta bort det helt.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="33"/>
      <source>Enable Telemetry Addon</source>
      <translation>Aktivera Telemetry-tillägget</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="42"/>
      <source>Transmit information about installed Addons</source>
      <translation>Överför information om installerade tillägg</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="45"/>
      <source>Addon list</source>
      <translation>Tilläggslista</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="55"/>
      <source>Transmit basic UI preferences such as theme and overlay settings</source>
      <translation>Överför grundläggande inställningar för användargränssnittet, t.ex. inställningar för tema och överlägg</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="58"/>
      <source>Basic UI preferences</source>
      <translation>Grundläggande inställning för grafiskt gränssnitt</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="68"/>
      <source>Transmit system information like Python version, OS, and screen size</source>
      <translation>Överför systeminformation som Python-version, operativsystem och skärmstorlek</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="71"/>
      <source>System information</source>
      <translation>Systeminformation</translation>
    </message>
  </context>
  <context>
    <name>Gui::Dialog::DlgSettingsTelemetry</name>
    <message>
      <location filename="../panels/preferences.ui" line="14"/>
      <source>General settings</source>
      <translation>Allmänna inställningar</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="20"/>
      <source>Globally enable or disable all telemetry: if disabled, no data is sent</source>
      <translation>Aktivera eller inaktivera all telemetri globalt: om den är inaktiverad skickas inga data</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="23"/>
      <source>Enable telemetry</source>
      <translation>Aktivera telemetri</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="36"/>
      <source>Metrics to send</source>
      <translation>Mätvärden att skicka</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="42"/>
      <source>Allow sending OS, version, and system architecture information</source>
      <translation>Tillåt sändning av information om operativsystem, version och systemarkitektur</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="45"/>
      <source>System information (processor, OS, etc.)</source>
      <translation>Systeminformation (processor, OS, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="58"/>
      <source>Allow sending language, theme, navigation style, and related preferences settings</source>
      <translation>Tillåt inställningar för språk, tema, navigeringsstil och relaterade inställningar för sändning</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="61"/>
      <source>Basic preferences settings (language, theme, etc.)</source>
      <translation>Grundläggande inställningar (språk, tema, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="74"/>
      <source>Allow sending a list of installed Addons</source>
      <translation>Tillåt att skicka en lista över installerade tillägg</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="77"/>
      <source>Addon list</source>
      <translation>Tilläggslista</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="93"/>
      <source>Advanced</source>
      <translation>Avancerat</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="99"/>
      <source>The URL data is sent to. Note that if you change this, the data is no longer sent to the FreeCAD project</source>
      <translation>URL-adressen som data skickas till. Observera att om du ändrar detta skickas inte längre data till FreeCAD-projektet</translation>
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
      <translation>Sentry Data Source Name är den URL som sessions- och kraschdata skickas till. Fyll i det här fältet för att åsidosätta den inbyggda standarden och skicka data någon annanstans än huvudservern FreeCAD Sentry.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="133"/>
      <source>PostHog API Key</source>
      <translation>PostHog API-nyckel</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="148"/>
      <source>Request data removal...</source>
      <translation>Begär borttagning av data...</translation>
    </message>
  </context>
  <context>
    <name>Telemetry</name>
    <message>
      <location filename="../../TelemetryPreferences.py" line="135"/>
      <source>Deletion request response</source>
      <translation>Svar på begäran om radering</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="152"/>
      <source>No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove</source>
      <translation>Ingen UUID hittades i dina FreeCAD Telemetry-inställningar, så det finns inga data att ta bort</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="155"/>
      <source>There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}</source>
      <translation>Det uppstod ett problem med att ta bort dina användardata: kontakta telemetry@freecad.org för att begära borttagning av UUID {}</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="165"/>
      <source>Your user data was successfully removed from the database.</source>
      <translation>Dina användardata har tagits bort från databasen.</translation>
    </message>
  </context>
</TS>
