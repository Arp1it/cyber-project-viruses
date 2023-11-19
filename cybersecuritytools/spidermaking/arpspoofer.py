from scapy.all import *
import sys
import time


def get_mac_address(ip_address):
    broadcast_layer = Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = ARP(pdst=ip_address)
    get_mac_packet = broadcast_layer/arp_layer
    answer = srp(get_mac_packet, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc

target_ip = str(sys.argv[2])
router_ip = str(sys.argv[1])

target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

print(router_mac)
print(target_mac)