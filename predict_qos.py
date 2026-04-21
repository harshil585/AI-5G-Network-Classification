import pandas as pd
import joblib

# -----------------------------
# 1. Load Model & Encoder
# -----------------------------
print("Loading model...")
model = joblib.load("rf_model.pkl")
proto_encoder = joblib.load("proto_encoder.pkl")

# -----------------------------
# 2. Load Dataset
# -----------------------------
print("Loading dataset...")
df = pd.read_csv("mec_dataset.csv")

# -----------------------------
# 3. Basic Cleaning
# -----------------------------
df = df.dropna()

for col in ['spkts', 'dpkts', 'sbytes', 'dbytes']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

# -----------------------------
# 4. Encode Protocol
# -----------------------------
df['proto'] = df['proto'].apply(
    lambda x: x if x in proto_encoder.classes_ else proto_encoder.classes_[0]
)
df['proto'] = proto_encoder.transform(df['proto'])

# -----------------------------
# 5. Predict Traffic Type
# -----------------------------
X = df[['proto', 'spkts', 'dpkts', 'sbytes', 'dbytes']]
df['TrafficType'] = model.predict(X)

# -----------------------------
# 6. Map Traffic → QoS
# -----------------------------
def traffic_label(x):
    if x == 0:
        return "VoIP / Control Traffic"
    elif x == 1:
        return "Streaming Traffic"
    else:
        return "Web / Browsing Traffic"

def qos_map(x):
    if x == 0:
        return "Low Latency Required"
    elif x == 1:
        return "High Bandwidth Required"
    else:
        return "Best Effort"

df['Traffic_Label'] = df['TrafficType'].apply(traffic_label)
df['Predicted_QoS'] = df['TrafficType'].apply(qos_map)

# -----------------------------
# 7. Final Output
# -----------------------------
print("\n===== FINAL OUTPUT =====\n")
print(df[['proto', 'spkts', 'sbytes', 'Traffic_Label', 'Predicted_QoS']].head(10))

# -----------------------------
# 8. Save
# -----------------------------
df.to_csv("predicted_output.csv", index=False)

print("\n✅ Results saved to predicted_output.csv")
