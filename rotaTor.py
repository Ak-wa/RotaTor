#!/usr/bin/python
# for any bugs/issues contact me at github.com/ak-wa
# woop woop

import socks
import socket
from time import sleep
from stem.control import Controller
from stem import Signal
from requests import get


class Rotator:
    def __init__(self, tor_host="127.0.0.1", tor_port=9150):
        self.__controller = Controller.from_port(port=9051)
        self.__tor_host = tor_host
        self.__tor_port = tor_port

        self.public_ip = get("https://myexternalip.com/raw")
        print("Your (real) public IP address is:", self.public_ip)

    def rotate(self):
        self.__controller.authenticate()
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, self.__tor_host, self.__tor_port)
        socket.socket = socks.socksocket
        ip_req = get("https://myexternalip.com/raw")
        print("[+] Exit node: %s" % ip_req.text)
        self.__controller.signal(Signal.NEWNYM)
        sleep(self.__controller.get_newnym_wait())
