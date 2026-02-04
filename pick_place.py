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
delta_speed = 1*20
speed_black = 1*(44 + delta_speed/2)
rotation_speed = 1*(18)
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
        last_seen = 1
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

    if rotation_time > 1.2:
        rotation_time = -1.4
        last_seen *= -1

m3.on(50)
sleep(5.5)
m3.off()


while not s1.is_pressed:
	print("-"*28)

while True:
    if state == -1:
        l1.on(30)
        l2.on(30)
        if s2.color_name == "Black" or s3.color_name == "Black": 
            state = 0

    if state == 0:
        follow_the_line(["Black"])
        if s2.color_name == "Red" or s3.color_name == "Red":
            l1.on(0)
            l2.on(0)
            sleep(0.4)
            state = 1
            state1_time = 0
            

    if state == 1:
        if state1_time < 0.5:
            last_seen = -1
        print("state1")
        follow_the_line({"Red"})
        state1_time += tick
        if state1_time > 1.3 and (s2.color_name in ["Black"] or s3.color_name in ["Black"]):
            state = 2

    if state == 2:
        print("state2")
        if s2.color_name in ["Black"] and s3.color_name in ["Black"]:
            l1.on(18)
            l2.on(18)
            rotation_time = 0
        if (not s2.color_name in ["Black"] and s3.color_name in ["Black"]): 
            l1.on(12-12)
            l2.on(12+12)
            last_seen = -1
            rotation_time = 0
        if (s2.color_name in ["Black"] and not s3.color_name in ["Black"]): 
            l1.on(12+12)
            l2.on(12-12)
            last_seen = 1
            rotation_time = 0
        if (not s2.color_name in ["Black"] and not s3.color_name in ["Black"]): 
            follow_the_line(["Black"])

        if s2.color_name == "Red" or s3.color_name == "Red":
            l1.on(last_seen * 2*rotation_speed)
            l2.on(-last_seen * 2*rotation_speed)
            sleep(0.1)
            l1.on(speed_black+delta_speed/2)
            l2.on(speed_black+delta_speed/2)
            sleep(0.24)
            state = 3

    if state == 3:
        print("state3")
        l1.on(0)
        l2.on(0)
        m3.on(-50)
        sleep(4.5)
        m3.on(0)
        l1.on(last_seen * 3 *rotation_speed)
        l2.on(-last_seen * 3 *rotation_speed)
        sleep(1.83)
        l1.on(speed_black+delta_speed/2)
        l2.on(speed_black+delta_speed/2)
        sleep(0.20)
        state = 4

    if state == 4:
        print("state4")
        follow_the_line(["Black", "Red"])
        if s2.color_name == "Green" or s3.color_name == "Green":
            state = 6
            last_seen = -1
            l1.on(-last_seen * 3 *rotation_speed)
            l2.on(last_seen * 3 *rotation_speed)
            sleep(0.80)

    if state == 5:
        speed_black = 1*(32 + delta_speed/2)
        rotation_speed = 1*(12)
        print("state5")
        follow_the_line(["Green"])
        state5_time += tick
        if state5_time > 1.5 and (s2.color_name == "Green" or s3.color_name == "Green"):
            state = 6

    if state == 6:
        print("state6")
        if True:
            l1.on(0)
            l2.on(0)
            m3.on(50)
            sleep(4.5)
            m3.on(0)
            l1.on(-50)
            l2.on(-50)
            sleep(1)
            l1.on(0)
            l2.on(0)
            break
    print(s2.color_name + s3.color_name)
    sleep(tick)
