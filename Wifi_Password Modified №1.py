# __Author__ __Lencof__
# Wifi_Password Modified №1.py

import random
from password import password

x="Wifi"
while x != password:
  x = " "
  while len(x) != len(password):
    y = random.randrange(10)
    x = str(x) + str(y)
  print("Password:", x)
  
  # It took a lot of time
