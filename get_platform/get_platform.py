import platform

def get_platform():
    sys_platform = platform.platform().lower()
    if "windows" in sys_platform:
        return "windows"
    elif "macos" in sys_platform:
        return "macos"
