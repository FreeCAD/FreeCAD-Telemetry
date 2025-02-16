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
from Sentry import init_sentry

def setup():
    global init_sentry
    params = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")
    default_dsn = "https://ff3b28f395e6df9ba8fc4c34e03ffdc7@o4508819774963712.ingest.de.sentry.io/4508819779944528"
    dsn = params.GetString("DSN", default_dsn)

    init_sentry(dsn=dsn)

setup()
