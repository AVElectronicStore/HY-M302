# --------------------------------------------
# - Demo para exposicion en Machachi
# - Autor: Rodrigo Tufiño
# - Fecha: 28/11/2022
# -------------------------------------------

import serial
import time
import os

from dotenv import load_dotenv
from base import Base

load_dotenv()

db_host = os.environ['BDD_HOST']
db_user = os.environ['BDD_USER']
db_pass = os.environ['BDD_PASS']
db_schema = os.environ['BDD_SCHEMA']

puerto = os.environ['TTY_DEVICE']
baudios = os.environ['TTY_BAUDIOS']

arduino = serial.Serial(puerto,baudios);
db = Base(db_host, db_user, db_pass, db_schema)

time.sleep(2)

for i in range(10):
    arduino.write(b'x')
    time.sleep(0.05)
    line = arduino.readline()
    if line:
        string = line.decode().strip()
        frame = string.split(";")
        print(frame)
        if len(frame) == 7:
            hum = float(frame[0])
            tem = float(frame[1])
            pot = float(frame[2])
            luz = float(frame[3])
            sw1 = float(frame[5])
            sw2 = float(frame[6])
            db.agregar(hum, tem, luz, pot, sw1, sw2)
    time.sleep(1)

arduino.close()
db.cerar()
