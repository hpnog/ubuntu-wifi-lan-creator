#!/bin/sh

# Make sure that the wifi radio is on
nmcli r wifi on

# Determine the name if the network interface
nmcli d

# Determine the name if the Wifi network interface
nmcli d wifi list

# The following command would connect to <networkName> using <password>
# nmcli d wifi connect <networkName> password <password>
