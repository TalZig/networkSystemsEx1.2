import socket
import sys

ip, port = sys.argv[1], sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for line in sys.stdin:
    # exit condition
    s.sendto(line.encode(), (ip, int(port)))
    data, addr = s.recvfrom(1024)
    data = data.decode()
    data = data.split(",")
    print(str(data[1]))
s.close()