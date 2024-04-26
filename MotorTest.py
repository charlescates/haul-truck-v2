from gpiozero import Motor
from time import sleep

# Declare motors
frontLeftMotor = Motor(foward=17, backward=27)
frontRightMotor = Motor(forward=23, backward=24)
backLeftMotor = Motor(foward=6, backward=13)
backRightMotor = Motor(foward=16, backward=20)

# Functions
def forward():
    frontLeftMotor.foward()
    frontRightMotor.forward()
    backLeftMotor.forward()
    backRightMotor.forward()

def backward():
    frontLeftMotor.backward()
    frontRightMotor.backward()
    backLeftMotor.backward()
    backRightMotor.backward()

def left():
    frontLeftMotor.foward()
    frontRightMotor.backward()
    backLeftMotor.forward()
    backRightMotor.backward()

def right():
    frontLeftMotor.backward()
    frontRightMotor.forward()
    backLeftMotor.backward()
    backRightMotor.forward()

def stop():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()

forward()
sleep(0.5)
stop()