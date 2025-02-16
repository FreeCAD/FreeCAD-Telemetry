# FreeCAD-Telemetry Privacy Policy

The FreeCAD-Telemetry Addon is an optional Addon for FreeCAD that collects anonymized usage information
using the [Sentry](https://sentry.io) telemetry service. That information is transmitted across the internet and
stored in a centralized database. The raw information is available only to FreeCAD Maintainers and Sentry system
administrators. Aggregate data is provided to the general public for the purpose of informing developers about how
FreeCAD is used so that their efforts may be focused on the most significant use-cases and problem areas.

Details about the data collected by Sentry are available here:
https://docs.sentry.io/platforms/python/data-management/data-collected/

This addon is configured to use Sentry with `send_default_pii=False` to minimize the data sent and to protect your
personal information.
