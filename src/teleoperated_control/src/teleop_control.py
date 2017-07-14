#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from teleoperated_control.msg import DriveSpeeds

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
                rightMotorSpeed = max(moveValue, rotateValue)
            else:
                leftMotorSpeed = max(moveValue, -rotateValue)
                rightMotorSpeed = moveValue + rotateValue
        else:
            if rotateValue > 0.0:
                leftMotorSpeed = -max(-moveValue, rotateValue)
                rightMotorSpeed = moveValue + rotateValue
            else:
                leftMotorSpeed = moveValue - rotateValue
                rightMotorSpeed = -max(-moveValue, -rotateValue)

        return leftMotorSpeed, rightMotorSpeed


    def callback(self, data):
        x = data.axes[2]
        y = data.axes[3]
        left_motor, right_motor = self.calc_arcade_drive(y, x)
        self.pub.publish(left_motor, right_motor)

    def __init__(self):
        self.pub = rospy.Publisher('teleop_control', DriveSpeeds, queue_size=10)
        rospy.init_node('teleop_control')
        rospy.Subscriber('joy', Joy, self.callback)
        self.pub.publish(0.0,0.0)
        rospy.spin()

if __name__ == '__main__':
    try:
        teleop_drive = TeleopDrive()
    except rospy.ROSInterruptException:
        pass
