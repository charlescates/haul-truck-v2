from gpiozero import Motor
from time import sleep

# Declare motors
frontLeftMotor = Motor(forward=17, backward=27)
frontRightMotor = Motor(forward=23, backward=24)
backLeftMotor = Motor(forward=6, backward=13)
backRightMotor = Motor(forward=16, backward=20)

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
sleep(0.5)
goStop()