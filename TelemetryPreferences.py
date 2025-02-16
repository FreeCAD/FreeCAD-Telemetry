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

    def _dsn_changed(self, text):
        """Update the DSN in the FreeCAD parameters."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        params.SetString("DSN", text)
        init_sentry(text)
        FreeCAD.Console.PrintMessage(f"Telemetry is now being sent to {text}\n")
