#/usr/bin/env python

from helpers.utils import (
    get_arguments, change_mac,
    check_mac_address_updated, get_current_mac)

# **1** Get the Interface and new MAC values from the User.
options = get_arguments()
# **2** Update the MAC Address for the specified interface.
change_mac(options.interface, options.new_mac, options.view)
# **3** Run a test to make sure the MAC Address has been updated:
check_mac_address_updated(options, get_current_mac)


