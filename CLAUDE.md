# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The FreeCAD **Telemetry** addon: an optional FreeCAD workbench (pure Python, no C++) that sends
non-identifying usage metrics to PostHog. It is installed into `{userAppDataDir}/Mod/Telemetry` and
loaded by FreeCAD at startup. It is not a real workbench — the `Telemetry` class in `InitGui.py` is an
empty shell that exists only so FreeCAD will load the addon; all work happens at import time.

`README.md` and `PRIVACY_POLICY.md` are user-facing contracts about exactly what data is collected.
**Any change that adds a new collected field must be reflected in both**, per the project's stated
promise that no data is added to the collection list without informing the user.

## Commands

```bash
# Install dev deps (hash-pinned; same set CI installs)
pip install --require-hashes -r requirements.txt

# Run all tests (must be run from the repo root)
python -m unittest discover Tests

# Run a single test — note: plain `python -m unittest Tests.test_posthog...` FAILS because
# Tests/test_posthog.py does `import mocks`, which needs Tests/ on sys.path (discover adds it).
python -m unittest discover Tests -k test_posthog_launch_addon_enabled

# Formatting (enforced by pre-commit / pre-commit.ci)
black --line-length 100 .
pre-commit run --all-files

# Security lint (enforced by .github/workflows/bandit.yml; same config as FreeCAD/Addon-Reports).
# Must report zero issues. Fix findings, or add `# nosec BXXX` preceded by an
# `# Audited: <why it is safe> (added nosec BXXX)` comment, as the AddonManager does.
pip install bandit
bandit -c bandit.yaml -r .
```

Dependency pinning: edit `requirements.in` (currently just `posthog`), then regenerate with
`pip-compile --generate-hashes`. Dependabot bumps `requirements.txt` automatically.

Translations: see `Resources/translations/README.md`. `update_translation.sh -U` regenerates the
`.ts` template from `../../*.py ../panels/*.ui`; `run_translation_cycle.py` drives the full CrowdIn
round-trip. `update_translation.sh` hardcodes Windows Qt paths for `lupdate`/`lrelease` — override
`LUPDATE`/`LRELEASE` in the script for your system.

## Architecture

Load order is dictated by FreeCAD, not by us:

- `Init.py` — console/non-GUI startup. Currently a no-op: the Sentry crash-reporting path
  (`setup_sentry()` and the `Sentry.py` import) is deliberately commented out and unused.
- `InitGui.py` — GUI startup, the real entry point. Runs `setup()` at import time, which:
  registers the preference page, shows the `first_start.ui` consent dialog on first run (writing the
  four opt-in params), calls `posthog_launch()`, and wires `posthog_shutdown` to Qt's `aboutToQuit`.
  The shutdown event is what lets the project infer crash rates (startup without matching shutdown).
- `PosthogFC.py` — all event capture. Five events: `freecad_startup`, `freecad_version`,
  `freecad_system_info`, `freecad_preferences`, `freecad_addon_list`, plus `freecad_shutdown`.
  Module-global `posthog` client and `posthog_id`.
- `TelemetryPreferences.py` — the preference page class (FreeCAD calls `loadSettings`/`saveSettings`
  by name), plus the GDPR data-removal button which DELETEs
  `https://www.freecad.org/deletetelemetry.php?person_id={uuid}`.
- `TelemetryPaths.py` — path constants for `Resources/{icons,panels,translations}`.
- `Sentry.py` — dormant. Kept for planned crash reporting; every call site is commented out.

### State lives in FreeCAD's parameter system

There is no config file. Everything is read/written through
`FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Telemetry")`:
`Enable`, `SendSystemInformation`, `SendAddonInformation`, `SendPreferences`, `FirstStart`,
`PostHogUUID` (the random per-install identity), `PostHogURL`, `PostHogAPIKey`, `DSN`, `LastSendTime`.
Defaults are inlined at each call site rather than centralized, so a default changed in one file must
be changed in all of them.

Gotcha: `InitGui.py` and `TelemetryPreferences.py` use the key **`Enable`**, while
`PosthogFC.posthog_launch()`/`posthog_shutdown()` check **`Enabled`** — a key the UI never writes, so
that inner check always falls through to its `True` default. The effective kill switch is the
`Enable` check in `InitGui.setup_posthog()`. Don't "fix" one side in isolation; changing the key
silently changes opt-out behavior for existing users.

### Reading tracked preferences

`posthog_preferences()` reads *FreeCAD's own* preferences (not the addon's) through the
`TrackedPreference` helpers in `PosthogFC.py`, which take a full `Group/Path/Name` string, a type, a
default, and an optional `transform`. `ui_panel_preferences()` additionally scans the
`BaseApp/MainWindow/DockWindows/Overlay{Left,Right,Top,Bottom}` groups to work out where a dock panel
is placed. Add new tracked preferences as entries in the `preferences` dict, not as new events.

## Testing

`Tests/mocks.py` provides `FreeCADMock` (a `MagicMock` subclass with a working `ParamGet`/parameter
dict) and `ParameterMock`. Tests never touch a real FreeCAD. The pattern in `Tests/test_posthog.py`:
patch `sys.modules` for `FreeCAD`, `FreeCADGui`, and `posthog` in `setUp`, pop them in `tearDown`,
then `import PosthogFC` *inside* the test body — the module raises on import outside FreeCAD, so the
import must happen after the patches are live. Seed behavior with
`self.fc.add_parameter_dict("User parameter:BaseApp/Preferences/Mod/Telemetry", {...})` and assert
against `MockPosthog.return_value.capture.call_args_list`.

## Conventions

- Black, line length 100.
- Every source file carries the SPDX header and the FPA LGPL-2.1-or-later boilerplate block; copy it
  into new files.
- User-visible strings go through `FreeCAD.Qt.translate("Telemetry", ...)` so CrowdIn picks them up.
- Bump `<version>` and `<date>` in `package.xml` for a release; the Addon Manager reads it.
