import smbus
import time
import math

PCA9685_MODE1 = 0x0
PCA9685_PRESCALE = 0xFE


class PWMDriver:

  def __init__(self, bus):
    self._i2caddr = 0x40
    self.bus = bus

  def begin(self) :
    global PCA9685_MODE1
    global PCA9685_PRESCALE

    self.reset()
    self.setPWMFreq(1500)


  def reset(self) :
    self.write8(PCA9685_MODE1, 0x0)
    

  def setPWMFreq(self, freq) :
    #Serial.print("Attempting to set freq ")
    #Serial.println(freq)
    freq *= 0.9  # Correct for overshoot in the frequency setting (see issue #11).
    self.prescaleval = 25000000
    self.prescaleval /= 4096
    self.prescaleval /= freq
    self.prescaleval -= 1
    #Serial.print("Estimated pre-scale: ") Serial.println(prescaleval)
     
    self.prescale = int(math.floor(self.prescaleval + 0.5))
    #Serial.print("Final pre-scale: ") Serial.println(prescale)
     
    
    self.oldmode = self.read8(PCA9685_MODE1)
    self.newmode = (self.oldmode&0x7F) | 0x10 # sleep
    self.write8(PCA9685_MODE1, self.newmode) # go to sleep
    self.write8(PCA9685_PRESCALE, self.prescale) # set the prescaler
    self.write8(PCA9685_MODE1, self.oldmode)
    time.sleep(.005)
    self.write8(PCA9685_MODE1, self.oldmode | 0xa1)  #  This sets the MODE1 register to turn on auto increment.
                                            # This is why the beginTransmission below was not working.
    #  Serial.print("Mode now 0x") Serial.println(read8(PCA9685_MODE1), HEX)
   

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
    """
    WIRE.beginTransmission(_i2caddr)
    WIRE.write(addr)
    WIRE.endTransmission()

    WIRE.requestFrom((uint8_t)_i2caddr, (uint8_t)1)
    return WIRE.read()
    """
    return self.bus.read_byte_data(self._i2caddr, addr)

  def write8(self, addr, d):
    """
    WIRE.beginTransmission(_i2caddr)
    WIRE.write(addr)
    WIRE.write(d)
    WIRE.endTransmission()
    """
    self.bus.write_byte_data(self._i2caddr, addr, d)

pwmdriver = PWMDriver(smbus.SMBus(1))
pwmdriver.begin()

while True:
  print("Set pins forward")
  for i in range(0,16):
    pwmdriver.setPin(i, 3072)
  time.sleep(2)
  print("Set pins backwards")
  for i in range(0, 16):
    pwmdriver.setPin(i, 1024)
  time.sleep(2)

