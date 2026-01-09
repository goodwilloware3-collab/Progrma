#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S4)
motor_left = Motor(Port.A)
motor_right = Motor(Port.B)
robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=114)
motor_grabber = Motor(Port.A)  # Changed from Port.C to Port.A to avoid port conflict

# Write your program here.
ev3.speaker.beep()
target=38
gain=1.25
while True:
    correction= color_sensor.reflection()-target
    turn_power=correction*gain
    robot.drive(100,turn_power)   

!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S4)   # Make sure this is correct
motor_left = Motor(Port.A)
motor_right = Motor(Port.B)
motor_grabber = Motor(Port.C)         # FIXED: no conflict
robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=114)

ev3.speaker.beep()

target = 38
gain = 1.25

while True:
    value = color_sensor.reflection()

    if value is None:
        ev3.speaker.beep(100, 300)   # error beep
        continue                     # skip this loop

    correction = value - target
    turn_power = correction * gain
    robot.drive(100, turn_power)
