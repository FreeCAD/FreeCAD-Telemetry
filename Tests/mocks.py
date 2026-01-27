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

"""Mocks for unit-testing the Telemetry Addon outside of FreeCAD, or without interaction with
FreeCAD (e.g. it won't actually change any user preferences, and doesn't matter that they are
set to.)"""

from unittest.mock import MagicMock


class ParameterMock:
    """A minimal, fully self-contained mock of FreeCAD's parameter group"""

    def __init__(self, param_dict=None):
        super().__init__()
        if param_dict is None:
            self.param_dict = {}
        else:
            self.param_dict = param_dict

    def GetBool(self, key: str, default: bool) -> bool:
        return self._get(key, default)

    def GetString(self, key: str, default: str) -> str:
        return self._get(key, default)

    def GetInt(self, key: str, default: int) -> int:
        return self._get(key, default)

    def SetBool(self, key: str, value: bool):
        self.param_dict[key] = value

    def SetString(self, key: str, value: str):
        self.param_dict[key] = value

    def SetInt(self, key: str, value: int):
        self.param_dict[key] = value

    def _get(self, key: str, default):
        if key in self.param_dict:
            return self.param_dict[key]
        return default


class FreeCADMock(MagicMock):
    """A minimal mock of FreeCAD that allows the creation of parameter groups that can be manipulated
    the same way real ones can (minus any interaction with FreeCAD's actual parameter system)."""

    def __init__(self):
        super().__init__()
        self.param_dicts = {}
        self.Console = MagicMock()

    def add_parameter_dict(self, group_name: str, param_dict):
        self.param_dicts[group_name] = param_dict

    def Version(self):
        return ["1", "2", "3", "", "", "", "main"]

    def ParamGet(self, group_name: str):
        if group_name in self.param_dicts:
            return ParameterMock(self.param_dicts[group_name])
        else:
            return ParameterMock()

    def getUserAppDataDir(self):
        return "/Some/Fake/Path/"
