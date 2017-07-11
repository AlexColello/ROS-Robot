#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32

def callback(data):
    x = data.axes[2]
    y = data.axes[3]
    

def pwm_tester():
    
    pub = rospy.Publisher('pwm_tester', Float32, queue_size=10)
    rospy.init_node('pwm_tester', anonymous=True)
    rate = rospy.Rate(.5) # 10hz
    value = .5
    #rospy.Subscriber('joy_node', , callback)
    while not rospy.is_shutdown():
        value *= 1.0
        rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        pwm_tester()
    except rospy.ROSInterruptException:
        pass
