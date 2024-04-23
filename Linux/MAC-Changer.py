# You have to be root to run this script

import subprocess

interface = input("Enter interface:")
MACaddr = input("New MAC address:")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {MACaddr}", shell=True)  # Fixed the closing curly brace
subprocess.call(f"ifconfig {interface} up", shell=True)
print(f"MAC address of {interface} has been changed to {MACaddr}.")
subprocess.call(f"ifconfig {interface}", shell=True)
