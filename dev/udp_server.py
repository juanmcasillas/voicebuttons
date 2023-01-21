#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# ############################################################################
#
# udp_server.py
# 11/01/2023 (c) Juan M. Casillas <juanm.casillas@gmail.com>
#
# Simple UDP multicast server. Implements the same logic as DCS, so you 
# can test you program using this as Dummy.
#
# ############################################################################



import socket
from time import sleep
import json

addr = ("127.0.0.1", 64998)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#sock.bind(addr)



cmd_mod =  json.dumps({ "cmd": "mod", "value": "UH-1H" })
cmd_exit =  json.dumps({ "cmd": "exit", "value": True   })

count = 0
while count < 5:
    print("simulating connection")
    sleep(1)
    count+=1

count = 0
while count < 100000:
    print(cmd_mod)
    sock.sendto(cmd_mod.encode("ascii"), addr)
    sleep(1)
    count+=1

sock.send(cmd_exit.encode("ascii"),addr)
sock.close()

