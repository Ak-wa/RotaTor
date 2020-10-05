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
    def __init__(self, tor_host="127.0.0.1", tor_port=9050, verbose=False):
        self.__controller = Controller.from_port(port=9051)
        self.__tor_host = tor_host
        self.__tor_port = tor_port
        self.__verbose = verbose
        self.node = None

        if self.__verbose:
            self.public_ip = get("https://myexternalip.com/raw").text
            print("[+] Your (real) public IP address is:", self.public_ip)

    def get_node(self):
        self.node = get("https://myexternalip.com/raw").text
        return self.node

    def rotate(self):
        self.__controller.authenticate()
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, self.__tor_host, self.__tor_port)
        socket.socket = socks.socksocket
        if self.__verbose:
            self.get_node()
            print("[+] Exit node: %s" % self.node)
        self.__controller.signal(Signal.NEWNYM)
        sleep(self.__controller.get_newnym_wait())
