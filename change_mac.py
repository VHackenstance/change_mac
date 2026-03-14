#/usr/bin/env python

from helpers.utils import get_arguments, is_valid_mac, change_mac, check_mac_address_updated, get_current_mac

options = get_arguments(is_valid_mac)
change_mac(options.interface, options.new_mac, options.view)
check_mac_address_updated(options, get_current_mac)


