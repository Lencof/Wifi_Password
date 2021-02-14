# __Author__ __Lencof__
# Wifi_Password Modified.py

import random # use random

x="Capo_125" # Your Wifi
password="29121994598439058439058435894695846908549068895476895476896767548954906898" # Random password, put a lot of numbers
while x!=password:
  x=""
  while len(x)!=len(password):
      y=random.randrange(10)
      x=str(x)+str(y)
  print("Password:",x)
  
  # It took a lot of time
