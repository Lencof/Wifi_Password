# __Author__ __Lencof__
# Wifi_Password Modified №1.py

import wifi 

x="Wifi"
password = [12345678910]  
while x != password:
  x = " "
  while len(x) != len(password):
    y = random.randrange(10)
    x = str(x) + str(y)
  print("Password:", x)
  
  # It took a lot of time
