import pyserial
#'/dev/serial0' might be the wrong port
serialPort = serial.Serial('/dev/serial0')
print(serialPort.name)