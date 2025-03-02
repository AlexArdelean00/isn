import subprocess
import re
from joblib import load
import numpy as np
import warnings
warnings.filterwarnings("ignore")

estimator = load("bestModelSVM.joblib")
scaler = load('scaler.pkl')
map = {
    0: "Wired",
    1: "Wireless"
}

# Selezione dell'interfaccia su cui catturare
result = subprocess.run(['tshark', '-D'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)
interfaccia = input("Select interface: ")

# Avvia la cattura sull'interfaccia
command = [
    'tshark', '-i', interfaccia, '-a', f'duration:1',
    '-q', '-p', '-z',
    'io,stat,1,AVG(tcp.analysis.ack_rtt)tcp.analysis.ack_rtt,COUNT(tcp.analysis.retransmission)tcp.analysis.retransmission,BYTES'
]

duration = 600
wiredSamples = 0
wirelessSamples = 0
# Cattura i dati ogni secondo ed effettua una previsione
for i in range(duration):
    print(i)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        content = result.stdout
        content = content.replace(" ", "")
        content = re.sub('[^A-Za-z0-9|\n<.]+', '', content)
        lines = content.split('\n')
        data = [l for l in lines if "<" in l]
        linspl = data[0].split("|")
        [latency, retransmission, bandwidth] = float(linspl[2]), int(linspl[3]), int(linspl[4])
        print([latency, retransmission, bandwidth] )

        new_data = np.array([latency, retransmission, bandwidth]).reshape(1, -1)
        new_data_normalized = scaler.transform(new_data)

        label = map[int(estimator.predict(new_data_normalized))]
        print(label)

        if label == "Wireless":
            wirelessSamples += 1
        else:
            wiredSamples += 1
    else:
        print(f"Unable to monitor on interface {interfaccia}")
        break

print(f"Wireless sample: {wirelessSamples/duration*100} %")
print(f"Wired sample: {wiredSamples/duration*100} %")