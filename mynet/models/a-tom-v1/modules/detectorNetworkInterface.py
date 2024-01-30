#! _*_ encoding: utf-8 _*_
import os
from colors import *

def detectar_interfaces():
    if os.name == 'posix':  # Linux
        interfaces = os.listdir('/sys/class/net/')
    elif os.name == 'nt':  # Windows
        interfaces = [interface.strip() for interface in os.popen('wmic nic get NetConnectionID').read().split('\n') if interface.strip()]
    else:
        interfaces = []
    return interfaces

global ifaces
ifaces = detectar_interfaces()
print("*"*20) 
print("NETWORKING INTERFACES")
print("*"*20)

for iface in ifaces:
    print(f"Interface : {iface}")

