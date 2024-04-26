from gpiozero import Motor
from time import sleep

# Declare motors
frontLeftMotor = Motor(17, 27)
frontRightMotor = Motor(23, 24)
backLeftMotor = Motor(6, 13)
backRightMotor = Motor(16, 20)

# Functions
def goForward():
    frontLeftMotor.forward()
    frontRightMotor.forward()
    backLeftMotor.forward()
    backRightMotor.forward()

def goBackward():
    frontLeftMotor.backward()
    frontRightMotor.backward()
    backLeftMotor.backward()
    backRightMotor.backward()

def goLeft():
    frontLeftMotor.forward()
    frontRightMotor.backward()
    backLeftMotor.forward()
    backRightMotor.backward()

def goRight():
    frontLeftMotor.backward()
    frontRightMotor.forward()
    backLeftMotor.backward()
    backRightMotor.forward()

def goStop():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()

goForward()