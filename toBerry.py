# /usr/bin/python3
# -*- coding:utf-8 -*-
import os
from socket import *
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading

'''
公共初始化
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''
初始化小车行进部分
'''

ENA = 13
ENB = 20

IN1 = 19
IN2 = 16
IN3 = 21
IN4 = 26

rool_speed = 5

GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT,  initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT,  initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT,  initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT,  initial=GPIO.LOW)

pwmA = GPIO.PWM(ENA, 25)
pwmB = GPIO.PWM(ENB, 25)

def speed(np):
    np = max(0, min(100, np))
    global rool_speed

    rool_speed = np

    pwmA.ChangeDutyCycle(rool_speed)
    pwmB.ChangeDutyCycle(rool_speed)

def engStart():
    global rool_speed

    pwmA.start(rool_speed)
    pwmB.start(rool_speed)

def pwmEnd():

    pwmA.stop()
    pwmB.stop()

def gogo():
    LGogo()
    RGogo()
    
def back():
    LBack()
    RBack()

def rockL():
    LBack()
    RGogo()

def rockR():
    LGogo()
    RBack()

def stop():
    # GPIO.output(ENA, False)
    # GPIO.output(ENB, False)

    # pwmEnd()

    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def RGogo():
    # global rool_speed

    # GPIO.output(ENA, True)
    # pwmA.start(rool_speed)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)

def LGogo():
    # global rool_speed

    # GPIO.output(ENB, True)
    # pwmB.start(rool_speed)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def RBack():
    # global rool_speed

    # GPIO.output(ENA, True)
    # pwmA.start(rool_speed)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)

def LBack():
    # global rool_speed

    # GPIO.output(ENB, True)
    # pwmB.start(rool_speed)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

'''
初始化声纳测距部分
'''

Trig = 17
Echo = 4 

GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def get_Dis_Sound():
    time.sleep(0.05)
    # 启动
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trig, GPIO.LOW)

    while not GPIO.input(Echo):
        pass

    t1 = time.time()

    while GPIO.input(Echo):
        pass

    t2 = time.time() - t1
    time.sleep(0.1)

    return t2 * 340 / 2 * 100

'''
红外部分
'''
IR_R = 18
IR_L = 27
GPIO.setup(IR_R, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Avioding_IR():
    if GPIO.input(IR_L) == False and GPIO.input(IR_R) == False:
        gogo()
    elif GPIO.input(IR_L) == False and GPIO.input(IR_R) == True:
        RBack()
    elif GPIO.input(IR_L) == True and GPIO.input(IR_R) == False:
        LBack()
    elif GPIO.input(IR_L) == True and GPIO.input(IR_R) == True:
        stop()
'''
返回左右红外的检测数据
'''
def getIR():
    return GPIO.input(IR_L) , GPIO.input(IR_R)

'''
按键部分
'''
car_stop = True
B_S4 = 11
GPIO.setup(B_S4, GPIO.IN)

def Check8Button():
    if GPIO.input(B_S4):
        stop != stop
    print(GPIO.input(B_S4))


'''
贴片三色LED
LY-S0004
'''
LED_R = 5
LED_B = 7
LED_G = 8
GPIO.setup(LED_R , GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_B , GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G , GPIO.OUT, initial=GPIO.LOW)

LY004LEDLIGHT = []

def Init004LED_Order(temp, k):
    if k==3:
        LY004LEDLIGHT.append(temp.copy())
        return

    Init004LED_Order(temp.copy(), k +1)

    temp[k] = not temp[k]

    Init004LED_Order(temp.copy(), k +1)


def LED_show(i):
    GPIO.output(LED_R, LY004LEDLIGHT[i][0])
    GPIO.output(LED_B, LY004LEDLIGHT[i][1])
    GPIO.output(LED_G, LY004LEDLIGHT[i][2])

def LED_flesh(i):
    if len(LY004LEDLIGHT) == 0:
        Init004LED_Order([False, False, False], 0)
        print(LY004LEDLIGHT)
        
    LED_show(i)
    
'''
继电器部分
'''
DSwitch_P = 9
GPIO.setup(DSwitch_P, GPIO.OUT, initial=GPIO.LOW)

def switch_it_to(to_what):
    print (to_what)
    GPIO.output(DSwitch_P, to_what)


'''
主程序
'''
if __name__ == "__main__":
    pass


    # q = 'q'
    # # led_index = 0
    # switch_to_what = False 
    # time_delay = 1
    # while True:
    #     time.sleep(time_delay)
    #     # switch_it_to(switch_to_what)
    #     # switch_to_what = not switch_to_what

    #     GPIO.output(DSwitch_P, GPIO.HIGH)
    #     time.sleep(time_delay)
    #     GPIO.output(DSwitch_P, GPIO.LOW)

    #     '''
    #     # 贴片LED
    #     LED_flesh(led_index)
    #     led_index += 1
    #     led_index %= len(LY004LEDLIGHT)
    #     '''

    #     '超声测距'
    #     # get_Dis_Sound()
    #     '红外避障'
    #     # Avioding_IR()
    #     '按键检测'
    #     # if car_stop:
    #     #     stop()
    #     # else:
    #     #     gogo()
    #     # time.sleep(0.5)

    #     # a = input()
    #     # if a=='q':
    #     #     stop()
    #     #     break