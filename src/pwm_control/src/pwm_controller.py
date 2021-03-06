#!/usr/bin/env python

import smbus
import time
import math
import RPi.GPIO as gpio
import rospy
from teleoperated_control.msg import DriveSpeeds
from pwm_control.msg import PWMValues

class PWMDriver:

    FREQUENCY = 200.0
    PRESCALE_MODIFIER = 1.05
    #To calculate the length of the pulse, use the formula:
    #Length in ms = 1000 / frequency(hz) * value / 4096
    JAGUAR_MAX_DUTY_CYCLE = 1853 #2.304 ms at 200 hz
    JAGUAR_MIN_DUTY_CYCLE = 560 #0.691 ms at 200 hz
    JAGUAR_MAX_DEADBAND = 1247 #1.551 ms at 200 hz
    JAGUAR_MIN_DEADBAND = 1165 #1.448 ms at 200 hz


    PRESCALE          = 0xFE
    RA_MODE1          = 0x00
    RA_ALL_LED_OFF_H  = 0xFD

    MODE1_RESTART_BIT = (1 << 7)
    MODE1_EXTCLK_BIT  = (1 << 6)
    MODE1_AI_BIT      = (1 << 5)
    MODE1_SLEEP_BIT   = (1 << 4)
    ALL_LED_OFF_H_SHUT = (1 << 4)

    def __init__(self, bus=smbus.SMBus(1), addr=0x40):
          self._i2caddr = addr
          self.bus = bus

          #gpio.setmode(gpio.BCM)
          #gpio.setup(27, gpio.OUT)

    def set_pwm_freq(self, freq) :
          print "Attempting to set freq ", freq
          self.prescaleval = int(math.ceil(25000000.0 * self.PRESCALE_MODIFIER / (4096.0 * freq))) - 1
          print "Final pre-scale: " , self.prescaleval
          
          self.write8(self.RA_ALL_LED_OFF_H, self.ALL_LED_OFF_H_SHUT) # shutdown before sleeping
          self.write8(self.RA_MODE1, self.MODE1_SLEEP_BIT) # go to sleep
          self.write8(self.PRESCALE, self.prescaleval) # set the prescaler
          self.write8(self.RA_MODE1, self.MODE1_RESTART_BIT | self.MODE1_AI_BIT)  #  This sets the MODE1 register to turn on auto increment.
          print "Mode now 0x", self.read8(self.RA_MODE1)

    def set_pwm(self, num, on, off) :
          #Serial.print("Setting PWM ") Serial.print(num) Serial.print(": ") Serial.print(on) Serial.print("->") Serial.println(off)

          register = 0x06+4*(num + 3)
          ledout_values = [on&0xFF, on>>8, off&0xFF, off>>8]
          #print("Starting values of register {0} are {1}".format(register, self.bus.read_i2c_block_data(self._i2caddr, register)))
          self.bus.write_i2c_block_data(self._i2caddr, register, ledout_values)
          #print("Current values of register {0} are {1}".format(register, self.bus.read_i2c_block_data(self._i2caddr, register)))
          print("Set register {0} at address {2} to {1}".format(register, ledout_values, self._i2caddr))


          # Sets pin without having to deal with on/off tick placement and properly handles
          # a zero value as completely off.  Optional invert parameter supports inverting
          # the pulse for sinking to ground.  Val should be a value from 0 to 4095 inclusive.
    def set_pin_raw(self, num, val, invert=False):
          # Clamp value between 0 and 4095 inclusive.
          val = min(val, 4095)
          if invert :
              if val == 0 :
                  # Special value for signal fully on.
                  self.set_pwm(num, 4096, 0)
                  
              elif val == 4095 :
                  # Special value for signal fully off.
                  self.set_pwm(num, 0, 4096)

              else :
                  self.set_pwm(num, 0, 4095-val)


          else:
              if val == 4095:
                  # Special value for signal fully on.
                  self.set_pwm(num, 4096, 0)
                  
              elif val == 0:
                  # Special value for signal fully off.
                  self.set_pwm(num, 0, 4096)
                  
              else:
                  self.set_pwm(num, 0, val)
                  
    def set_pin(self, num, val):
            if val >= 1.0:
                self.set_pin_raw(num, self.JAGUAR_MAX_DUTY_CYCLE)
            elif val <= -1.0:
                self.set_pin_raw(num, self.JAGUAR_MIN_DUTY_CYCLE)
            else:
                duty_cycle_range = self.JAGUAR_MAX_DUTY_CYCLE - self.JAGUAR_MIN_DUTY_CYCLE
                middle_duty_cycle = duty_cycle_range / 2 + self.JAGUAR_MIN_DUTY_CYCLE
                val = round(val * duty_cycle_range / 2 + middle_duty_cycle)
                self.set_pin_raw(num, int(val))

    def read8(self, addr):
        return self.bus.read_byte_data(self._i2caddr, addr)

    def write8(self, addr, d):
        self.bus.write_byte_data(self._i2caddr, addr, d)

    def callback(self, data):
        for i in range(0,12):
            rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.outputs[i])
            self.set_pin(i, data.outputs[i])
        
def pwm_control():
    pwmdriver = PWMDriver()
    rospy.init_node('pwm_control')
    pwmdriver.set_pwm_freq(pwmdriver.FREQUENCY)
    rospy.Subscriber("pwm_control", PWMValues, pwmdriver.callback)
    rospy.spin()

if __name__ == '__main__':
    pwm_control()
                                                                    
