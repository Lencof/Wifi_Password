# __Author__ __Lencof__
# Wifi_Password Modified №3.py

Wifi="Telnet_130"
password="29121994598439058439058435894695846908549068895476895476896767548954906898" 
while Wifi!=password:
    Wifi=""
    while len(Wifi)!=len(password):
        y=random.randrange(10)
        Wifi=str(Wifi)+str(y)
    print(Wifi)
print("Password:", Wifi)

