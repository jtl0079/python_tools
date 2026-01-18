import socket

from python_tools.core.network.primitive import mac_to_hex_string


def wake_on_lan(mac):
    
    mac = mac_to_hex_string(mac)
    data = "FF" * 6 + mac * 16
    packet = bytes.fromhex(data)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(packet, ("255.255.255.255", 9))
    s.close()


