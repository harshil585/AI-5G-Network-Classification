from scapy.all import rdpcap, IP

def collect_bandwidth_from_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    traffic = {}

    for pkt in packets:
        if pkt.haslayer(IP):
            ip = pkt[IP].src
            size = len(pkt)  # bytes

            traffic[ip] = traffic.get(ip, 0) + size

    # Convert to kbps (approximation)
    for ip in traffic:
        traffic[ip] = traffic[ip] / 1024  # KB

    return traffic
