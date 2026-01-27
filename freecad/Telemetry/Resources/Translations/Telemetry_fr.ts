<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="fr_FR" sourcelanguage="en_US">
  <context>
    <name>Dialog</name>
    <message>
      <location filename="../panels/first_start.ui" line="14"/>
      <source>Welcome to the Telemetry Addon!</source>
      <translation>Bienvenue dans l'extension Telemetry !</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="23"/>
      <source>Thank you for installing the Telemetry addon! This addon will send data about each FreeCAD session to a central server. It can be disabled in Preferences, or by removing it entirely.</source>
      <translation>Merci d'avoir installé l'extension Telemetry ! Cette extension enverra des données à chaque session de FreeCAD à un serveur central. L'extension peut être désactivée dans les préférences ou en la supprimant complètement.</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="33"/>
      <source>Enable Telemetry Addon</source>
      <translation>Activer l'extension Telemetry</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="42"/>
      <source>Transmit information about installed Addons</source>
      <translation>Transmettre des informations sur les extensions installées</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="45"/>
      <source>Addon list</source>
      <translation>Liste des extensions</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="55"/>
      <source>Transmit basic UI preferences such as theme and overlay settings</source>
      <translation>Transmettre les préférences de base de l'interface utilisateur, telles que le thème et les paramètres de superposition</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="58"/>
      <source>Basic UI preferences</source>
      <translation>Préférences de base de l'interface utilisateur</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="68"/>
      <source>Transmit system information like Python version, OS, and screen size</source>
      <translation>Transmettre des informations sur le système, telles que la version de Python, le système d'exploitation et la taille de l'écran</translation>
    </message>
    <message>
      <location filename="../panels/first_start.ui" line="71"/>
      <source>System information</source>
      <translation>Informations sur le système</translation>
    </message>
  </context>
  <context>
    <name>Gui::Dialog::DlgSettingsTelemetry</name>
    <message>
      <location filename="../panels/preferences.ui" line="14"/>
      <source>General settings</source>
      <translation>Réglages généraux</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="20"/>
      <source>Globally enable or disable all telemetry: if disabled, no data is sent</source>
      <translation>Activer ou désactiver toute la télémétrie : si elle est désactivée, aucune donnée ne sera envoyée.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="23"/>
      <source>Enable telemetry</source>
      <translation>Activer la télémétrie</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="36"/>
      <source>Metrics to send</source>
      <translation>Données à envoyer</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="42"/>
      <source>Allow sending OS, version, and system architecture information</source>
      <translation>Permettre l'envoi d'informations sur le système d'exploitation, la version et l'architecture du système</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="45"/>
      <source>System information (processor, OS, etc.)</source>
      <translation>Informations sur le système (processeur, système d'exploitation, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="58"/>
      <source>Allow sending language, theme, navigation style, and related preferences settings</source>
      <translation>Permettre l'envoi de la langue, du thème, du style de navigation et des paramètres de préférences associés</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="61"/>
      <source>Basic preferences settings (language, theme, etc.)</source>
      <translation>Paramètres des préférences de base (langue, thème, etc.)</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="74"/>
      <source>Allow sending a list of installed Addons</source>
      <translation>Permettre l'envoi de la liste des extensions installées</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="77"/>
      <source>Addon list</source>
      <translation>Liste des extensions</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="93"/>
      <source>Advanced</source>
      <translation>Paramètres avancés</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="99"/>
      <source>The URL data is sent to. Note that if you change this, the data is no longer sent to the FreeCAD project</source>
      <translation>L'URL à laquelle les données sont envoyées. Si vous modifiez cette URL, les données ne seront plus envoyées au projet FreeCAD.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="106"/>
      <source>PostHog URL</source>
      <translation>URL PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="113"/>
      <source>Sentry DSN</source>
      <translation>DSN de Sentry</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="120"/>
      <source>Sentry Data Source Name is the URL that session and crash data is sent to. Fill in this field to override the built-in default and send data someplace other than the main FreeCAD Sentry server.</source>
      <translation>Un Data Source Name (DSN) de Sentry est l'URL vers laquelle les données de session et de crash sont envoyées.
Remplissez ce champ pour remplacer la valeur par défaut intégrée et envoyer les données ailleurs que sur le serveur principal Sentry de FreeCAD.</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="133"/>
      <source>PostHog API Key</source>
      <translation>Clé API de PostHog</translation>
    </message>
    <message>
      <location filename="../panels/preferences.ui" line="148"/>
      <source>Request data removal...</source>
      <translation>Arrêter l'envoi des données...</translation>
    </message>
  </context>
  <context>
    <name>Telemetry</name>
    <message>
      <location filename="../../TelemetryPreferences.py" line="135"/>
      <source>Deletion request response</source>
      <translation>Réponse à la demande de l'arrêt</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="152"/>
      <source>No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove</source>
      <translation>Aucun UUID n'a été trouvé dans les paramètres de Telemetry, il n'y a donc pas de données à supprimer.</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="155"/>
      <source>There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}</source>
      <translation>Il y a eu un problème lors de la suppression de vos données d'utilisateur : contacter telemetry@freecad.org pour demander la suppression de l'UUID {}.</translation>
    </message>
    <message>
      <location filename="../../TelemetryPreferences.py" line="165"/>
      <source>Your user data was successfully removed from the database.</source>
      <translation>Vos données d'utilisateur ont été supprimées avec succès de la base de données.</translation>
    </message>
  </context>
</TS>
