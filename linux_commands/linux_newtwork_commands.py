#/usr/bin/env python

network_connections = "watch ss -tp"
# -t: TCP sockets. -p: show process PID and name

tcp_connections = "netstat -ant"
tcp_connections_with_pid = "netstat -tulpn"
established_connections = "lsof -i"
established_connections_listening_ports = "lsof -nP -iTCP -sTCP:LISTEN"

# **** START **** Problematic, these are windows commands
# SMB (Server Message Block) Windows file sharing protocol
access_smb_share = "smb://<ip>/share"
mount_windows_share = "share user x.x.x.x c$"
smb_connect = "smbclient -U user \\\\<ip>\\<share>"
# **** END **** Problematic, these are windows commands

set_ip_and_netmask = "ifconfig eth# <ip>/<cidr>"
