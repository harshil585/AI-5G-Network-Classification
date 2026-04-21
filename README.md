# AI-Based 5G Network Traffic Classification

## Overview

This project presents an intelligent system for **traffic classification and Quality of Service (QoS) management** in a 5G Multi-access Edge Computing (MEC) environment.

The system captures real-time network traffic, converts it into flow-based features, and uses a **Random Forest machine learning model** to classify traffic types and assign appropriate QoS levels.

---

##  Objectives

* Capture real-time network traffic
* Convert packet-level data into flow-based features
* Train a machine learning model for classification
* Predict traffic types using real-time data
* Assign QoS dynamically based on classification

---

##  System Architecture

Workflow:

1. Capture packets using `tcpdump`
2. Convert PCAP → flow data using `Scapy`
3. Preprocess dataset
4. Train Random Forest model
5. Predict traffic class
6. Assign QoS


##  Project Structure

```
AI-5G-Network-Classification/
│
├── flow_extractor.py        # Extracts flow features
├── predict_qos.py           # Predicts QoS based on traffic
├── runner.py                # Main execution script
│
├── dns_collector.py         # Collects DNS traffic
├── traffic_collector.py     # Captures general traffic
├── network_data.py          # Handles dataset creation
│
├── mec_dataset.csv          # Dataset
├── rf_model.pkl             # Trained Random Forest model
├── proto_encoder.pkl        # Protocol encoder
│
└── README.md
```

##  How to Run

### 1. Capture network traffic

```bash
sudo tcpdump -i ens33 -w traffic.pcap
```

### 2. Convert to flow data

```bash
run runner.py and it will convert .pcap to csv format 
```

### 3. Run data collection scripts

```bash
python3 dns_collector.py
python3 traffic_collector.py
python3 network_data.py
```

### 4. Run main model

```bash
python3 train_model.py
```


##  Results

* Model Accuracy: ~91%
* Good precision and recall across traffic classes

### Observations:

* High packet flows → Streaming traffic
* Low packet flows → Control traffic
* UDP traffic → Mostly DNS
* Minor misclassification in ICMP

##  Output

The system classifies traffic and assigns QoS such as:

* Low Latency Required
* High Bandwidth Required

---

##  Conclusion

This project demonstrates an efficient AI-based approach for:

* Real-time traffic classification
* Dynamic QoS assignment

It is suitable for modern 5G MEC environments and works even with encrypted traffic due to flow-based analysis.

---


## 📎 Note

Make sure required tools (`tcpdump`, `Argus`) are installed before running.
