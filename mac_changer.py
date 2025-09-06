#!/usr/bin/env python
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
    subprocess.call(["ifconfig",interface])
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw" , "ether", mac])
    subprocess.call(["ifconfig",interface, "up"])
options=get_arguments()
mac_changer(options.interface,options.mac)


