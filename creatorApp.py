import subprocess


def main():
    """Creator App
    """

    checkAdapterProperties = subprocess.run(["iw", "list"], stdout=subprocess.PIPE)
    checkAdapterPropertiesOut = str(checkAdapterProperties.stdout)
    hasAPCapabilities = checkAdapterPropertiesOut.find("* AP\n")
    
    print(hasAPCapabilities)

if __name__ == "__main__":
    main()