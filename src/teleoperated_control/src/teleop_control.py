#!/usr/bin/env python

import rospy
from sensor_msgs import Joy
from std_msgs.msg import Float32

def calc_arcade_drive(moveValue, rotateValue):
    
    #square the inputs (while preserving the sign) to increase fine
    #control
    if moveValue >= 0.0:
        moveValue = moveValue * moveValue
    else:
        moveValue = -(moveValue * moveValue)
    
    if rotateValue >= 0.0:
        rotateValue = rotateValue * rotateValue
    else:
        rotateValue = -(rotateValue * rotateValue)

    if moveValue > 0.0:
        if rotateValue > 0.0:
            leftMotorSpeed = moveValue - rotateValue
            rightMotorSpeed = Math.max(moveValue, rotateValue)
        else:
            leftMotorSpeed = Math.max(moveValue, -rotateValue)
            rightMotorSpeed = moveValue + rotateValue
    else:
        if rotateValue > 0.0:
            leftMotorSpeed = -Math.max(-moveValue, rotateValue)
            rightMotorSpeed = moveValue + rotateValue
        else:
            leftMotorSpeed = moveValue - rotateValue
            rightMotorSpeed = -Math.max(-moveValue, -rotateValue)
            
    return leftMotorSpeed, rightMotorSpeed
        

def callback(data):
    x = data.axes[2]
    y = data.axes[3]
    left_motor, right_motor = calc_arcade_drive(y, x)

def teleop_control():
    
    pub = rospy.Publisher('pwm_tester', Float32, queue_size=10)
    rospy.init_node('pwm_tester', anonymous=True)
    rate = rospy.Rate(100) # 100hz
    value = .5
    rospy.Subscriber('joy_node', Joy, callback)
    while not rospy.is_shutdown():
        value *= 1.0
        rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        teleop_control()
    except rospy.ROSInterruptException:
        pass
