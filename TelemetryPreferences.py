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

import json
import os
import urllib.request

from PySide import QtWidgets, QtCore

import TelemetryPaths

# from Sentry import init_sentry


class TelemetryPreferences:
    """A class containing a form element that is inserted as a FreeCAD preference page."""

    def __init__(self, _=None):
        self.form = FreeCADGui.PySideUic.loadUi(
            os.path.join(TelemetryPaths.panels_path, "preferences.ui")
        )
        # Don't need the next line until we choose to start using Sentry for crash reporting
        # self.form.dsn_line_edit.textEdited.connect(self._dsn_changed)
        if hasattr(self.form.enable_check_box, "checkStateChanged"):
            # With Qt 6.7 the original stateChanged was deprecated and changed to checkStateChanged
            self.form.enable_check_box.checkStateChanged.connect(self._enable_check_state_changed)
        else:
            self.form.enable_check_box.stateChanged.connect(self._enable_check_state_changed)
        self.form.request_data_removal_pushbutton.clicked.connect(self._data_removal_clicked)

    def saveSettings(self):
        """Required function: called by the preferences dialog when Apply or Save is clicked,
        saves out the preference data by reading it from the widgets."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        params.SetBool("Enable", self.form.enable_check_box.isChecked())
        params.SetBool("SendSystemInformation", self.form.system_check_box.isChecked())
        params.SetBool("SendAddonInformation", self.form.addons_check_box.isChecked())
        params.SetBool("SendPreferences", self.form.preferences_check_box.isChecked())
        params.SetString("DSN", self.form.dsn_line_edit.text())
        params.SetString("PostHogURL", self.form.posthog_url_line_edit.text())
        params.SetString("PostHogAPIKey", self.form.posthog_api_key_line_edit.text())
        # self._reset_sentry()  # If we start using Sentry, uncomment

    def loadSettings(self):
        """Required function: called by the preferences dialog when it is launched,
        loads the preference data and assigns it to the widgets."""
        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
        enable = params.GetBool("Enable", True)
        system = params.GetBool("SendSystemInformation", True)
        addon = params.GetBool("SendAddonInformation", True)
        preferences = params.GetBool("SendPreferences", True)
        host = params.GetString("PostHogURL", "https://eu.i.posthog.com")
        api_key = params.GetString(
            "PostHogAPIKey", "phc_Q9zaBGzSRys31DO8dSp8YepSICY1CJh2xRBUmrbt3Jl"
        )
        uuid = params.GetString("PostHogUUID", "unset")
        dsn = params.GetString("DSN", "unset")
        self.form.enable_check_box.setChecked(enable)
        self.form.dsn_line_edit.setText(dsn)
        self.form.posthog_url_line_edit.setText(host)
        self.form.posthog_api_key_line_edit.setText(api_key)
        self.form.system_check_box.setChecked(system)
        self.form.addons_check_box.setChecked(addon)
        self.form.preferences_check_box.setChecked(preferences)
        self._enable_check_state_changed(QtCore.Qt.Checked if enable else QtCore.Qt.Unchecked)

    def _enable_check_state_changed(self, check_state):
        """Update the enable state of the sub-widgets"""
        if check_state == QtCore.Qt.Checked:
            self.form.dsn_line_edit.setEnabled(True)
            self.form.posthog_url_line_edit.setEnabled(True)
            self.form.posthog_api_key_line_edit.setEnabled(True)
            self.form.addons_check_box.setEnabled(True)
            self.form.system_check_box.setEnabled(True)
            self.form.preferences_check_box.setEnabled(True)
        else:
            self.form.dsn_line_edit.setEnabled(False)
            self.form.posthog_url_line_edit.setEnabled(False)
            self.form.posthog_api_key_line_edit.setEnabled(False)
            self.form.addons_check_box.setEnabled(False)
            self.form.system_check_box.setEnabled(False)
            self.form.preferences_check_box.setEnabled(False)

    #    def _dsn_changed(self, text):
    #        """Update the DSN in the FreeCAD parameters."""
    #        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    #        params.SetString("DSN", text)
    #        init_sentry(text)
    #        FreeCAD.Console.PrintMessage(f"Telemetry is now being sent to {text}\n")
    #        self._reset_sentry()

    #    def _reset_sentry(self):
    #        params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    #        if params.GetBool("Enable", True):
    #            dsn = params.GetString("DSN", "unset")
    #            FreeCAD.Console.PrintMessage(f"Resetting Sentry to use DSN {dsn}\n")
    #            init_sentry(dsn=dsn)
    #        else:
    #            FreeCAD.Console.PrintMessage(f"Deactivating Sentry (setting dsn=None)\n")
    #            init_sentry(dsn=None)

    def _data_removal_clicked(self):
        self.form.enable_check_box.setChecked(False)
        ok, message = self._remove_user_data()
        if ok:
            self.form.uuid_label.setText("unset")
            FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry").SetString(
                "PostHogUUID", "unset"
            )
        QtWidgets.QMessageBox.information(
            None,
            FreeCAD.Qt.translate("Telemetry", "Deletion request response"),
            message,
            QtWidgets.QMessageBox.Ok,
        )

    @staticmethod
    def _remove_user_data() -> (bool, str):
        uuid = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry").GetString(
            "PostHogUUID", "unset"
        )
        if uuid == "unset":
            return False, FreeCAD.Qt.translate(
                "Telemetry",
                "No UUID was found in your FreeCAD Telemetry settings, so there is no data to remove",
            )

        # Real error string
        error_string = FreeCAD.Qt.translate(
            "Telemetry",
            "There was a problem removing your user data: please contact telemetry@freecad.org to request removal of UUID {}",
        ).format(uuid)

        url = f"https://www.freecad.org/deletetelemetry.php?person_id={uuid}"
        req = urllib.request.Request(url, method="DELETE")
        try:
            with urllib.request.urlopen(req) as response:
                if 200 <= response.status < 300:
                    return True, FreeCAD.Qt.translate(
                        "Telemetry", "Your user data was successfully removed from the database."
                    )
                else:
                    FreeCAD.Console.PrintMessage(
                        f"Received a {response.status} response to our request\n"
                    )
                    FreeCAD.Console.PrintError(response.read() + "\n")
                    return False, error_string
        except urllib.request.HTTPError as e:
            FreeCAD.Console.PrintMessage(str(e) + "\n")
            return False, error_string
