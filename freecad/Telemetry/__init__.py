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


from FreeCAD import Console, ParamGet

# from .Sentry import init_sentry


def setup_sentry():
    global init_sentry
    global close_sentry_session
    params = ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    dsn = params.GetString("DSN", "unset")
    if dsn == "unset":
        dsn = "https://ff3b28f395e6df9ba8fc4c34e03ffdc7@o4508819774963712.ingest.de.sentry.io/4508819779944528"
        params.SetString("DSN", dsn)

    enabled = params.GetBool("Enable", True)
    if not enabled:
        Console.PrintLog(
            "Sentry initializing, but FreeCAD Telemetry sending is disabled: no data will be transmitted\n"
        )
        dsn = None
    else:
        Console.PrintLog("Sentry initializing. FreeCAD Telemetry sending is active.\n")
    # init_sentry(dsn=dsn)


# Currently not using Sentry
# setup_sentry()
