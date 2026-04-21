from scapy.all import rdpcap, IP, TCP, UDP
import csv

def extract_flows(pcap_file, output_csv):
    packets = rdpcap(pcap_file)

    flows = {}

    for pkt in packets:
        if not pkt.haslayer(IP):
            continue

        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = "TCP" if pkt.haslayer(TCP) else "UDP" if pkt.haslayer(UDP) else "OTHER"

        key = (src, dst, proto)

        if key not in flows:
            flows[key] = {
                "spkts": 0,
                "dpkts": 0,
                "sbytes": 0,
                "dbytes": 0
            }

        size = len(pkt)

        # Forward direction
        flows[key]["spkts"] += 1
        flows[key]["sbytes"] += size

        # Reverse flow
        rev_key = (dst, src, proto)
        if rev_key in flows:
            flows[rev_key]["dpkts"] += 1
            flows[rev_key]["dbytes"] += size

    # Write CSV
    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["proto", "spkts", "dpkts", "sbytes", "dbytes", "label"])

        for (src, dst, proto), data in flows.items():
            # Simple labeling logic (customize later)
            label = 0  # default: normal

            writer.writerow([
                proto,
                data["spkts"],
                data["dpkts"],
                data["sbytes"],
                data["dbytes"],
                label
            ])

    print(f"✅ CSV saved as {output_csv}")
