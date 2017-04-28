import socket 
import ssl 
import httplib 
import requests 

proxies = {}

RHOST = 'https://commandandconquer.net'
PORT = 80

resp = requests.get(RHOST, proxies)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="TLS_RSA_WITH_RC4_128_SHA")
wrappedSocket.connect((HOST, PORT))  #set HOST and port to agree with resp
wrappedSocket.send(packet)
print wrappedSocket.recv(1280)
wrappedSocket.close()

