import sys
import re
import csv

def getDataFromStatistics(filename):
    with open(filename, 'r') as file:
        content = file.read().replace(" ", "")
        content = re.sub('[^A-Za-z0-9|\n<.]+', '', content)
    lines = content.split('\n')

    data = [l for l in lines if "<" in l]
    return data

if __name__ == '__main__':
    arguments = sys.argv[1:]
    
    wiredStats = arguments[0]
    wirelessStats = arguments[1]

    wiredData = getDataFromStatistics(wiredStats)
    wirelessData = getDataFromStatistics(wirelessStats)

    with open(f"WirelessWiredData.csv", mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["latency","retransmission","bandwidth","label"])

        for l in wiredData:
            linspl = l.split("|")
            [latency, retransmission, bandwidth] = linspl[2], linspl[3], linspl[4]
            csv_writer.writerow([latency, retransmission, bandwidth, 'wired'])

        for l in wirelessData:
            linspl = l.split("|")
            [latency, retransmission, bandwidth] = linspl[2], linspl[3], linspl[4]
            csv_writer.writerow([latency, retransmission, bandwidth, 'wireless'])