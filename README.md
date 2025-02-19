# FreeCAD Telemetry Addon

This addon sends select FreeCAD usage information to a centralized database.

# Why you should share telemetry with the FreeCAD project?

FreeCAD is a community project.  We freely contribute our time and money to make the software as good as possible for the largest number of users.
Contributing data is another way of supporting the project.

Sharing telemetry with FreeCAD helps the project leaders and developers make a better solution for everyone and allocate donations responsibly.
Without good data, it is difficult to make good decisions between competing priorities: for example, which bugs to prioritize fixing.
Without good data, forum discussions become anecdotal and emotional.

Good data solves many problems.

Our telemetry is intended to help us understand how many people are affected by our decisions.  For example:

- How many people are affected by a given bug
- How many people are running an Addon that may be affected by an API change
- How many people are using a specific translation and would benefit from improving it
- How long should we maintain support and documentation for older releases

The telemetry also helps us fine tune the user experience to benefit the largest number of users with default settings:

- What are the most popular unit schemas, themes
- Do addons contain features that should be in the core experience
- Which platforms are the most popular and should receive the most development support

These are just examples and it is important to understand that we will never sell data to third parties and will not use the data to market products or services to you.

# What data is sent?

Telemetry data is selected to be non-identifying.  Nothing sent is personally identifying: upon installation of the
Addon you are automatically assigned a random UUID that can be used to request data removal if you later choose
not to participat in the Telemetry project.

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
* FreeCADGui.getMainWindow().screen().availableSize()
* FreeCADGui.getMainWindow().screen().devicePixelRatio()

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

## Requesting removal of data

In the Telemetry Addon preferences your UUID is displayed. To request that your data be removed from our telemetry
collection, click the button next to it to engage an automated process, or send a removal request with that UUID to
telemetry@freecad.org. This will not affect your use of FreeCAD in any way, nor cancel any other online accounts you
may have: those accounts are not tied in any way to the generated UUID.

## Who has access to the data?

Only FreeCAD's maintainers have access to the raw data, but aggregate data will be made available to the public.
That is currently a work-in-progress.
