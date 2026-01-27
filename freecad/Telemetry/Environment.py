try:
    import FreeCAD
    import FreeCADGui
except ImportError as e:
    raise RuntimeError("This is a FreeCAD Addon, and should be run from within FreeCAD") from e

try:
    import posthog
except ImportError as e:
    raise ImportError("Posthog Python package is not installed: pip install posthog") from e
