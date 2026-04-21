from dns_collector import collect_dns_from_pcap
from traffic_collector import collect_bandwidth_from_pcap

def collect_network_data(pcap_file):
    dns_data = collect_dns_from_pcap(pcap_file)
    bandwidth_data = collect_bandwidth_from_pcap(pcap_file)

    combined = {}

    for ip in set(dns_data.keys()).union(bandwidth_data.keys()):
        combined[ip] = {
            "domains": dns_data.get(ip, []),
            "bandwidth_kb": bandwidth_data.get(ip, 0)
        }

    return combined
