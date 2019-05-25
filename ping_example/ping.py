import socket
import sys
import os
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket

def ping_at(env):
    server_ip = env.ip
    rep = os.system('ping -c 4 ' + server_ip)
    if rep == 0:
        print(f'{server_ip} is up\n')
        env.set_status(True)
    else:
        print(f'{server_ip} is down\n')
        env.set_status(False)

