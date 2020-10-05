from rotaTor import Rotator
rot = Rotator(verbose=False)
for i in range(3):
    rot.rotate()
    print(rot.get_node())
