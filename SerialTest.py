import serial
#'/dev/serial0' might be the wrong port
serialPort = serial.Serial('/dev/serial0')
print(serialPort.name)
serialPort.write("test\n")
thing = serialPort.readline()
print(thing)