import socket
import sys
import time

myPort, parentIp, parentPort, ipsFileName = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', myPort))
while True:
	data, addr = s.recvfrom(1024)
	data = data.decode()
	if data[-1] == '\n':
		data = data[:-1]
	file = open(ipsFileName, "r")
	lines = file.readlines()
	file.close()
	isFound = False
	for line in lines:
		splitOfLine = line.split(sep=",")
		if data == splitOfLine[0]:
			if len(splitOfLine) == 3 or (time.time() - float(splitOfLine[3])) < float(splitOfLine[2]):
				s.sendto(str.encode(line), addr)
				isFound = True
			else:
				lines.remove(line)
	if not isFound:
		if parentIp != -1 and parentPort != -1:
			s.sendto(data.encode(), (parentIp, parentPort))
			data2, addr2 = s.recvfrom(1024)
			data2 = data2.decode()
			if data2[-1] == '\n':
				data2 = data2[:-1]
			dataForFile = "\n" + data2 + ',' + str(time.time())
			lines.append(dataForFile)
			file = open(ipsFileName, "w")
			for line in lines:
				file.write(line)
			file.close()
			s.sendto(data2.encode(), addr)