import urllib.request
import re
import time

class Colors:
    def __init__(self):
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.bold = "\033[1m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"

ga = Colors()

class HTTP_HEADER:
    HOST = "Host"
    SERVER = "Server"

def headers_reader(url):
    # This function will print the server headers such as WebServer OS & Version.
    print(ga.bold + " \n [!] Fingerprinting the backend Technologies." + ga.end)
    try:
        opener = urllib.request.urlopen(url)
        if opener.getcode() == 200:
            print(ga.green + " [!] Status code: 200 OK" + ga.end)
        elif opener.getcode() == 404:
            print(ga.red + " [!] Page was not found! Please check the URL \n" + ga.end)
            exit()
        # Host = opener.headers.get(HTTP_HEADER.HOST)
        Server = opener.headers.get(HTTP_HEADER.SERVER)
        # HOST will split the HostName from the URL
        Host = url.split("/")[2]
        print(ga.green + " [!] Host: " + str(Host) + ga.end)
        print(ga.green + " [!] WebServer: " + str(Server) + ga.end)
        for item in opener.getheaders():
            for powered in item:
                sig = "x-powered-by"
                if sig in item:
                    print(ga.green + " [!] " + str(powered).strip() + ga.end)
    except Exception as e:
        print(ga.red + " [!] An error occurred:", str(e) + ga.end)

# Example usage:
url = "https://www.slavehack.com/"
headers_reader(url)
