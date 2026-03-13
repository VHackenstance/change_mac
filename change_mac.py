#/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_option("-v", "--view", dest="view", help="enter True for View result")
    (opt, args) = parser.parse_args()
    return opt

def change_mac(interface, new_mac, view):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])

options = get_arguments()
change_mac(options.interface, options.new_mac, options.view)