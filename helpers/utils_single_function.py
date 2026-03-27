#/usr/bin/env python
import subprocess
import argparse
import re

def mac_changer_single_function():
    global current_mac
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_argument("-v", "--view", dest="view", help="enter True for View result")
    (opt, args) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info")
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    valid_mac = bool(re.search(pattern, opt.new_mac))
    if not valid_mac:
        parser.error("[-] Please use the correct format for the new MAC Address [XX:XX:XX:XX:XX:XX]")
    print(opt)
    interface = opt.interface
    new_mac = opt.new_mac
    view = opt.view
    print("\n[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    # print(interface + " current ifconfig -- " + ifconfig_result)
    mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)
    if mac_address_search_result:
        current_mac = mac_address_search_result.group(0)
    else:
        print("[-] Something went wrong. Could not read the MAC Address")
    if current_mac == new_mac:
        print("\n[+] MAC Address successfully changed to: " + current_mac)
    else:
        print("No MAC Address update occurred")