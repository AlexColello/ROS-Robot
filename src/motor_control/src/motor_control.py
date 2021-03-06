#!/usr/bin/env python

from teleoperated_control.msg import DriveSpeeds
from pwm_control.msg import PWMValues
import rospy

class MotorController:

    def callback(self, data):
        output = [0.0]*12
        output[0], output[1] = data.left_speed, -data.right_speed
        self.pub.publish(output)
        
    def __init__(self):
        self.pub = rospy.Publisher('pwm_control', PWMValues, queue_size=10)
        rospy.init_node('motor_control')
        rospy.Subscriber('teleop_control', DriveSpeeds, self.callback)
        self.pub.publish([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
        rospy.spin()

if __name__ == '__main__':
    motor_control = MotorController()
