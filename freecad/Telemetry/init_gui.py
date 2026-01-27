# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Telemetry addon.

################################################################################
#                                                                              #
#   © 2025 FreeCAD Project Association                                         #
#                                                                              #
#   This addon is free software: you can redistribute it and/or modify         #
#   it under the terms of the GNU Lesser General Public License as             #
#   published by the Free Software Foundation, either version 2.1              #
#   of the License, or (at your option) any later version.                     #
#                                                                              #
#   This addon is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty                #
#   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    #
#   See the GNU Lesser General Public License for more details.                #
#                                                                              #
#   You should have received a copy of the GNU Lesser General Public           #
#   License along with this addon. If not, see https://www.gnu.org/licenses    #
#                                                                              #
################################################################################

import freecad.Telemetry.Environment

from FreeCAD import Console , ParamGet , Gui

from .Preferences import Preferences
from .Resources import asInterface , asIcon , Paths
from .PostHog import posthog_shutdown, posthog_launch
from .PySide import QtWidgets

Gui.addLanguagePath(Paths['Translations'])
Gui.updateLocale()


def setup_posthog():
    params = ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enable", True)
    if not enabled:
        Console.PrintLog(
            "PostHog initializing, but FreeCAD launch metrics sending is disabled: no data will be transmitted\n"
        )
        return
    else:
        Console.PrintLog("PostHog initializing. FreeCAD launch metrics are being sent.\n")
    posthog_launch()


def setup():

    Gui.addPreferencePage(Preferences, "Telemetry")
    Gui.addIconPath(Paths['Icons'])

    params = ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    first_start = params.GetBool("FirstStart", True)

    if first_start:
        dialog = Gui.PySideUic.loadUi(asInterface('Welcome')) # type: ignore
        dialog.exec()

        enabled = dialog.settings_group_box.isChecked()
        addons_enabled = dialog.addon_checkbox.isChecked()
        preferences_enabled = dialog.preferences_checkbox.isChecked()
        system_enabled = dialog.system_checkbox.isChecked()

        params.SetBool("Enable", enabled)
        params.SetBool("SendAddonInformation", addons_enabled)
        params.SetBool("SendPreferences", preferences_enabled)
        params.SetBool("SendSystemInformation", system_enabled)

        params.SetBool("FirstStart", False)

    setup_posthog()

    app = QtWidgets.QApplication.instance()

    if app:
        app.aboutToQuit.connect(posthog_shutdown)


class Telemetry(Gui.Workbench):
    """Telemetry is not *really* a workbench, so this class is basically empty."""

    Icon = asIcon('Logo')

    def __init__(self):
        super().__init__()
        Console.PrintLog("Telemetry workbench loaded\n")

    def Activated(self):
        """This function is executed when the workbench is activated"""

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""

    def GetClassName(self):
        """This function is mandatory if this is a full python workbench"""
        return "Gui::PythonWorkbench"


setup()
