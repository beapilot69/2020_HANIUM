from __future__ import division
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685() #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

servo_min = 130
servo_mid = 380
servo_max = 630


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)

####initial condition###
pwm.set_pwm(15,0,180) #right
pwm.set_pwm(8,0,450)  #left
time.sleep(1)
pwm.set_pwm(12,0,400) #bottom
pwm.set_pwm(9,0,350)  #tong open

start = 400
end = 130
term = -1
for bot in range(start,end,-1):  #Rotate to pick up
    pwm.set_pwm(12,0,bot)
    time.sleep(0.001)

time.sleep(1)

for right in range(180,280,1):
    pwm.set_pwm(15,0,right) #go forward
    time.sleep(0.001)
time.sleep(1)

for left in range(450,330,-1):
    pwm.set_pwm(8,0,left)  #down tong
    time.sleep(0.001)
time.sleep(1)


pwm.set_pwm(15,0,430) #go forward
time.sleep(1)

for left in range(330,230,-1):
    pwm.set_pwm(8,0,left)  #down tong
    time.sleep(0.001)
time.sleep(1)
pwm.set_pwm(9,0,130)  #tong close
time.sleep(1)
for left in range(230,410,1):
    pwm.set_pwm(8,0,left)  #up tong
    time.sleep(0.001)
    
time.sleep(1)
for bot in range(130,430,1):
    pwm.set_pwm(12,0,bot) #Rotate to A conveyorbelt
    time.sleep(0.001)
time.sleep(1)
# for left in range(430,380,-1):
#     pwm.set_pwm(8,0,left)  #down tong to get off a thing
#     time.sleep(0.00)
# time.sleep(1)

pwm.set_pwm(9,0,350)  #tong open
time.sleep(1)

pwm.set_pwm(2,0,450)  #classify
time.sleep(5)
pwm.set_pwm(2,0,630)  #open
time.sleep(1)


# pwm.set_pwm(15,0,180) #right
# pwm.set_pwm(8,0,450)  #left
# time.sleep(1)
# pwm.set_pwm(12,0,400) #bottom
# pwm.set_pwm(9,0,350)  #tong open

# for i in range(180,400, 5):
#     pwm.set_pwm(15, 0, i)
#     time.sleep(0.05)
#     if i ==400:
#     
#         for j in range(380,250, 5):
#             pwm.set_pwm(8, 0, j)
#             time.sleep(0.05)
        

        
