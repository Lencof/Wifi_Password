# __Author__ __Lencof__
# Wifi_Password Modified №4.py

'''
added new class changed numbers
removed the sys module.
'''

import os
import sys 
import wifi
import random

# create class Wifi_Password():
class Wifi_Password():
    pass

Wifi="Telnet_130" # Your Wifi
password="1234567890" # Random Password
while Wifi!=password:
    Wifi=""
    while len(Wifi)!=len(password):
        y=random.randrange(10)
        Wifi=str(Wifi)+str(y)
    print(Wifi)
print("Password:",Wifi)
