#!/usr/bin/env python
"""**********MODULE DOCSTRING************
Name: node_turtle_revolve

Objective: This script moves the turtle in a circular path for one complete revolution
            by publishing appropriate linear and angular velocity

Functions: pose_callback,get_current_pos,main
**************************************"""
#Importing the required modules
import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
    """**************FUNCTION DOCSTRING*********
    Name: pose_callback

    Objective: This function checks if the turtle has reached it's initial position
                after completing one revolution

    Argument: msg, i.e the message object published to turtlesim

    Returns: None
    ***************************************"""
    if msg.theta > -0.03 and msg.theta < 0.0:  #Condition for stopping the turtle movement
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        val_pub = Twist()
        val_pub.linear.x = 0.0
        val_pub.linear.y = 0.0
        val_pub.angular.z = 1.0
        velocity_publisher.publish(val_pub)
        rospy.signal_shutdown('finished')

def get_current_pos(msg):
    """**************FUNCTION DOCSTRING*********
    Name: get_current_pos

    Objective: This function prints distance travelled by the turtle from angular displacement

    Argument: msg, i.e the object published to turtlesim

    Returns: None
    **************************************"""
    if msg.theta >= 0:
        rospy.loginfo('Moving in a circle\n'+str(msg.theta))
    else:
        #This takes care of the negative theta
        rospy.loginfo('Moving in a circle\n'+str(2*math.pi+msg.theta))

def main():
    """**************FUNCTION DOCSTRING*********
    Name: main

    Objective: This function initializes the node,publisher,subscriber etc., controls
                the rate of publishing and the message to be published to the topics

    Argument: None

    Returns: None
    *****************************************"""
    #Initializing the node
    rospy.init_node('node_turtle_revolve', anonymous=True)
    #Initializing the publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #Calling get_current_pos to get current position of turtle
    rospy.Subscriber("/turtle1/pose", Pose, get_current_pos)
    rate = rospy.Rate(10)      #Setting the rate of publishing i.e 10Hz
    while not rospy.is_shutdown():
        vel_msg = Twist()  #Creating an Instance of Twist class of geometry_msgs.msg
        #Assigning linear and angular velocity
        vel_msg.linear.x = 1.0
        vel_msg.linear.y = 0.0
        vel_msg.angular.z = 1.0
        velocity_publisher.publish(vel_msg) #Publishing the velocities to the turtle
        #pose_callback is called to check if it has reached it's initial point
        rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        #This will raise ROSInterruptedException if the sleep is interrupted by shutdown
        rate.sleep()
    rospy.loginfo('goal reached')   #prints the status that turtle has completed it's revolution

if __name__ == '__main__':
    try:
        main() #Driver function is called
    except rospy.ROSInterruptException:  #exception caught for rospy shutdown
        pass
