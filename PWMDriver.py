import smbus
import time
import math
import RPi.GPIO as gpio


class PWMDriver:

  FREQUENCY = 100

  PRESCALE          = 0xFE
  RA_MODE1          = 0x00
  RA_MODE2          = 0x01
  RA_LED0_ON_L      = 0x06
  RA_LED0_ON_H      = 0x07
  RA_LED0_OFF_L     = 0x08
  RA_LED0_OFF_H     = 0x09
  RA_ALL_LED_ON_L   = 0xFA
  RA_ALL_LED_ON_H   = 0xFB
  RA_ALL_LED_OFF_L  = 0xFC
  RA_ALL_LED_OFF_H  = 0xFD

  MODE1_RESTART_BIT = (1 << 7)
  MODE1_EXTCLK_BIT  = (1 << 6)
  MODE1_AI_BIT      = (1 << 5)
  MODE1_SLEEP_BIT   = (1 << 4)
  MODE1_SUB1_BIT    = (1 << 3)
  MODE1_SUB2_BIT    = (1 << 2)
  MODE1_SUB3_BIT    = (1 << 1)
  MODE1_ALLCALL_BIT = (1 << 0)
  ALL_LED_OFF_H_SHUT = (1 << 4)
  MODE2_INVRT_BIT   = (1 << 4)
  MODE2_OCH_BIT     = (1 << 3)
  MODE2_OUTDRV_BIT  = (1 << 2)
  MODE2_OUTNE1_BIT  = (1 << 1)
  MODE2_OUTNE0_BIT  = (1 << 0)
  
  def __init__(self, bus, addr=0x40):
    self._i2caddr = addr
    self.bus = bus
    self.reset()
    self.setPWMFreq(self.FREQUENCY)

    gpio.setmode(gpio.BCM)
    gpio.setup(27, gpio.OUT)
    


  def reset(self) :
    self.write8(self.RA_MODE1, 0x0)
    

  def setPWMFreq(self, freq) :
    print "Attempting to set freq ", freq
    self.prescaleval = int(math.ceil(24576000 / (4096 * freq))) - 1
    print "Final pre-scale: " , self.prescaleval

    self.write8(self.RA_ALL_LED_OFF_H, self.ALL_LED_OFF_H_SHUT) # shutdown before sleeping
    self.write8(self.RA_MODE1, self.MODE1_SLEEP_BIT) # go to sleep
    self.write8(self.PRESCALE, self.prescaleval) # set the prescaler
    #self.write8(self.RA_MODE1, self.MODE1_SLEEP_BIT | self.MODE1_EXTCLK_BIT)
    self.write8(self.RA_MODE1, self.MODE1_RESTART_BIT | self.MODE1_AI_BIT)  #  This sets the MODE1 register to turn on auto increment.
    print "Mode now 0x", self.read8(self.RA_MODE1)
   

  def setPWM(self, num, on, off) :
    #Serial.print("Setting PWM ") Serial.print(num) Serial.print(": ") Serial.print(on) Serial.print("->") Serial.println(off)

    register = 0x06+4*num 
    ledout_values = [on&0xFF, on>>8, off&0xFF, off>>8]
    print("Starting values of register {0} are {1}".format(register, self.bus.read_i2c_block_data(self._i2caddr, register)))
    self.bus.write_i2c_block_data(self._i2caddr, register, ledout_values)
    print("Current values of register {0} are {1}".format(register, self.bus.read_i2c_block_data(self._i2caddr, register)))
    print("Set register {0} at address {2} to {1}".format(register, ledout_values, self._i2caddr))
    

  # Sets pin without having to deal with on/off tick placement and properly handles
  # a zero value as completely off.  Optional invert parameter supports inverting
  # the pulse for sinking to ground.  Val should be a value from 0 to 4095 inclusive.
  def setPin(self, num, val, invert=False):
    # Clamp value between 0 and 4095 inclusive.
    val = min(val, 4095)
    if (invert) :
      if (val == 0) :
        # Special value for signal fully on.
        self.setPWM(num, 4096, 0)
       
      elif (val == 4095) :
        # Special value for signal fully off.
        self.setPWM(num, 0, 4096)
       
      else :
        self.setPWM(num, 0, 4095-val)
       
     
    else:
      if (val == 4095):
        # Special value for signal fully on.
        self.setPWM(num, 4096, 0)
       
      elif (val == 0):
        # Special value for signal fully off.
        self.setPWM(num, 0, 4096)
       
      else:
        self.setPWM(num, 0, val)
       
  def read8(self, addr):
    return self.bus.read_byte_data(self._i2caddr, addr)

  def write8(self, addr, d):
    self.bus.write_byte_data(self._i2caddr, addr, d)

pwmdriver = PWMDriver(smbus.SMBus(1))

while True:
  print("Set pins forward")
  for i in range(0,13):
    pwmdriver.setPin(i, 1100)
  time.sleep(2)
  print("Set pins backwards")
  for i in range(0, 13):
    pwmdriver.setPin(i, 300)
  time.sleep(2)

