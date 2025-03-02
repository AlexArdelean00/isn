import subprocess
import time
import csv

command = ['top', '-b', '-n', '1']

with open("stats.csv", mode="w", newline='') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(["VIRT", "CPU", "RAM"])
	for i in range(600):
		result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		if result.returncode == 0:
			content = result.stdout
			#print(content)
			for line in content.split("\n"):
				if "tshark" in line:
					cols = line.split()
					virt = cols[4]
					cpu = cols[8]
					ram = cols[9]
					csv_writer.writerow([virt, cpu, ram])
					print(i)
					print(virt)
					print(cpu)
					print(ram)
		else:
			print("Error")
			break
		time.sleep(1)