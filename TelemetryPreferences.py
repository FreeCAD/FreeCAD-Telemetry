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

from PySide import QtWidgets, QtCore

import TelemetryPaths
from Sentry import init_sentry


class TelemetryPreferences:
    """A class containing a form element that is inserted as a FreeCAD preference page."""

    def __init__(self, _=None):
        self.form = FreeCADGui.PySideUic.loadUi(
            os.path.join(TelemetryPaths.panels_path, "preferences.ui")
        )
        self.form.dsn_line_edit.textEdited.connect(self._dsn_changed)
        if hasattr(self.form.enable_check_box, "checkStateChanged"):
            # With Qt 6.7 the original stateChanged was deprecated and changed to checkStateChanged
            self.form.enable_check_box.checkStateChanged.connect(self._enable_check_state_changed)
        else:
            self.form.enable_check_box.stateChanged.connect(self._enable_check_state_changed)
        self.form.dsn_line_edit.textEdited.connect(self._dsn_changed)

    def saveSettings(self):
        """Required function: called by the preferences dialog when Apply or Save is clicked,
        saves out the preference data by reading it from the widgets."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        params.SetBool(
            "Enable", 1 if self.form.enable_check_box.checkState() == QtCore.Qt.Checked else 0
        )
        params.SetString("DSN", self.form.dsn_line_edit.text())

    def loadSettings(self):
        """Required function: called by the preferences dialog when it is launched,
        loads the preference data and assigns it to the widgets."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        enable = params.GetBool("Enable", True)
        dsn = params.GetString("DSN", "unset")
        self.form.enable_check_box.setChecked(enable)
        self.form.dsn_line_edit.setText(dsn)

    def _dsn_changed(self, text):
        """Update the DSN in the FreeCAD parameters."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        params.SetString("DSN", text)
        init_sentry(text)
        FreeCAD.Console.PrintMessage(f"Telemetry is now being sent to {text}\n")
        self._reset_sentry()

    def _enable_check_state_changed(self, check_state):
        """Update the enable state in the FreeCAD parameters."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        params.SetBool("Enable", 1 if check_state == QtCore.Qt.Checked else 0)
        self._reset_sentry()

    def _reset_sentry(self):
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        if params.GetBool("Enable", True):
            dsn = params.GetString("DSN", "unset")
            FreeCAD.Console.PrintMessage(f"Resetting Sentry to use DSN {dsn}\n")
            init_sentry(dsn=dsn)
        else:
            FreeCAD.Console.PrintMessage(f"Deactivating Sentry (setting dsn=None)\n")
            init_sentry(dsn=None)
