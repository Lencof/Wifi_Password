# __author__ __Lencof__
# Wifi_Password.py

import random
from password import password

x="Telnet_130" 
password="29121998" 
while x!=password:
    x=""
    while len(x)!=len(password):
        y=random.randrange(10)
        x=str(x)+str(y)
    print(x)
print("Password:",x) 

# It took a lot of time 
