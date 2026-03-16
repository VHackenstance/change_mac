#/usr/bin/env python

import platform

def get_os_name():
    os_name = platform.system().lower()
    print(f"Operating System: {os_name}")
    # Check for specific OS
    if os_name == "windows":
        print("Running on Windows")
    elif os_name == "linux":
        print("Running on Linux")
    elif os_name == "darwin":
        print("Running on macOS")
    else:
        print("Unknown OS")