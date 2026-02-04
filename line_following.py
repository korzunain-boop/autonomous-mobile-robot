#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.led import Leds
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor


l1 = LargeMotor(OUTPUT_A)
l2 = LargeMotor(OUTPUT_B)
m3 = MediumMotor(OUTPUT_C)
leds = Leds()
s1 = TouchSensor(INPUT_1)
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)

state = -1
rotation_time = 0
last_seen = 1
tick = 0.05
delta_speed = 1*28
speed_black = 1*(56 + delta_speed/2)
rotation_speed = 1*(19)
state1_time = 0
state5_time = 0

def follow_the_line(followed_colors):
    global rotation_time
    global last_seen
    global tick
    global delta_speed
    global speed_black
    global rotation_speed

    if (s2.color_name in followed_colors and not s3.color_name in followed_colors): 
        l1.on(speed_black+delta_speed)
        l2.on(speed_black-delta_speed)
        last_seen = 1
        rotation_time = 0

    if (not s2.color_name in followed_colors and s3.color_name in followed_colors): 
        l1.on(speed_black-delta_speed)
        l2.on(speed_black+delta_speed)
        last_seen = -1
        rotation_time = 0

    if (s2.color_name in followed_colors and s3.color_name in followed_colors): 
        l1.on(speed_black+delta_speed/2)
        l2.on(speed_black+delta_speed/2)
        rotation_time = 0

    if (not s2.color_name in followed_colors and not s3.color_name in followed_colors): 
        if abs(rotation_time-0.01) < 5*tick:
            l1.on(20 + last_seen * 3*rotation_speed)
            l2.on(20 + -last_seen * 3*rotation_speed)
        else:
            l1.on(-last_seen * 3 *rotation_speed )
            l2.on(last_seen * 3 *rotation_speed)			
        rotation_time += tick

    if rotation_time > 1.1:
        rotation_time = -1.3
        last_seen *= -1

while not s1.is_pressed:
	print("-"*28)

while True:
	follow_the_line(["Black"])