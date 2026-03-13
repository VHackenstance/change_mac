#/usr/bin/env python

import subprocess
import optparse
import re

def is_valid_mac(mac: str) -> bool:
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.fullmatch(pattern, mac))

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_option("-v", "--view", dest="view", help="enter True for View result")
    (opt, args) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info")
    is_valid = is_valid_mac(opt.new_mac)
    if not is_valid:
        parser.error("[-] Please use the correct syntax for the new MAC address [XX:XX:XX:XX:XX:XX]")
    return opt

def change_mac(interface, new_mac, view):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])

options = get_arguments()
change_mac(options.interface, options.new_mac, options.view)
