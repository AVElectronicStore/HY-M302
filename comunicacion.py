# --------------------------------------------
# - Demo para exposicion en Machachi
# - Autor: Rodrigo Tufiño
# - Fecha: 28/11/2022
# -------------------------------------------

import serial
import time

serial = serial.Serial("/dev/ttyACM0",9600);
time.sleep(2)

for i in range(50):
    line = serial.readline();
    if line:
        string = line.decode().strip()
        frame = string.split(";")
        if len(frame) == 8:
            dato = frame[0].split(":")
            print(f"Humedad: {dato[1]}%")
            dato = frame[1].split(":")
            print(f"Temperatura: {dato[1]}℃ ")

serial.close()

