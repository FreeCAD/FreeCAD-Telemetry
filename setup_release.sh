# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Telemetry addon.

# Install the cli
curl -sL https://sentry.io/get-cli/ | bash

# Setup configuration values
SENTRY_AUTH_TOKEN=$SENTRY_RELEASE_TOKEN
SENTRY_ORG=the-freecad-project-associatio
SENTRY_PROJECT=python
VERSION=`1.1.0dev`

# Workflow to create releases
sentry-cli releases new "$VERSION"
sentry-cli releases set-commits "$VERSION" --auto
sentry-cli releases finalize "$VERSION"
