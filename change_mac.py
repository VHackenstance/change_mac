#/usr/bin/env python
from helpers.utils import get_arguments, is_valid_mac, change_mac, check_mac_address_updated, get_current_mac
from helpers.detect_os import get_os_name

# test changes
# Return the name of the OS so we know which way to proceed
get_os_name()
# Get the interface and new MAC values from the user.  Store them in options.
options = get_arguments(is_valid_mac)
# Update the MAC Address for the specified interface.
change_mac(options.interface, options.new_mac, options.view)
# Run a test to make sure the MAC Address has been updated: That the current address matches the requested one.
check_mac_address_updated(options, get_current_mac)


