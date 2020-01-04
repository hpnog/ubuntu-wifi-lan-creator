#!/bin/sh

echo "Disconnecting from Hospot ubutntuWifiCreator connection"
nmcli c down ubutntuWifiCreator

echo "Removing ubutntuWifiCreator connection"
nmcli connection delete id ubutntuWifiCreator