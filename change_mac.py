#/usr/bin/env python

# from helpers.utils_single_function import mac_changer_single_function
# mac_changer_single_function()

from helpers.utils import (get_arguments, is_valid_mac, change_mac,
                           check_mac_address_updated, get_current_mac)

# Get the interface and new MAC values from the user.  Store them in options.
options = get_arguments(is_valid_mac)
# Update the MAC Address for the specified interface.
change_mac(options.interface, options.new_mac, options.view)
# Run a test to make sure the MAC Address has been updated: That the current address matches the requested one.
check_mac_address_updated(options, get_current_mac)


