import subprocess
import sys

def addScriptsPermissions():
    print("Adding script Permissions")
    subprocess.run(["chmod", "+x", "./shScripts/create.sh"])
    subprocess.run(["chmod", "+x", "./shScripts/disconnectAndRemove.sh"])
    print("Script Permissions set")
    return

def hasAPCapabilities() -> bool:
    # cmd to show manipulate wireless devices and their configuration
    checkAdapterProperties = subprocess.run(["iw", "list"], stdout=subprocess.PIPE)

    checkAdapterPropertiesOut = str(checkAdapterProperties.stdout)

    # Find if the AP configuration exists
    hasAP = checkAdapterPropertiesOut.find("* AP\\n") != -1
    return hasAP

def getWifiDevice() -> str:
    # Get adapter information
    getAdapters = subprocess.run(["nmcli", "d"], stdout=subprocess.PIPE)

    # Returns a table with the first line being the header
    getAdaptersOut = str(getAdapters.stdout).split("\\n")
    for line in getAdaptersOut:
        if line.find("wifi") != -1:
            return line.split(" ")[0]
    return ""

def requestUserInput() -> {}:
    res = {}

    print("Please enter a valid SSID for your Network:")
    SSID = input()
    res["ssid"] = SSID
    print("Please enter a valid password for your Network:")
    pw = input()
    res["password"] = pw
    return res

def removeNetworkIfExistant() -> str:
    res = subprocess.run(["./shScripts/disconnectAndRemove.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return str(res.stdout)

def attemptConnection():
    print("Attempting new connection")

    # Command to connect to the specified network
    res = subprocess.run(["nmcli", "c", "up", "ubuntuWifiCreator"], stdout=subprocess.PIPE)

    # If the connection was not successfull, it is to be removed
    if res.returncode != 0:
        print("An error has occured while connecting...")
        print("Canceling and removing network")
        removeNetworkIfExistant()
        return -1
    return 0
    
def createNetwork() -> int:
    res = 0
    if not hasAPCapabilities():
        print("Network adapter with support for the \"AP\" interface mode not detected.")
        print("Exiting")
        return -1
    print("Network adapter with support for the \"AP\" interface mode detected.")

    # Make sure that the wifi radio is on
    subprocess.run(["nmcli", "r", "wifi", "on"], stdout=subprocess.PIPE)

    wifiDevice = getWifiDevice()
    if wifiDevice == "":
        print("Wifi device not detected")
        print("Exiting")
    else:
        print("Wifi device found: " + wifiDevice)
    input = requestUserInput()
    removeNetworkIfExistant()
    subprocess.call(["./shScripts/create.sh", wifiDevice, input["ssid"], input["password"]])
    res = attemptConnection()

    if res == 0:
        print("Creation ended")
        return 0
    else:
        print("Creation not finished")
        return -1

def main(argv):
    """Creator App
    """
    res = 0
    if len(argv) != 1 or argv[0] not in ["-create", "-remove"]:
        print("Wrong argument input")
        print("Expected ARGS: -create OR -remove")
        return -1

    addScriptsPermissions()

    # Handle user arguments
    if argv[0] == "-create":
        res = createNetwork()
    elif argv[0] == "-remove":
        string = removeNetworkIfExistant().split("\\n")
        for line in string:
            print("Script stdout:" + line)
    
    if res == 0:
        print("Ended successfuly")
    else:
        print("Ended with Errors")
    return res

if __name__ == "__main__":
    main(sys.argv[1:])