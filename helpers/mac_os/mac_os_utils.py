#/usr/bin/env python
import subprocess

def change_mac_macos(interface, new_mac, view):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "ether", new_mac])
    if view: subprocess.call(["ifconfig", interface])