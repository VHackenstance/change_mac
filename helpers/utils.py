import subprocess
import optparse
import re

def is_valid_mac(mac: str) -> bool:
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.fullmatch(pattern, mac))

def get_current_mac(interface):
    # 1. Execute and read ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface], text=True)
    print("Here is our current ifconfig for " + interface + " " + ifconfig_result)
    # 2. Read the MAC address from input, use Regex
    mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)
    current_mac = mac_address_search_result.group(0)
    return current_mac

def check_mac_address_updated(options, get_mac) -> str:
    current_mac = get_mac(options.interface)
    # 3. Check if MAC in ifconfig is what the user requested
    if options.new_mac == current_mac:
        # 4. Print appropriate message
        print("Requested MAC: " + options.new_mac + ". Current MAC Address: " + current_mac)
        print("MAC Address successfully updated to new MAC")
    else:
        print("No MAC Address update occurred")

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
    is_valid = is_valid_new(opt.new_mac)
    if not is_valid:
        parser.error("[-] Please use the correct syntax for the new MAC address [XX:XX:XX:XX:XX:XX]")
    return opt

def change_mac(interface: str, new_mac: str, view: bool):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    if view: subprocess.call(["ifconfig", interface])