# FreeCAD Telemetry Addon

This addon sends select telemetry information to a centralized database. When installed, every time you run FreeCAD,
basic session information is transmitted to let the FreeCAD developers know which versions of FreeCAD are in use. It
also sends your current FreeCAD Language setting and your OS information. Finally, a list of the Addons you have
installed is transmitted.

## Future plans
Eventually if FreeCAD crashes while this addon is running, crash data will automatically be sent to the server.
This data **does not** include information about your model or detailed information about your system.

## Disabling collection
You can disable this data reporting by removing the Addon via the Addon Manager, by manually deleting the addon
from your FreeCAD Mod directory, or temporarily by unchecking "Enabled" in the Telemetry Addon's preferences.

## Who has access to the data?

Only FreeCAD's maintainers have access to the raw data, but aggregate data will be made available to the public.
That is currently a work-in-progress.
