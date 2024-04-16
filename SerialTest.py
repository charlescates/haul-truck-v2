import serial
from time import sleep
#'/dev/serial0' might be the wrong port
serialPort = serial.Serial('/dev/serial0')
serialPort.timeout = 1
print(serialPort.name)
serialPort.write(b'test\n')
sleep(1)
thing = serialPort.readline()
print(thing)