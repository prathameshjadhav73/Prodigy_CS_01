from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            protocol_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol_name = "Other"
            src_port = "N/A"
            dst_port = "N/A"

        print(f"IP {ip_src} -> {ip_dst} | Protocol: {protocol_name} | Src Port: {src_port} | Dst Port: {dst_port}")

# Start sniffing
sniff(prn=packet_callback, filter="ip", store=0)
