# __author__ __Lencof__
# Wifi_Password.py

import wifi 
import random 


x="Telnet_130" # Your Wifi
password="29121998" # Random Password
while x!=password:
    x=""
    while len(x)!=len(password):
        y=random.randrange(10)
        x=str(x)+str(y)
    print(x)
print("Password:",x) 

# It took a lot of time 
