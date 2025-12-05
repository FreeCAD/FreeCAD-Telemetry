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

from datetime import datetime
import os
import platform
from typing import Optional, Dict, Any
import uuid

posthog: Optional[Posthog] = None
posthog_id: str = ""


def posthog_launch():
    global posthog
    global posthog_id
    """Send statistics to Posthog based on user preferences settings"""

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
        on_error=handle_error,
    )

    system = params.GetBool("SendSystemInformation", True)
    addon = params.GetBool("SendAddonInformation", True)
    preferences = params.GetBool("SendPreferences", True)

    FreeCAD.Console.PrintLog("Telemetry Addon: Sending FreeCAD version data to Posthog\n")
    posthog_fc_startup()
    posthog_fc_version()
    if system:
        FreeCAD.Console.PrintLog("Telemetry Addon: Sending FreeCAD system info to Posthog\n")
        posthog_system_info()
    if addon:
        FreeCAD.Console.PrintLog("Telemetry Addon: Sending FreeCAD addon info to Posthog\n")
        posthog_addon_list()
    if preferences:
        FreeCAD.Console.PrintLog(
            "Telemetry Addon: Sending FreeCAD preferences info to Posthog\n"
        )
        posthog_preferences()
    params.SetString("LastSendTime", datetime.now().isoformat())


def handle_error(exception: Exception, _payload: Optional[Dict[str, Any]]) -> None:
    FreeCAD.Console.PrintLog(
        "Telemetry Addon: Error connecting, no telemetry will be sent for this session\n"
    )
    FreeCAD.Console.PrintLog(str(exception) + "\n")


def posthog_fc_startup():
    global posthog
    posthog.capture(distinct_id=posthog_id, event="freecad_startup")


def posthog_fc_shutdown():
    global posthog
    posthog.capture(distinct_id=posthog_id, event="freecad_shutdown")


