# __Author__ __Lencof__
# Wifi_Password Modified №1.py

import os # use os
import sys # use sys
import wifi # use wifi
import random # use random

x="Wifi" # your wifi
password="12345678910" # your figures 
while x!=password:
  x=""
  while len(x)!=len(password):
    y=random.randrange(10)
    x=str(x)+str(y)
  print("Password:",x)
  
  # It took a lot of time
