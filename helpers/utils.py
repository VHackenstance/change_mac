#/usr/bin/env python
import random
import string
import subprocess
import argparse
import re

def get_arguments():
    mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_argument("-v", "--view", dest="view", help="enter True for View result")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info")
    is_valid = bool(re.search(mac_pattern, options.new_mac)) # check valid MAC address
    if not is_valid:
        parser.error("[-] Please use the correct format for the new MAC Address [XX:XX:XX:XX:XX:XX]")
    return options

def change_mac(interface, new_mac, view):
    current_mac = get_current_mac(interface)
    print("\n[+] Changing MAC address for " + interface + " from " + current_mac + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])

def check_mac_address_updated(options, get_mac):
    current_mac = get_mac(options.interface)
    if options.new_mac == current_mac:
        print("\n[+] MAC Address successfully changed to: " + current_mac)
    else:
        print("No MAC Address update occurred")

def get_current_mac(interface):
    mac_pattern2 = "r\"(\w\w:){5}(\w\w)\""
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(mac_pattern2, ifconfig_result)
    if mac_address_search_result:
        current_mac = mac_address_search_result.group(0)
        return current_mac
    else:
        print("[-] Something went wrong. Could not read the MAC Address")
        return None

def get_random_mac_address():
    hex_range = "02468ACE"
    uppercase_hexdigits = "".join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice(hex_range)
            else:
                mac += random.choice(uppercase_hexdigits)
        mac += ":"
    return mac.strip(":")



































