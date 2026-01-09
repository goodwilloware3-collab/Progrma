#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize EV3
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S4)
motor_left = Motor(Port.A)
motor_right = Motor(Port.B)
robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=114)
motor_grabber = Motor(Port.D)

# Line following parameters
speed = 200  # Forward speed in mm/s
target = 10  # Target reflection value for center-followi\ng (low value = center of black line, 0-100 scale)
gain = 1.5   # Proportional gain (higher = more aggressive turning)
duration = 8000  # Duration to follow line in milliseconds (8 seconds)

# Start beep
ev3.speaker.beep()

# Make a 90-degree turn at the beginning
robot.turn(90)

# Move grabber motor down
motor_grabber.run_angle(300, -180)  # Rotate -90 degrees at 300 deg/s (adjust speed/angle as needed)

# Move 2 rotations forward
# Wheel diameter = 56mm, circumference = π * 56 ≈ 176mm, 2 rotations = 352mm
robot.straight(352)

# Turn 90 degrees right
robot.turn(-90)

# Move forward for 5 seconds
robot.drive(200, 0)  # Drive straight forward at 200 mm/s
wait(5000)  # Wait for 5 seconds
robot.stop()

# Line following loop - run for approximately 8 seconds
elapsed_time = 0
loop_delay = 10  # Small delay in milliseconds for each loop iteration

while elapsed_time < duration:
    # Read the reflection value (0 = black, 100 = white)
    reflection = color_sensor.reflection()
    
    # Calculate error: how far from target
    error = reflection - target
    
    # Calculate turn rate using proportional control
    # For center-following: tries to keep sensor on black line (low reflection)
    # Positive error (too light/off line) = turn toward line
    # Negative error (on black line) = minimal correction needed
    turn_rate = error * gain
    
    # Drive with correction
    robot.drive(speed, turn_rate)
    wait(loop_delay)
    elapsed_time += loop_delay

# Stop the robot after 8 seconds
robot.stop()

# Reverse a little bit
reverse_speed = -100  # Negative speed for reverse (mm/s)
reverse_time = 500  # Reverse for 0.5 seconds
robot.drive(reverse_speed, 0)  # Drive straight backward
wait(reverse_time)
robot.stop()
      
