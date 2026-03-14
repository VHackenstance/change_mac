#/usr/bin/env python
import subprocess
import re

from helpers.utils import get_arguments, is_valid_mac

options = get_arguments(is_valid_mac)

# Change_mac simple algorithm TO Check if Mac address has changed
# Setups:
# We need to execute system commands and read the results
# 1. Execute and read ifconfig
print("Here is our interface *********** " + options.interface)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface], text=True)
print(ifconfig_result)

# 2. Read the MAC address from input, use Regex
mac_address_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)
print("This is the mac address our search has returned: " + mac_address_search_result.group(0))


# 3. Check if MAC in ifconfig is what the user requested
# 4. Print appropriate message
# change_mac(options.interface, options.new_mac, options.view)


