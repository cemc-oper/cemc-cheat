try:
    from importlib.metadata import version

    __version__ = version("cemc-cheat")
except Exception:  # pragma: no cover
    __version__ = "unknown"
