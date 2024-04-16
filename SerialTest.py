import serial
#'/dev/serial0' might be the wrong port
serialPort = serial.Serial('/dev/tty0')
print(serialPort.name)
serialPort.write(b'test\n')
thing = serialPort.readline()
print(thing)