#!/usr/bin/env python
import re
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change mac address")
    parser.add_option("-m","--mac",dest="mac",help="mac address to change")
    (options,args)=parser.parse_args()
    return options
def mac_changer(interface,mac):
    print("changing mac address")
    # subprocess.call(["ifconfig",interface])
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw" , "ether", mac])
    subprocess.call(["ifconfig",interface, "up"])
def get_current_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig",interface])
    mac_add_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_results))
    if mac_add_search:
        return mac_add_search.group(0)
    else:
        print("cound not read mac address")
options=get_arguments()
cur_mac=get_current_mac(options.interface)  #here value will be the current address
print(">current mac add is : "+ cur_mac)
mac_changer(options.interface,options.mac)
cur_mac=get_current_mac(options.interface)  #here value of cur_mac is changed if above func works properly
if cur_mac == options.mac:
    print("mac address changed to : "+cur_mac)
else:
    print("mac address not changed")

