#/usr/bin/env python
import subprocess
import optparse
import re

def mac_changer_single_function(interface, new_mac, view):
    # Get values from the user for the Interface and a new MAC address.
    global current_mac
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    parser.add_option("-v", "--view", dest="view", help="enter True for View result")
    (opt, args) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info")

    # Check to see if a MAC Address has a valid format.
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    valid_mac = bool(re.search(pattern, opt.new_mac))
    if not valid_mac:
        parser.error("[-] Please use the correct format for the new MAC Address [XX:XX:XX:XX:XX:XX]")
    print(opt)

    # Update the MAC Address for the specified interface.
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])

    # Return the MAC Address of a specified Interface
    # 1. Execute and read ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    print(interface + " current ifconfig -- " + ifconfig_result)
    # 2. Read the MAC address from input, use Regex
    mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)

    if mac_address_search_result:
        current_mac = mac_address_search_result.group(0)
    else:
        print("[-] Something went wrong. Could not read the MAC Address")

    # Check the MAC Address has been updated to the NEW MAC Address.
    # 3. Check if MAC in ifconfig is what the user requested
    if current_mac == new_mac:
        print("MAC Address successfully changed to: " + current_mac)
    else:
        print("No MAC Address update occurred")