from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP

def show_packet(packet):
    print("\n--- Packet Captured ---")
    print("Protocol layers:", packet.summary())

    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
    elif IPv6 in packet:
        print("Source IPv6:", packet[IPv6].src)
        print("Destination IPv6:", packet[IPv6].dst)

    if TCP in packet:
        print("Protocol: TCP")
    elif UDP in packet:
        print("Protocol: UDP")
    elif ICMP in packet:
        print("Protocol: ICMP")

print("Basic Network Sniffer Started")
print("Capturing 10 packets...")

sniff(count=10, prn=show_packet)

print("\nSniffing stopped. Total packets captured: 10")