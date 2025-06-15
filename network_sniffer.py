from scapy.all import sniff, IP

# Function to process each packet
def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] Packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

# Sniff packets
print("[*] Starting packet sniffing...")
sniff(prn=process_packet, count=20)  # Captures 20 packets (can remove count for continuous)
