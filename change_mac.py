#/usr/bin/env python

from helpers.utils import get_arguments, change_mac

# Change_mac simple algorithm
# Check if Mac address has changed
# Setups:
# 1. Execute and read ifconfig
# 2. Read the MAC address from input
# 3. Check if MAC in ifconfig is what the user requested
# 4. Print appropriate message

options = get_arguments()
change_mac(options.interface, options.new_mac, options.view)
