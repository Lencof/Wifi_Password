# __Author__ __Lencof__
# Wifi_Password Modified №2.py

import os
import wifi
import random 

x="Wifi" # your wifi
password="dfbmkfdklbrftjhbiodfj940358231984mfdg" # your figures 
while x!=password:
  x=""
  while len(x)!=len(password):
    y=random.randrange(10)
    x=str(x)+str(y)
  print("Password:",x) # use function print()
  
  # It took a lot of time
