# SPDX-License-Identifier: LGPL-2.1-or-later
# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2025 The FreeCAD project association AISBL              *
# *                                                                         *
# *   This file is part of Telemetry, a FreeCAD addon.                      *
# *                                                                         *
# *   Telemetry is free software: you can redistribute it and/or modify it  *
# *   under the terms of the GNU Lesser General Public License as           *
# *   published by the Free Software Foundation, either version 2.1 of the  *
# *   License, or (at your option) any later version.                       *
# *                                                                         *
# *   Telemetry is distributed in the hope that it will be useful, but      *
# *   WITHOUT ANY WARRANTY; without even the implied warranty of            *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU      *
# *   Lesser General Public License for more details.                       *
# *                                                                         *
# *   You should have received a copy of the GNU Lesser General Public      *
# *   License along with Telemetry. If not, see                             *
# *   <https://www.gnu.org/licenses/>.                                      *
# *                                                                         *
# ***************************************************************************

try:
    import FreeCAD
    import FreeCADGui
except ImportError as e:
    raise RuntimeError("This is a FreeCAD Addon, and should be run from within FreeCAD") from e

try:
    from posthog import Posthog
except ImportError as e:
    raise ImportError("Posthog Python package is not installed: pip install posthog") from e

import os
import platform
import uuid

posthog = Posthog(
    project_api_key="phc_Q9zaBGzSRys31DO8dSp8YepSICY1CJh2xRBUmrbt3Jl",
    host="https://eu.i.posthog.com",
    disable_geoip=True,
)

anonymous_id = str(uuid.uuid4())
# posthog.identify(distinct_id=anonymous_id)


def posthog_launch():
    """Send launch statistics to Posthog: FreeCAD version and platform"""
    release = FreeCAD.Version()
    if release[6] and release[6] != "main":
        return  # Do not capture information about branches

    locale = FreeCADGui.getLocale()
    current_language = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/General").GetString(
        "Language", locale
    )

    posthog.capture(
        anonymous_id,
        event="freecad_launch",
        properties={
            "version_major": release[0],
            "version_minor": release[1],
            "version_patch": release[2],
            "system": platform.system(),
            "system_version": platform.version(),
            "fc_language": current_language,
            "$process_person_profile": False,  # Do not include person information
        },
    )


def posthog_addon_list():
    home_mod = FreeCAD.getUserAppDataDir() + "Mod"
    home_mod = os.path.realpath(home_mod)
    mods = []
    if os.path.isdir(home_mod):
        mod_dirs = os.listdir(home_mod)
        for mod_dir in mod_dirs:
            if not ".backup" in mod_dir and mod_dir[0] != "." and mod_dir != "CVS":
                mods.append(mod_dir.lower())
    posthog.capture(
        anonymous_id,
        event="freecad_addon_list",
        properties={
            "mods": mods,
            "$process_person_profile": False,  # Do not include person information
        },
    )


def posthog_shutdown():
    posthog.flush()
