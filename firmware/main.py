import network
import time

sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)    
sta.connect("quepasapatejode", "losvilla08")
while not sta.isconnected():
    time.sleep(1)
    
print("Conectado a la red WiFi")
print(sta.ifconfig())


