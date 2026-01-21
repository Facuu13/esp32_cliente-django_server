import network
import time
import urequests
import json

ssid = "quepasapatejode"
password = "losvilla08"

url = "http://192.168.1.11:8000/api/v1/data/"

# Funcion para conectar a una red WiFi
def wifi_connect(ssid, password, max_attempts=4, timeout_s=10):
    sta = network.WLAN(network.WLAN.IF_STA)
    sta.active(True)

    for attempt in range(1, max_attempts + 1):
        if sta.isconnected():
            return True

        print("WiFi: intento", attempt, "de", max_attempts)

        try:
            sta.disconnect()
        except:
            pass

        sta.connect(ssid, password)

        t0 = time.ticks_ms()
        while not sta.isconnected():
            if time.ticks_diff(time.ticks_ms(), t0) > timeout_s * 1000:
                print("WiFi: timeout")
                break
            time.sleep(0.2)

        if sta.isconnected():
            print("WiFi: conectado", sta.ifconfig())
            return True

    print("WiFi: no se pudo conectar")
    return False

# Funcion para hacer peticiones HTTP GET con reintentos
def http_get_json(url, retries=3, delay_s=2):
    for attempt in range(1, retries + 1):
        response = None
        try:
            print("HTTP GET: intento", attempt, "de", retries)
            response = urequests.get(url)

            if response.status_code != 200:
                print("HTTP GET: status", response.status_code)
                continue

            data = response.json()
            return data

        except Exception as e:
            print("HTTP GET: excepción", e)

        finally:
            if response:
                response.close()

        time.sleep(delay_s)

    print("HTTP GET: falló después de", retries, "intentos")
    return None


# Llamamos a la funcion para conectar wifi
wifi_connect(ssid, password)
# Hacemos una peticion HTTP GET
data = http_get_json(url)
if data:
    print("Datos recibidos:", data)
else:
    print("No se recibieron datos")




