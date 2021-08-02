# __Author__ __Lencof__
# Wifi_Password Modified №4.py

'''
added new class changed numbers
removed the sys module.
'''

import wifi
import random

class Wifi_Password():
    pass

Wifi="Telnet_130" 
password="1234567890" 
while Wifi!=password:
    Wifi=""
    while len(Wifi)!=len(password):
        y=random.randrange(10)
        Wifi=str(Wifi)+str(y)
    print(Wifi)
print("Password:",Wifi)
