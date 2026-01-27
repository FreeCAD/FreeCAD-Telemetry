# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Telemetry addon.

import freecad.Telemetry as module
from importlib import resources
from typing import TypedDict

translations = resources.files(module) / "Resources/Translations"
interfaces = resources.files(module) / "Resources/Interfaces"
icons = resources.files(module) / "Resources/Icons"


class PathsDict(TypedDict):
    Translations: str
    Icons: str


Paths: PathsDict = {"Translations": str(translations), "Icons": str(icons)}


def asInterface(name: str):

    file = name + ".ui"

    interface = interfaces / file

    with resources.as_file(interface) as path:
        return str(path)


def asIcon(name: str):

    file = name + ".svg"

    icon = icons / file

    with resources.as_file(icon) as path:
        return str(path)
