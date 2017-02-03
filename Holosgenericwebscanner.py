import sys, time
from socket import *
from datetime import datetime

host = ''
minport = 1
maxport = 100


def scan_host(host, port, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            r_code = code
            s.close()
    except Exception, e:
        pass
    return r_code


try:
    host = raw_input("Enter host2pwn: ")
except KeyboardInterrupt:
    print("\n\n n00b chickened out. Shutting down")
    sys.exit(1)

    hostip = gethostbyname(host)
    print("Host: %s\n IP: %s" % (host, hostip))
for port in range(minport, maxport):
    try:
        response = scan_host(host, port)
        if response == 0:
            print("Port %d open" % port)
    except Exception, e:
        pass
