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

import FreeCAD
import FreeCADGui

import os

from PySide import QtWidgets

import TelemetryPaths
import TelemetryPreferences

# from Sentry import close_sentry_session
from PosthogFC import posthog_shutdown, posthog_launch, posthog_addon_list


FreeCADGui.addLanguagePath(TelemetryPaths.language_path)
FreeCADGui.updateLocale()


def setup_posthog():
    global posthog_launch
    global posthog_addon_list
    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enable", True)
    if not enabled:
        FreeCAD.Console.PrintMessage(
            "PostHog initializing, but FreeCAD launch metrics sending is disabled: no data will be transmitted\n"
        )
        return
    else:
        FreeCAD.Console.PrintMessage(
            "PostHog initializing. FreeCAD launch metrics are being sent.\n"
        )
    posthog_launch()


def setup():
    global TelemetryPaths
    global TelemetryPreferences
    global QtWidgets
    # global close_sentry_session
    global posthog_shutdown, setup_posthog

    FreeCADGui.addPreferencePage(TelemetryPreferences.TelemetryPreferences, "Telemetry")
    FreeCADGui.addIconPath(TelemetryPaths.icons_path)

    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    first_start = params.GetBool("FirstStart", True)

    if first_start:
        r = QtWidgets.QMessageBox.information(
            None,
            FreeCAD.Qt.translate("Telemetry", "Telemetry Addon Activated"),
            FreeCAD.Qt.translate(
                "Telemetry",
                "Thank you for installing the Telemetry addon! This addon will "
                "send data about each FreeCAD session to a central server."
                " It can be disabled in Preferences, or by removing it entirely.",
            ),
            QtWidgets.QMessageBox.Ok,
        )
        params.SetBool("FirstStart", False)

    setup_posthog()

    # QtWidgets.QApplication.instance().aboutToQuit.connect(close_sentry_session)
    QtWidgets.QApplication.instance().aboutToQuit.connect(posthog_shutdown)


class Telemetry(Workbench):
    """Telemetry is not *really* a workbench, so this class is basically empty."""

    Icon = os.path.join(TelemetryPaths.icons_path, "telemetryLogo.svg")

    def __init__(self):
        super().__init__()
        FreeCAD.Console.PrintMessage("Telemetry workbench loaded\n")

    def Activated(self):
        """This function is executed when the workbench is activated"""

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""

    def GetClassName(self):
        """This function is mandatory if this is a full python workbench"""
        return "Gui::PythonWorkbench"


setup()
