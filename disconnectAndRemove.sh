#!/bin/sh

echo "Disconnecting from Hospot ubuntuWifiCreator connection"
nmcli c down ubuntuWifiCreator

echo "Removing ubuntuWifiCreator connection"
nmcli connection delete ubuntuWifiCreator