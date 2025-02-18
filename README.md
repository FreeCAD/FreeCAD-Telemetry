# FreeCAD Telemetry Addon

This addon sends select FreeCAD usage information to a centralized database.

# How does telemetry help the FreeCAD project?

FreeCAD developers are often faced with competing priorities: for example, which bugs to prioritize fixing. One
way of making decisions is to estimate how many people are affected by a given bug, or are running an Addon that
may be affected by an API change, etc. In order to better focus limited resources, we want to gather a picture
of how FreeCAD is being used.

# What data is sent?

When installed, every time you run FreeCAD, the current version of FreeCAD is sent to our telemetry server
(current using the PostHog service). This is also transmitted when FreeCAD shuts down correctly (e.g. without a
crash) to enable us to gather aggregate crash statistics about each version of FreeCAD.

In addition, three other categories of information are usually sent, but can be disabled on a per-category basis.

## Addons list

A list of all installed addons, obtained by listing the contents of the _UserAppDataDir_/Mod directory on your
system.

## FreeCAD preferences

The following FreeCAD preferences:
* language
* theme
* stylesheet
* geometry
* overlay_stylesheet
* default_unit_schema

## System statistics

The output of the following Python commands:
* platform.machine()
* platform.system()
* platform.version()
* platform.python_version()

## Future plans
Eventually if FreeCAD crashes while this addon is running, crash data will automatically be sent to the server.
This data **will not** include information about your CAD model or detailed information about your system. No
data will be added to the collection list without a dialog informing you of the change when the new version
is first launched.

## Disabling collection
You can disable this data reporting by removing the Addon via the Addon Manager, by manually deleting the addon
from your FreeCAD Mod directory, or temporarily by unchecking "Enabled" in the Telemetry Addon's preferences. You
may also individually uncheck the categories described above if you are not comfortable sending the listed data, but
still wish to participate in the overall metrics program.

## Who has access to the data?

Only FreeCAD's maintainers have access to the raw data, but aggregate data will be made available to the public.
That is currently a work-in-progress.
