![Logo]

# Telemetry Addon [ Beta ]

Sends non-identifying usage information to FreeCAD.

This addon doesn't ship with FreeCAD and is optional.

*If you have the time, please try out this Beta!*  
*See [Installing Telemetry](#installation) below.*

## Why you should share telemetry with the FreeCAD project

[FreeCAD] is a community project. We freely contribute our time and money to make the software as good as possible for the largest number of users. Contributing data is another way of supporting the project.

Sharing telemetry with FreeCAD helps the project leaders and developers make a better solution for everyone and allocate
donations responsibly. Without good data, it is difficult to make good decisions between competing priorities: for
example, which bugs to prioritize fixing. Without good data, forum discussions become anecdotal and emotional.

Good data solves many problems.

Our telemetry is intended to help us understand how many people are affected by our decisions. For example:

- How many people are affected by a given bug
- How many people are running an Addon that may be affected by an API change
- How many people are using a specific translation and would benefit from improving it
- How long should we maintain support and documentation for older releases

The telemetry also helps us fine tune the user experience to benefit the largest number of users with default settings:

- What are the most popular unit schemas, themes
- Do addons contain features that should be in the core experience
- Which platforms are the most popular and should receive the most development support

These are just examples, and it is important to understand that we will never sell data to third parties and will not
use the data to market products or services to you.

## Shared Data

Telemetry data is selected to be non-identifying. Nothing sent is personally identifying: upon installation of the
Addon you are automatically assigned a random UUID that can be used to request data removal if you later choose
not to participate in the Telemetry project.

When installed, every time you run FreeCAD, the current version of FreeCAD is sent to our telemetry server
(current using the [PostHog](https://posthog.com) service with data retained in the EU). This is also transmitted when
FreeCAD shuts down correctly (e.g. without a crash) to enable us to gather aggregate crash statistics about each version
of FreeCAD.

In addition, three other categories of information are usually sent, but can be disabled on a per-category basis.

### Addons

We may collect the list of names of your installed addons.

This list can be obtained by listing the  contents of the  
`{UserAppDataDir}/Mod` directory on your system.

### Preferences

We may collect a variety of your preferences:

-   Language
-   Theme
-   Stylesheet
-   Window geometry
-   Overlay stylesheet
-   Default unit schema

### System

We may collect system details from the  
output of the following Python commands:

-   [`platform.machine()`][Python - Machine]  
    ➞ `x86_64`

-   [`platform.system()`][Python - System]  
    ➞ `Linux`

-   [`platform.version()`][Python - SVersion]  
    ➞ `#45-Ubuntu SMP PREEMPT_DYNAMIC Thu Dec 06 12:50:01 UTC 2024`

-   [`platform.python_version()`][Python - PVersion]  
    ➞ `3.12.1`

-   [`FreeCADGui.getMainWindow().screen().availableSize()`][QT - Size]  
    ➞ `{ width : 1920 , height : 1080 }`

-   [`FreeCADGui.getMainWindow().screen().devicePixelRatio()`][QT - Ratio]  
    ➞ `1.0`

### Future plans

Eventually if FreeCAD crashes while this addon is running, crash data will automatically be sent to the server.
This data **will not** include information about your CAD model or detailed information about your system. No
data will be added to the collection list without a dialog informing you of the change when the new version
is first launched.

### Disabling collection

You can disable this data reporting by removing the Addon via the Addon Manager, by manually deleting the addon
from your FreeCAD Mod directory, or temporarily by unchecking "Enabled" in the Telemetry Addon's preferences. You
may also individually uncheck the categories described above if you are not comfortable sending the listed data, but
still wish to participate in the overall metrics program.

### Data Removal

To request that your data be removed from our telemetry collection, click the button in the Telemetry preferences
page to engage an automated process, or send a removal request with your UUID (found in the FreeCAD Tools menu, under
"Edit parameters" -- look for `BaseApp/Preferences/Mod/Telemetry/PostHogUUID`) to
[telemetry@freecad.org](mailto:telemetry@freecad.org). This will not affect your use of FreeCAD in any way, nor cancel
any other online accounts you may have: those accounts are not tied in any way to the generated UUID.

### Requesting a copy of your data

To receive a copy of the data associated with your UUID, please send email to
[telemetry@freecad.org](mailto:telemetry@freecad.org) with your UUID (see instructions in
[Requesting removal of data](#requesting-removal-of-data)) and your preferred data format (CSV or XLSX).

### Who has access to the data?

The data is collected by [The FreeCAD project association AISBL](https://fpa.freecad.org/) who stewards the data
on behalf of all users and developers of FreeCAD. Only FPA officers, FreeCAD's maintainers, and system administrators
have access to the raw data, but aggregate data will be made available to the public. Publication of the data is
currently a work-in-progress.

### Privacy and GDPR compliance

See our [Privacy Policy](PRIVACY_POLICY.md).

## Installation

While it is still in beta testing this addon is not in the official FreeCAD addons list. The easiest way to install it
is to edit the Addon Manager's preferences to add a new custom repository,
`https://github.com/FreeCAD/FreeCAD-Telemetry` with branch `main`. The Telemetry addon will then be displayed in the
Addon Manager like normal addons. When installing, it will require the installation of the `posthog` Python package,
which the Addon Manager will handle.

As an alternative you can install the addon manually by cloning it from its git repository into your
`{userAppDataDir}/Mod` directory. Use pip to install the contents of the `requirements.txt` file (use the same Python
interpreter that FreeCAD uses to ensure the requirements are found).


[FreeCAD]: https://freecad.org
[Logo]: Resources/icons/TelemetryIcon.png "A heart rate monitor with the FreeCAD logo on it"

[Python - SVersion]: https://docs.python.org/3/library/platform.html#platform.version
[Python - PVersion]: https://docs.python.org/3/library/platform.html#platform.python_version
[Python - Machine]: https://docs.python.org/3/library/platform.html#platform.machine
[Python - System]: https://docs.python.org/3/library/platform.html#platform.system

[QT - Ratio]: https://doc.qt.io/qt-6/qscreen.html#devicePixelRatio-prop
[QT - Size]: https://doc.qt.io/qt-6/qscreen.html#availableSize-prop
