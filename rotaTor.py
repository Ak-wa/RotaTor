#!/usr/bin/python
# for any bugs/issues contact me at github.com/ak-wa
# woop woop
try:
    import socks, socket
    from time import sleep
    from stem.control import Controller
    from stem import Signal
    from sys import stdout
    from requests import get
except:
    from os import system
    system('pip install socks')
    system('pip install stem')
    system('pip install requests')
    import socks, socket
    from time import sleep
    from stem.control import Controller
    from stem import Signal
    from requests import get

with Controller.from_port(port = 9051) as controller:
    controller.authenticate()
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket     
    while 1:
        ip_req = get("https://myexternalip.com/raw")
        print("[+] Exit node: %s" % (ip_req.text))
        print("[+] Your code could happen here!") # You can delete this
        # Here comes your code, e.g a request to a website
        #
        #
        controller.signal(Signal.NEWNYM)
        sleep(controller.get_newnym_wait())
