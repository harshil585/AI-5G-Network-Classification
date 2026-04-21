from scapy.all import rdpcap, DNS, DNSQR, IP

def collect_dns_from_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    dns_map = {}

    for pkt in packets:
        if pkt.haslayer(DNS) and pkt.haslayer(DNSQR):
            ip = pkt[IP].src
            domain = pkt[DNSQR].qname.decode(errors="ignore")

            dns_map.setdefault(ip, set()).add(domain)

    return {ip: list(domains) for ip, domains in dns_map.items()}
