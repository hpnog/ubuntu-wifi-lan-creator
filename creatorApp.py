import subprocess

def addScriptsPermissions():
    print("Adding script Permissions")
    subprocess.run(["chmod", "+x", "./shScripts/create.sh"])
    subprocess.run(["chmod", "+x", "./shScripts/disconnectAndRemove.sh"])
    print(" Script Permissions set")

    return

def hasAPCapabilities() -> bool:
    checkAdapterProperties = subprocess.run(["iw", "list"], stdout=subprocess.PIPE)
    checkAdapterPropertiesOut = str(checkAdapterProperties.stdout)
    hasAP = checkAdapterPropertiesOut.find("* AP\\n") != -1
    return hasAP

def getWifiDevice() -> str:
    
    getAdapters = subprocess.run(["nmcli", "d"], stdout=subprocess.PIPE)
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

def attemptConnection():
    print("Attempting new connection")
    res = subprocess.run(["nmcli", "c", "up", "ubuntuWifiCreator"], stdout=subprocess.PIPE)
    print(res.stdout)
    print(res)

def main():
    """Creator App
    """
    addScriptsPermissions()

    if not hasAPCapabilities():
        print("Network adapter with support for the \"AP\" interface mode not detected.")
        print("Exiting")
        # return -1
    print("Network adapter with support for the \"AP\" interface mode detected.")

    subprocess.run(["nmcli", "r", "wifi", "on"], stdout=subprocess.PIPE)
    wifiDevice = getWifiDevice()
    if wifiDevice == "":
        print("Wifi device not detected")
        print("Exiting")
    else:
        print("Wifi device found: " + wifiDevice)

    input = requestUserInput()

    subprocess.call(["./shScripts/create.sh", wifiDevice, input["ssid"], input["password"]])

    attemptConnection()

    return 0

if __name__ == "__main__":
    main()