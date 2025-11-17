<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="pl_PL" sourcelanguage="en_US">
  <context>
    <name>Dialog</name>
    <message>
      <location filename="../panels/first_start.ui" line="14"/>
      <source>Welcome to the Telemetry Addon!</source>
      <translation>Witamy w dodatku Telemetria!</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="23"/>
      <source>Thank you for installing the Telemetry addon! This addon will send data about each FreeCAD session to a central server. It can be disabled in Preferences, or by removing it entirely.</source>
      <translation>Dziękujemy za zainstalowanie dodatku Telemetria!
Ten dodatek będzie wysyłał dane o każdej sesji FreeCAD do centralnego serwera.
Można go wyłączyć w Preferencjach lub całkowicie usunąć.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="33"/>
      <source>Enable Telemetry Addon</source>
      <translation>Włącz dodatek Telemetrii</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="42"/>
      <source>Transmit information about installed Addons</source>
      <translation>Przesyłaj informacje o zainstalowanych dodatkach</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="45"/>
      <source>Addon list</source>
      <translation>Lista dodatków</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="55"/>
      <source>Transmit basic UI preferences such as theme and overlay settings</source>
      <translation>Przesyłanie podstawowych preferencji interfejsu użytkownika, takich jak ustawienia motywów i nakładek.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="58"/>
      <source>Basic UI preferences</source>
      <translation>Podstawowe ustawienia interfejsu użytkownika</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="68"/>
      <source>Transmit system information like Python version, OS, and screen size</source>
      <translation>Przesyłanie informacji takich jak: wersja Pythona, system operacyjny i rozmiar ekranu.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="71"/>
      <source>System information</source>
      <translation>Informacje o systemie</translation>
    </message>
  </context>
  <context>
    <name>Gui::Dialog::DlgSettingsTelemetry</name>
    <message>
      <location filename="../panels/preferences.ui" line="14"/>
      <source>General settings</source>
      <translation>Ustawienia ogólne</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="20"/>
      <source>Globally enable or disable all telemetry: if disabled, no data is sent</source>
      <translation>Globalnie włącz lub wyłącz wszystkie dane telemetryczne:
jeśli wyłączysz, żadne dane nie będą wysyłane</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="23"/>
      <source>Enable telemetry</source>
      <translation>Włącz telemetrię</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="36"/>
      <source>Metrics to send</source>
      <translation>Dane do wysłania</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="42"/>
      <source>Allow sending OS, version, and system architecture information</source>
      <translation>Zezwalaj na wysyłanie informacji o systemie operacyjnym, jego wersji i architekturze</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="45"/>
      <source>System information (processor, OS, etc.)</source>
      <translation>Informacje o systemie (procesor, system operacyjny itp.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="58"/>
      <source>Allow sending language, theme, navigation style, and related preferences settings</source>
      <translation>Zezwalaj na wysyłanie ustawień języka, motywu, stylu nawigacji i powiązanych preferencji.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="61"/>
      <source>Basic preferences settings (language, theme, etc.)</source>
      <translation>Podstawowe ustawienia preferencji (język, motyw itp.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="74"/>
      <source>Allow sending a list of installed Addons</source>
      <translation>Zezwalaj na wysyłanie listy zainstalowanych dodatków</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="77"/>
      <source>Addon list</source>
      <translation>Lista dodatków</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="93"/>
      <source>Advanced</source>
      <translation>Zaawansowane</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="99"/>
      <source>The URL data is sent to. Note that if you change this, the data is no longer sent to the FreeCAD project</source>
      <translation>Adres URL, na który wysyłane są dane.
Należy pamiętać, że jeśli go zmienisz, informacje nie będą już wysyłane do projektu FreeCAD.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="106"/>
      <source>PostHog URL</source>
      <translation>URL PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="113"/>
      <source>Sentry DSN</source>
      <translation>Sentry DSN</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="120"/>
      <source>Sentry Data Source Name is the URL that session and crash data is sent to. Fill in this field to override the built-in default and send data someplace other than the main FreeCAD Sentry server.</source>
      <translation>Sentry Data Source Name (DSN) to adres URL, na który wysyłane są dane dotyczące sesji i awarii. Wypełnij to pole, aby zastąpić domyślny adres i kierować dane na inny serwer niż główny serwer Sentry FreeCAD.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="133"/>
      <source>PostHog API Key</source>
      <translation>Klucz API PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="148"/>
      <source>Request data removal...</source>
      <translation>Żądanie usunięcia danych …</translation>
    </message>
  </context>
  <context>
    <name>Telemetry</name>
    <message>
      <location filename="../../TelemetryPreferences.py" line="135"/>
      <source>Deletion request response</source>
      <translation>Odpowiedź na żądanie usunięcia</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="152"/>
      <source>No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove</source>
      <translation>Nie znaleziono UUID w ustawieniach Telemetrii FreeCAD, więc nie ma żadnych danych do usunięcia</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="155"/>
      <source>There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}</source>
      <translation>Wystąpił problem z usunięciem danych użytkownika: skontaktuj się na adres telemetry@freecad.org, aby poprosić o usunięcie UUID {}</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="165"/>
      <source>Your user data was successfully removed from the database.</source>
      <translation>Twoje dane użytkownika zostały pomyślnie usunięte z bazy danych.</translation>
    </message>
  </context>
</TS>
