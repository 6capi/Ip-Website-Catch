# Free use
# dev-capi
import socket
hostname = input("Website URL:\n")
print(f'{hostname} : {socket.gethostbyname(hostname)}')
