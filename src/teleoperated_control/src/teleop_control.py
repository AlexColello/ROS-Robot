#!/usr/bin/env python

import rospy
from sensor_msgs import Joy
from std_msgs.msg import Float32MultiArray

class TeleopDrive:
        
    def calc_arcade_drive(self, moveValue, rotateValue):

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


    def callback(self,data):
        x = data.axes[2]
        y = data.axes[3]
        left_motor, right_motor = calc_arcade_drive(y, x)
        self.pub.publish([left_motor, right_motor, 0,0,0,0,0,0,0,0,0,0,0])

    def __init__(self):
        self.pub = rospy.Publisher('pwm_tester', Float32MultiArray, queue_size=10)
        rospy.init_node('pwm_tester', anonymous=True)
        rospy.Subscriber('joy_node', Joy, callback)
        self.pub.publish([0,0,0,0,0,0,0,0,0,0,0,0,0])
        rospy.spin()

if __name__ == '__main__':
    try:
        teleop_drive = TeleopDrive()
    except rospy.ROSInterruptException:
        pass
