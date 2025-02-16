# FreeCAD Telemetry Addon

This addon sends select telemetry information to FreeCAD's Sentry server. When installed, every time you run FreeCAD,
basic session information is transmitted to let the FreeCAD developers know which versions of FreeCAD are in use. In
addition, if FreeCAD crashes while this addon is running, crash data is automatically sent to the server. This data
**does not** include information about your model or detailed information about your system. You can disable this data
reporting by removing the Addon, either via the Addon Manager, or by manually deleting it from your FreeCAD Mod
directory.

## Who has access to the data?

Only FreeCAD's maintainers have access to the raw data, but aggregate data will be made available to the public. That is
currently a work-in-progress.
