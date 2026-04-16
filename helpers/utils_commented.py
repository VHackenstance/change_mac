#/usr/bin/env python
import random
import string
import subprocess
import argparse
import re

# **1** Get the Interface and new MAC values from the User.
# Get a value from the user for the Interface.
# Get a value from the user for the new MAC address.
# Check the new MAC Address provided is in a valid format.
def get_arguments():
    # regex pattern to validate MAC Address
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
    # Check if the MAC Address is valid.  Uses an external function.
    is_valid = bool(re.search(mac_pattern, options.new_mac))
    if not is_valid:
        parser.error("[-] Please use the correct format for the new MAC Address [XX:XX:XX:XX:XX:XX]")
    return options

# **2** Update the MAC Address for the specified interface
# Update the MAC Address for the specified interface.
# Execute ifconfig if required to preview changes (redundant probably)
def change_mac(interface, new_mac, view):
    current_mac = get_current_mac(interface)
    print("\n[+] Changing MAC address for " + interface + " from " + current_mac + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])

# **3** Run a test to make sure the MAC Address has been updated:
# Check the MAC Address has been updated to the NEW MAC Address.
def check_mac_address_updated(options, get_mac):
    current_mac = get_mac(options.interface)
    # 3. Check if MAC in ifconfig is what the user requested
    if options.new_mac == current_mac:
        # 4. Print appropriate message
        print("\n[+] MAC Address successfully changed to: " + current_mac)
    else:
        print("No MAC Address update occurred")

# Return the MAC Address of a specified Interface
def get_current_mac(interface):
    # 1. Execute and read ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    # print(interface + " current ifconfig -- " + ifconfig_result)
    # 2. Read the MAC address from input, use Regex
    mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)
    if mac_address_search_result:
        current_mac = mac_address_search_result.group(0)
        return current_mac
    else:
        print("[-] Something went wrong. Could not read the MAC Address")
        return None

# Generate and return a random MAC Address in the format of Linux
def get_random_mac_address():
    hex_range = "02468ACE"
    # Get the hexdigits uppercased
    uppercase_hexdigits = "".join(set(string.hexdigits.upper()))
    # 2nd character must be 0, 2, 4, 6, 8, A, C or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice(hex_range)
            else:
                mac += random.choice(uppercase_hexdigits)
        mac += ":"
    return mac.strip(":")
