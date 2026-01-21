import network
import time
import urequests
import json

sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)    
sta.connect("quepasapatejode", "losvilla08")
while not sta.isconnected():
    time.sleep(1)

print("Conectado a la red WiFi")
print(sta.ifconfig())

url = "http://192.168.1.11:8000/api/v1/data/"
r = urequests.get(url)
print(r.status_code)
data = r.json()   # parsea JSON
print(data)




