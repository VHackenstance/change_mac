#/usr/bin/env python
import subprocess
import os

def check_winget_installed():
    result = os.system("winget --version >nul 2>&1" )
    if result == 0:
        print("Winget is installed we can continue")
    else:
        print("Winget is not installed. Please install to continue.")
        exit(1)

def change_mac_windows10(interface_number, new_mac, view):
    print("[+] Changing MAC address for " + interface_number + " to " + new_mac)
    # View current mac
    subprocess.call(["getmac"])
    # Install ChMac
    subprocess.call(["winget", "install", "-e", "--id", "wandersick.ChMac"])
    # update network adapter #number with new mac address: xx-XX-xx-XX-xx-XX
    subprocess.call(["chmac", "/m", new_mac, "/n", interface_number])
    if view: subprocess.call(["getmac"])