def posthog_fc_version():
    """Send FreeCAD version to Posthog"""
    global posthog
    release = FreeCAD.Version()

    posthog.capture(
        distinct_id=posthog_id,
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
        distinct_id=posthog_id,
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


def get_preference(path: str, pref_type: str, default: any, transform: callable = lambda x: x):
    group = os.path.dirname(path)
    name = os.path.basename(path)

    preference_group = FreeCAD.ParamGet(f"User parameter:{group}")
    getter = getattr(preference_group, f"Get{pref_type.capitalize()}")

    return transform(getter(name, default))


class TrackedPreference:
    @classmethod
    def string(cls, path: str, default: str, **kwargs):
        return get_preference(path=path, pref_type="string", default=default, **kwargs)

    @classmethod
    def bool(cls, path: str, default: bool, **kwargs):
        return get_preference(path=path, pref_type="bool", default=default, **kwargs)

    @classmethod
    def unsigned(cls, path: str, default: int, **kwargs):
        return get_preference(path=path, pref_type="unsigned", default=default, **kwargs)

    @classmethod
    def int(cls, path: str, default: int, **kwargs):
        return get_preference(path=path, pref_type="int", default=default, **kwargs)

    @classmethod
    def double(cls, path: str, default: float, **kwargs):
        return get_preference(path=path, pref_type="double", default=default, **kwargs)


def ui_panel_preferences(_name: str, overlay_name: str, prefix: str):
    def get_overlay_preferences():
        placements = ["left", "right", "top", "bottom"]
        for placement in placements:
            overlay_group = FreeCAD.ParamGet(
                f"User parameter:BaseApp/MainWindow/DockWindows/Overlay{placement.capitalize()}"
            )
            overlay_widgets = overlay_group.GetString("Widgets", "").split(",")

            if overlay_name in overlay_widgets:
                overlay_preferences = {
                    "overlay": placement,
                    "transparent": overlay_group.GetBool("Transparent", False),
                }

                if placement in ["left", "right"]:
                    overlay_preferences["width"] = overlay_group.GetInt("Width", 0)
                else:
                    overlay_preferences["height"] = overlay_group.GetInt("Height", 0)

                return overlay_preferences

        return {}

    preferences = {
        "enabled": TrackedPreference.bool(path="BaseApp/MainWindow/DockWindows", default=False),
        **get_overlay_preferences(),
    }

    return {f"{prefix}_{name}": preference for name, preference in preferences.items()}


def posthog_preferences():
    """Send some basic FreeCAD preferences to Posthog"""
    global posthog

    preferences = {
        "language": TrackedPreference.string(
            path="BaseApp/Preferences/General/Language",
            default=FreeCADGui.getLocale(),
        ),
        "theme": TrackedPreference.string(
            path="BaseApp/Preferences/MainWindow/Theme", default="unset"
        ),
        "stylesheet": TrackedPreference.string(
            path="BaseApp/Preferences/MainWindow/StyleSheet",
            default="unset",
        ),
        "overlay_stylesheet": TrackedPreference.string(
            path="BaseApp/Preferences/MainWindow/OverlayActiveStyleSheet",
            default="unset",
        ),
        "geometry": TrackedPreference.string(
            path="BaseApp/Preferences/MainWindow/Geometry",
            default="unset",
        ),
        "default_unit_schema": TrackedPreference.int(
            path="BaseApp/Preferences/Units/UserSchema", transform=str, default=0
        ),
        "sketcher_dimension_single_tool": TrackedPreference.bool(
            path="BaseApp/Preferences/Mod/Sketcher/dimensioning/SingleDimensioningTool",
            default=True,
        ),
        "sketcher_dimension_separate_tools": TrackedPreference.bool(
            path="BaseApp/Preferences/Mod/Sketcher/dimensioning/SeparatedDimensioningTools",
            default=False,
        ),
        "sketcher_constraint_unified_coincident": TrackedPreference.bool(
            path="BaseApp/Preferences/Mod/Sketcher/Constraints/UnifiedCoincident",
            default=True,
        ),
        "sketcher_constraint_auto_hor_ver": TrackedPreference.bool(
            path="BaseApp/Preferences/Mod/Sketcher/Constraints/AutoHorVer",
            default=True,
        ),
        "sketcher_on_view_parameters": TrackedPreference.int(
            path="BaseApp/Preferences/Mod/Sketcher/Tools/OnViewParameterVisibility",
            transform=str,
            default=1,
        ),
        "workbench_enabled_list": TrackedPreference.string(
            path="BaseApp/Preferences/Workbenches/Ordered",
            transform=lambda s: s.split(","),
            default="",
        ),
        "workbench_disabled_list": TrackedPreference.string(
            path="BaseApp/Preferences/Workbenches/Disabled",
            transform=lambda s: s.split(","),
            default="",
        ),
        "workbench_default": TrackedPreference.string(
            path="BaseApp/Preferences/General/AutoloadModule",
            default="",
        ),
        "ui_workbench_selector": TrackedPreference.int(
            path="BaseApp/Preferences/Workbenches/WorkbenchSelectorType",
            transform=str,
            default=0,
        ),
        "navigation_style": TrackedPreference.string(
            path="BaseApp/Preferences/View/NavigationStyle",
            default="Gui::CADNavigationStyle",
        ),
        "navigation_orbit_style": TrackedPreference.int(
            path="BaseApp/Preferences/View/OrbitStyle",
            default=1,
        ),
        "navigation_rotation_style": TrackedPreference.int(
            path="BaseApp/Preferences/View/RotationStyle", default=1
        ),
        "ui_toolbar_icon_size": TrackedPreference.int(
            path="BaseApp/Preferences/General/ToolbarIconSize",
            default=24,
        ),
        **ui_panel_preferences("Std_TaskView", "Tasks", "ui_task_view"),
        **ui_panel_preferences("Std_TreeView", "Tree view", "ui_tree_view"),
        **ui_panel_preferences("Std_ComboView", "Property view", "ui_property_view"),
        **ui_panel_preferences("Std_PythonView", "Python console", "ui_python_console"),
        **ui_panel_preferences("Std_ReportView", "Report view", "ui_report_view"),
    }

    posthog.capture(distinct_id=posthog_id, event="freecad_preferences", properties=preferences)


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
        distinct_id=posthog_id,
        event="freecad_addon_list",
        properties={"mods": mods, "total_mods": len(mods)},
    )


def posthog_shutdown():
    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enabled", True)
    if enabled and posthog:
        FreeCAD.Console.PrintLog("Telemetry Addon: Sending FreeCAD shutdown info to Posthog\n")
        posthog_fc_shutdown()
        posthog.flush()
