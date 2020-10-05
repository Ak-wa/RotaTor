from rotaTor import Rotator
rot = Rotator(verbose=False)
for i in range(3):
    rot.rotate()
    print("[+] Your code could happen here!")
    print("[+] Current IP: " + rot.get_node())
