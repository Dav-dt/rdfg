import os

def getDesktopPath() -> str:
    """
    Get desktop Path function.
    """
    return os.path.expanduser("~/Desktop")

def getDefaultOutputPath() -> str:
    """
    create default output path if not existing
    and returns name
    """
    default = getDesktopPath()+r"/RDFG_output"

    if not os.path.exists(default):
        os.makedirs(default)

    return default
