from pynput.mouse import Button, Controller
from time import *
mouse = Controller()
key_list = []

for i in range(0, 10):
    key_list.append(mouse.position)
    sleep(0.4)

print(key_list)
