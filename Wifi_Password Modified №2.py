# __Author__ __Lencof__
# Wifi_Password Modified №2.py

import wifi

x="Wifi" 
password="dfbmkfdklbrftjhbiodfj940358231984mfdg" 
while x!=password:
  x=""
  while len(x)!=len(password):
    y=random.randrange(10)
    x=str(x)+str(y)
  print("Password:",x) 
  
  # It took a lot of time
