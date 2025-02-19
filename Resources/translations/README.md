# About translating the Telemetry Workbench

(Adapted from the [Sheet Metal Workbench](https://github.com/shaise/FreeCAD_SheetMetal/edit/master/Resources/translations/README.md))

## Translators

Translation for this workbench is done by visiting the **FreeCAD-addons**
project on CrowdIn platform at <https://crowdin.com/project/freecad-addons> webpage,
then find your language, look for the **Telemetry** project and do the translation.

## Maintainers

> [!NOTE]
> All commands **must** be run in `./Resorces/translations/` directory.

> [!WARNING]
> If you want to update/release the files you need to have installed
> `lupdate` and `lrelease` from Qt6 version. Using the versions from
> Qt5 is not advised because they're buggy.

## Updating translations template file

To update the template file from source files you should use this command:

```shell
./update_translation.sh -U
```

Once done you can commit the changes and upload the new file to CrowdIn platform
at <https://crowdin.com/project/freecad-addons> webpage and find the **Telemetry** project.

## More information

You can read more about translating external workbenches here:

<https://wiki.freecad.org/Translating_an_external_workbench>
