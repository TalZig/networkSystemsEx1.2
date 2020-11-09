import socket
import sys
import time

myPort, parentIp, parentPort, ipsFileName = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', myPort))
while True:
    data, addr = s.recvfrom(1024)
	file = open(ipsFileName, "r")
	lines = file.readlines()
	file.close()
	isFound = False
	for line in lines:
		splitOfLine = line.split(sep=",")
		if data == splitOfLine[0]:
			if (len(splitOfLine) == 3 or float(splitOfLine[3]) - time.time()) < float(splitOfLine[2]):
				s.sendto(str.encode(line), addr)
				isFound = True
			else:
				lines.remove(line)
		if not isFound:
			s.sendto(data,(parentIp,parentPort))
			data2, addr2 = s.recvfrom(1024)
			data2 = data2.__str__() + ',' + str(time.time())
			lines.append(data2)
			file = open(ipsFileName, "w")
			for line in lines:
				file.write(line)
			file.close()
			s.sendto(bytes(data2), addr)