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

posthog = None
posthog_id = None


def posthog_launch():
    global posthog
    global posthog_id
    """Send statistics to Posthog based on user preferences settings"""
    release = FreeCAD.Version()
    if release[6] and release[6] != "main":
        FreeCAD.Console.PrintMessage(
            f"Telemetry Addon: You are on branch {release[6]}, so no data will be sent.\n"
        )
        return  # Do not capture information about branches

    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enabled", True)
    if not enabled:
        return  # Addon is disabled, send nothing

    posthog_id = params.GetString("PostHogUUID", "unset")
    if posthog_id == "unset":
        posthog_id = str(uuid.uuid4())
        params.SetString("PostHogUUID", posthog_id)

    posthog = Posthog(
        project_api_key=params.GetString(
            "PostHogAPIKey", "phc_Q9zaBGzSRys31DO8dSp8YepSICY1CJh2xRBUmrbt3Jl"
        ),
        host=params.GetString("PostHogURL", "https://eu.i.posthog.com"),
        disable_geoip=True,
    )

    system = params.GetBool("SendSystemInformation", True)
    addon = params.GetBool("SendAddonInformation", True)
    preferences = params.GetBool("SendPreferences", True)

    FreeCAD.Console.PrintMessage("Telemetry Addon: Sending FreeCAD version data to Posthog\n")
    posthog_fc_startup()
    posthog_fc_version()
    if system:
        FreeCAD.Console.PrintMessage("Telemetry Addon: Sending FreeCAD system info to Posthog\n")
        posthog_system_info()
    if addon:
        FreeCAD.Console.PrintMessage("Telemetry Addon: Sending FreeCAD addon info to Posthog\n")
        posthog_addon_list()
    if preferences:
        FreeCAD.Console.PrintMessage(
            "Telemetry Addon: Sending FreeCAD preferences info to Posthog\n"
        )
        posthog_preferences()


def posthog_fc_startup():
    global posthog
    posthog.capture(posthog_id, event="freecad_startup")


def posthog_fc_shutdown():
    global posthog
    posthog.capture(posthog_id, event="freecad_shutdown")


def posthog_fc_version():
    """Send FreeCAD version to Posthog"""
    global posthog
    release = FreeCAD.Version()

    posthog.capture(
        posthog_id,
        event="freecad_version",
        properties={
            "version_major": release[0],
            "version_minor": release[1],
            "version_patch": release[2],
        },
    )


def posthog_system_info():
    """Send FreeCAD system information to Posthog"""
    global posthog
    screen = FreeCADGui.getMainWindow().screen()
    screen_size = screen.availableSize()
    posthog.capture(
        posthog_id,
        event="freecad_system_info",
        properties={
            "machine": platform.machine(),
            "system": platform.system(),
            "system_version": platform.version(),
            "python_version": platform.python_version(),
            "screen_resolution": f"{screen_size.width()}x{screen_size.height()}",
            "screen_dpi": screen.devicePixelRatio(),
        },
    )


def posthog_preferences():
    """Send some basic FreeCAD preferences to Posthog"""
    global posthog
    general = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/General")
    main_window = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/MainWindow")
    units = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units")

    posthog.capture(
        posthog_id,
        event="freecad_preferences",
        properties={
            "language": general.GetString("Language", FreeCADGui.getLocale()),
            "theme": main_window.GetString("Theme", "unset"),
            "stylesheet": main_window.GetString("Stylesheet", "unset"),
            "geometry": main_window.GetString("Geometry", "unset"),
            "overlay_stylesheet": main_window.GetString("OverlayActiveStyleSheet", "unset"),
            "default_unit_schema": units.GetInt("UserSchema", 0),
        },
    )


def posthog_addon_list():
    """Send FreeCAD addon list to Posthog"""
    global posthog
    home_mod = FreeCAD.getUserAppDataDir() + "Mod"
    home_mod = os.path.realpath(home_mod)
    mods = []
    if os.path.isdir(home_mod):
        mod_dirs = os.listdir(home_mod)
        for mod_dir in mod_dirs:
            if not ".backup" in mod_dir and mod_dir[0] != "." and mod_dir != "CVS":
                mods.append(mod_dir.lower())
    posthog.capture(
        posthog_id,
        event="freecad_addon_list",
        properties={
            "mods": mods,
        },
    )


def posthog_shutdown():
    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enabled", True)
    if enabled and posthog:
        FreeCAD.Console.PrintMessage("Telemetry Addon: Sending FreeCAD shutdown info to Posthog\n")
        posthog_fc_shutdown()
        posthog.flush()
