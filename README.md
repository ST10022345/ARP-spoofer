# ARP-spoofer


This Python script performs ARP (Address Resolution Protocol) spoofing, a technique commonly used in Man-in-the-Middle attacks. The script sends falsified ARP responses to trick the target machines into associating the attacker's MAC address with the IP addresses of the legitimate devices.

# Prerequisites
Python must be installed on your machine.

Install the Scapy library using the following command:



pip install scapy
Usage
Open a terminal.

Navigate to the directory containing the script.

Run the script with the target and spoofed IP addresses:



python arp_spoof.py -t <target_ip> -s <spoof_ip>
Replace <target_ip> with the IP address of the target machine and <spoof_ip> with the IP address to which you want to spoof.

Options
-t, --target: Specify the target IP address.
-s, --spoof: Specify the IP address to which you want to spoof.
Example


python arp_spoof.py -t 192.168.1.2 -s 192.168.1.1
# Script Details
The script defines two functions, getMac and spoof, to retrieve MAC addresses and perform ARP spoofing, respectively.
The restore function is used to restore the ARP tables of the target and gateway machines.
The while True loop continuously sends ARP spoofing packets every 2 seconds until interrupted.
Note
The script must be run with root privileges (sudo) to manipulate ARP tables.

Ensure that IP forwarding is enabled on the attacker machine:



echo 1 > /proc/sys/net/ipv4/ip_forward
Disclaimer
This script is provided for educational purposes only. Misuse of this tool is illegal and may lead to severe consequences.

Author
Ethan Robinson

License
This project is licensed under the MIT License.