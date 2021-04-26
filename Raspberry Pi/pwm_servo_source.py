from __future__ import division
import time

# PCA9685모듈을 임포트.
import Adafruit_PCA9685



pwm = Adafruit_PCA9685.PCA9685(): #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)



#  서보모터의 펄스 길이를 최소, 중간, 최대로 설정
servo_min = 130  # Min pulse length out of 4096
servo_mid = 380  # Middle pulse length out of 4096
servo_max = 630  # Max pulse length out of 4096

# 서보 펄스폭을 더 간단하게 만들어주는 함수.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    

# 서보모터(SG90)에 최적화된 60Hz로 펄스주기를 설정.
# 서보모터(MG90)도 같은 펄스주기를 가짐.
pwm.set_pwm_freq(60)

while True:
    
    pwm.set_pwm(1, 0, servo_min) #1번서보를 펄스길이최소(130)으로 설정.
    pwm.set_pwm(0, 0, servo_min) #0번서로를 펄스길이최소(130)으로 설정.
    time.sleep(1) # 1초정지.
    pwm.set_pwm(1, 0, servo_mid)
    pwm.set_pwm(0, 0, servo_mid)
    time.sleep(1)
    pwm.set_pwm(1, 0, servo_max)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(1, 0, servo_mid)
    pwm.set_pwm(0, 0, servo_mid)
    time.sleep(1)
	