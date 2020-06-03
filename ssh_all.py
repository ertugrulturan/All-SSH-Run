#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
from pexpect import pxssh

print ('''
 SSS   SSS  H  H  AA  L    L    RRRR  U   U N   N 
S     S     H  H A  A L    L    R   R U   U NN  N 
 SSS   SSS  HHHH AAAA L    L    RRRR  U   U N N N 
    S     S H  H A  A L    L    R R   U   U N  NN 
SSSS  SSSS  H  H A  A LLLL LLLL R  RR  UUU  N   N 
''')

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def t13rCommand(command):
    for client in t13r:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' +str(output, encoding='utf-8')+ '\n')

def addClient(host, user, password):
    client = Client(host, user, password)
    t13r.append(client)

order = input("Command:")
t13r = []
addClient('host', 'username', 'passwd') # add your ssh linux server
# addClient('host','username','passwd') -> you can add as much as you want
t13rCommand(order)
