#!/usr/bin/env python3
from getch import getch
import wiringpi as wp


motor_1_speed = 100
motor_1_dir = 28
motor_1_brake = 27

motor_2_speed = 100
motor_2_dir = 26
motor_2_brake = 6

motor_3_speed = 100
motor_3_dir = 1
motor_3_brake = 100

motor_4_speed = 100
motor_4_dir = 23
motor_4_brake = 22

dispense = 7

def setupPins():
    wp.wiringPiSetup()

    wp.pinMode(motor_1_speed,1)
    wp.pinMode(motor_1_dir,1)
    wp.pinMode(motor_1_brake,1)

    wp.pinMode(motor_2_speed,1)
    wp.pinMode(motor_2_dir,1)
    wp.pinMode(motor_2_brake,1)

    wp.pinMode(motor_3_speed,1)
    wp.pinMode(motor_3_dir,1)
    wp.pinMode(motor_3_brake,1)

    wp.pinMode(motor_4_speed,1)
    wp.pinMode(motor_4_dir,1)
    wp.pinMode(motor_4_brake,1)

    wp.pinMode(dispense,1)

    wp.softPwmCreate(motor_1_speed,100,100)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_1_brake,1)

    wp.softPwmCreate(motor_2_speed,100,100)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_2_brake,1)

    wp.softPwmCreate(motor_3_speed,100,100)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_3_brake,1)

    wp.softPwmCreate(motor_4_speed,100,100)
    wp.digitalWrite(motor_4_dir,1)
    wp.digitalWrite(motor_4_brake,1)

def moveForward():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_1_brake,0)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_2_brake,0)

def moveBackward():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_1_dir,0)
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_2_dir,0)
    wp.digitalWrite(motor_2_brake,1)

def moveRight():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_3_brake,0)
    wp.digitalWrite(motor_4_dir,1)
    wp.digitalWrite(motor_4_brake,0)

def moveLeft():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,0)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_4_dir,0)
    wp.digitalWrite(motor_4_brake,1)

def rotateLeft():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_3_brake,0)
    wp.digitalWrite(motor_4_dir,0)
    wp.digitalWrite(motor_4_brake,1)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_1_brake,0)
    wp.digitalWrite(motor_2_dir,0)
    wp.digitalWrite(motor_2_brake,1)

def rotateRight():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,0)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_4_dir,1)
    wp.digitalWrite(motor_4_brake,0)
    wp.digitalWrite(motor_1_dir,0)
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_2_brake,0)

def dispense():
    wp.digitalWrite(dispense,1)
    wp.delay(40)
    wp.digitalWrite(dispense,0)

def reset():
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_2_brake,1)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_4_brake,1)
    wp.digitalWrite(motor_4_dir,1)

def beginControl():
    setupPins()
    current_cmd = -1
    while True:
        current_cmd = getch()

        if current_cmd == 'w':
            moveForward()

        elif current_cmd == 's':
            moveBackward()

        elif current_cmd == 'd':
            moveRight()

        elif current_cmd == 'a':
            moveLeft()

        elif current_cmd == 'q':
            rotateRight()

        elif current_cmd == 'e':
            rotateLeft()

        elif current_cmd == 'u':
            dispense()


        wp.delay(40)

        reset()
