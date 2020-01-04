#!/bin/sh

echo "Starting Create script"

if [ $# != 3 ]
    then
        echo "No correct arguments supplied..."
        echo "Expected: \$1 = <Wi-Fi device to use> | \$2 = <SSID name> | \$3 = <Networks password>"
        exit 1
    else
        echo "Arguments received"
fi

echo "Removing ubuntuWifiCreator connection (if any exists)"
nmcli connection delete ubuntuWifiCreator

# wifi hotspot [ifname ifname] [con-name name] [ssid SSID] [band {a | bg}] [channel channel] [password password]

# Wifi Hotspot 
#  Create a Wi-Fi hotspot. The command creates a hotspot connection profile according to
#  Wi-Fi device capabilities and activates it on the device. The hotspot is secured with
#  WPA if device/driver supports that, otherwise WEP is used. Use connection down or
#  device disconnect to stop the hotspot

# ifname
#  what Wi-Fi device is used
# con-name
#  name of the created hotspot connection profile
# ssid
#  SSID of the hotspot
# password
#  password to use for the created hotspot. The password is either WPA pre-shared key or WEP key

nmcli dev wifi hotspot ifname $1 con-name "ubuntuWifiCreator" ssid $2 password "$3" --show-secrets

echo "Network Created - ubuntuWifiCreator"

echo "Changing network mode to ap"
nmcli connection modify ubuntuWifiCreator 802-11-wireless.mode ap
echo "Configuration done"

exit 0