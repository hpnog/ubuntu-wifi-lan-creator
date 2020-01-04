# Ubuntu Wifi Lan Creater

## Summary

This is a small app written in Python and Shell scripts that quicky configured a Wifi lan connection from your Linux terminal.

### Usage

I Wrote this small tool myself for personal use. I would sometimes need to setup a simple Wireless Local Network and always needed to setup each different configuration. With this tool I simply need to run it.
It has only been testes in a very small number of machines so, if you find any problems, please feel free to share in this repository!

## Some requirements exist:

 * Python (tested woth version 3.6.9);
 * Network adapter with **AP** interface mode;
   * The script detects if none exists;
 * Uses **nmcli** — command-line tool for controlling NetworkManager.

## How to use

 * Clone the repository;
 * Navigate to the repositorys folder;
 * Choose to **Create** or **Remove** the network;
 1. To **create** a network:
   
 ```shell
 python3 creatorApp.py -create
 ```

 * To **remove** a network:
 ```shell
 python3 creatorApp.py -remove
 ```