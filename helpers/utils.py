#/usr/bin/env python
import subprocess
import optparse
import re

# Check to see if a MAC Address has a valid format.
def is_valid_mac(mac):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.search(pattern, mac))

# Return the MAC Address of a specified Interface
def get_current_mac(interface):
    # 1. Execute and read ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    print("Here is our current ifconfig for " + interface + " " + ifconfig_result)
    # 2. Read the MAC address from input, use Regex
    mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)
    if mac_address_search_result:
        current_mac = mac_address_search_result.group(0)
        return current_mac
    else:
        print("[-] Something went wrong. Could not read the MAC Address")
        return None

# Check the MAC Address has been updated to the NEW MAC Address.
def check_mac_address_updated(options, get_mac):
    current_mac = get_mac(options.interface)
    # 3. Check if MAC in ifconfig is what the user requested
    if options.new_mac == current_mac:
    # 4. Print appropriate message
        print("MAC Address successfully changed to: " + current_mac)
    else:
        print("No MAC Address update occurred")

# Get a value from the user for the Interface.
# Get a value from the user for the new MAC address.
# Check the new MAC Address provided is in a valid format.
def get_arguments(is_valid_new):
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_option("-v", "--view", dest="view", help="enter True for View result")
    (opt, args) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info")
    # Check if the MAC Address is valid.  Uses an external function.
    is_valid = is_valid_new(opt.new_mac)
    if not is_valid:
        parser.error("[-] Please use the correct format for the new MAC Address [XX:XX:XX:XX:XX:XX]")
    return opt

# Update the MAC Address for the specified interface.
# Execute ifconfig if required to preview changes (redundant probably)
def change_mac(interface, new_mac, view):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])