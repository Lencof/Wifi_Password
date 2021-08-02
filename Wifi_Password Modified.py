# __Author__ __Lencof__
# Wifi_Password Modified.py

import wifi 
import random 

x="Capo_125" 
password="29121994598439058439058435894695846908549068895476895476896767548954906898"
while x!=password:
  x=""
  while len(x)!=len(password):
      y=random.randrange(10)
      x=str(x)+str(y)
  print("Password:",x)
  
  # It took a lot of time
