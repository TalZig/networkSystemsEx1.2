import socket
import sys
import datetime

myPort, parentIp, parentPort, ipsFileName = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', myPort))
file = open(ipsFileName,"r")
lines = file.readline()
ttls = []
addresses = []
ips = []
dates = []
for line in lines:
	lineSplitByComma = line.split(sep=",")
	addresses.append(line[0])
	ips.append(line[1])
	ttls.append(line[2])

while True:
    data, addr = s.recvfrom(1024)
	if (data in addresses):
		s.sendto(str.encode(ips[addresses.index(data)]), addr)
	else:
		s.sendto()
    s.sendto(data.upper(), addr)
