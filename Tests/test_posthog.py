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

import importlib
import unittest
from unittest.mock import patch, MagicMock
import mocks
import sys

from Tests.mocks import FreeCADMock


class PosthogFCTest(unittest.TestCase):

    def setUp(self):
        """On setup, ensure the real imports are never executed."""
        self.fc = FreeCADMock()
        self.fcg = MagicMock()
        self.ph = MagicMock()

        self.fc_patch = unittest.mock.patch.dict("sys.modules", {"FreeCAD": self.fc})
        self.fc_patch.start()

        self.fcg_patch = unittest.mock.patch.dict("sys.modules", {"FreeCADGui": self.fcg})
        self.fcg_patch.start()

        self.posthog_patch = unittest.mock.patch.dict("sys.modules", {"posthog": self.ph})
        self.posthog_patch.start()

    def tearDown(self):
        self.fc_patch.stop()
        self.fcg_patch.stop()
        self.posthog_patch.stop()
        sys.modules.pop("FreeCAD", None)
        sys.modules.pop("FreeCADGui", None)
        sys.modules.pop("posthog", None)

    def test_posthog_launch_addon_disabled(self):
        """Ensure that when disabled no calls to posthog are made"""
        self.fc.add_parameter_dict(
            "User parameter:BaseApp/Preferences/Mod/Telemetry", {"Enabled": False}
        )
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            MockPosthog.assert_not_called()
            instance = MockPosthog.return_value
            instance.capture.assert_not_called()

    def test_posthog_launch_addon_enabled(self):
        """Ensure that when enabled, calls to posthog are made"""
        self.fc.add_parameter_dict(
            "User parameter:BaseApp/Preferences/Mod/Telemetry", {"Enabled": True}
        )
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            MockPosthog.assert_called()
            instance = MockPosthog.return_value
            instance.capture.assert_called()

    def test_posthog_all_info_sent_by_default(self):
        """Ensure that with defaults used, all info is sent"""
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            instance = MockPosthog.return_value
            args = instance.capture.call_args_list
            expected_events = [
                "freecad_startup",
                "freecad_version",
                "freecad_system_info",
                "freecad_preferences",
                "freecad_addon_list",
            ]
            for arg in args:
                self.assertIn("event", arg.kwargs)
                self.assertIn(arg.kwargs["event"], expected_events)
                expected_events.remove(
                    arg.kwargs["event"]
                )  # Mark it as seen by removing it from the list
            self.assertEqual(
                len(expected_events), 0
            )  # If we saw them all, then there is nothing left

    def test_posthog_sysinfo_not_sent_if_disabled(self):
        self.fc.add_parameter_dict(
            "User parameter:BaseApp/Preferences/Mod/Telemetry", {"SendSystemInformation": False}
        )
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            instance = MockPosthog.return_value
            args = instance.capture.call_args_list
            for arg in args:
                self.assertIn("event", arg.kwargs)
                self.assertNotEqual(arg.kwargs["event"], "freecad_system_info")

    def test_posthog_addons_not_sent_if_disabled(self):
        self.fc.add_parameter_dict(
            "User parameter:BaseApp/Preferences/Mod/Telemetry", {"SendAddonInformation": False}
        )
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            instance = MockPosthog.return_value
            args = instance.capture.call_args_list
            for arg in args:
                self.assertIn("event", arg.kwargs)
                self.assertNotEqual(arg.kwargs["event"], "freecad_addon_list")

    def test_posthog_preferences_not_sent_if_disabled(self):
        self.fc.add_parameter_dict(
            "User parameter:BaseApp/Preferences/Mod/Telemetry", {"SendPreferences": False}
        )
        with patch("posthog.Posthog") as MockPosthog:
            import PosthogFC

            PosthogFC.posthog_launch()
            instance = MockPosthog.return_value
            args = instance.capture.call_args_list
            for arg in args:
                self.assertIn("event", arg.kwargs)
                self.assertNotEqual(arg.kwargs["event"], "freecad_preferences")
