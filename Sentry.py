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
    import sentry_sdk
except ImportError as e:
    raise ImportError("Sentry SDK is not installed") from e

try:
    import FreeCAD
except ImportError as e:
    raise RuntimeError("This is a FreeCAD Addon, and should be run from within FreeCAD") from e

def before_send(event, _):
    FreeCAD.Console.PrintMessage(f"Sending event to Sentry: {event}\n")
    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enable", False)
    if not enabled:
        FreeCAD.Console.PrintMessage("  -> Send blocked because Telemetry is disabled\n")
        return None  # Drop the event
    return event

def init_sentry(dsn):
    global sentry_sdk
    global before_send

    release = FreeCAD.Version()

    if release[6] and release[6] != "main":
        FreeCAD.Console.PrintMessage("FreeCAD Telemetry addon disabled: not on main branch\n")
        FreeCAD.Console.PrintMessage(f"FreeCAD branch: {release[6]}\n")
        return

    major = release[0]
    minor = release[1]
    patch = release[2]
    rev = release[3]
    version_string = f"FreeCAD@{major}.{minor}.{patch}"

    if minor == 0:
        # TODO(chennes): Currently hardcoded for FreeCAD 1.0
        environment = "production"
    else:
        environment = "development"
        version_string += "dev"

    sentry_sdk.init(
        dsn=dsn,
        send_default_pii=False,
        release=version_string,
        environment=environment,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        before_send=before_send,
    )

    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    enabled = params.GetBool("Enable", False)
    if not enabled:
        FreeCAD.Console.PrintMessage("Sentry initialized, but FreeCAD Telemetry sending is disabled: no data will be transmitted\n")
    else:
        FreeCAD.Console.PrintMessage("Sentry initialized. FreeCAD Telemetry sending is active.\n")
