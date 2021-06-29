#!/usr/bin/env python

'''**************MODULE DOCSTRING*******************
ROS Node - Simple Action Server - Turtle

Objective: This module drives the turtle upon receiving goals from IOT Action Client

Class: SimpleActionServerTurtle

Functions: main
****************************************************'''

import math
import rospy
import actionlib

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

from pkg_task1.msg import msgTurtleAction     # Message Class that is used by ROS Actions internally
from pkg_task1.msg import msgTurtleResult     # Message Class that is used for Result messages
from pkg_task1.msg import msgTurtleFeedback   # Message Class that is used for Feedback messages


class SimpleActionServerTurtle(object):
    '''*********************CLASS DOCSTRING*************
    Name: SimpleActionServerTurtle

    Methods: func_ros_sub_callback, func_move_straight,
                func_rotate, func_on_rx_goal
    ****************************************************'''
    # Constructor
    def __init__(self):
        '''
        * '/action_turtle' - The name of the action that will be used by ROS Nodes
            to communicate with this Simple Action Server.
        * msgTurtleAction - The Message Class that is used by ROS Actions
            internally for this Simple Action Server
        * execute_cb - Holds the function pointer to the function which will
            process incoming Goals from Simple Action Clients.
        * auto_start = False - Only when self._sas.start() will be called
            then only this Simple Action Server will start.
        '''
        # Initializing Simple Action Server
        self._sas = actionlib.SimpleActionServer('/action_turtle',
                                                 msgTurtleAction,
                                                 execute_cb=self.func_on_rx_goal,
                                                 auto_start=False)

        # Declaring constants
        self._config_ros_pub_topic = '/turtle1/cmd_vel'
        self._config_ros_sub_topic = '/turtle1/pose'

        # Declare variables
        self._curr_x = 0
        self._curr_y = 0
        self._curr_theta = 0

        # Start the Action Server
        self._sas.start()
        rospy.loginfo("Started Turtle Simple Action Server.")

    def func_ros_sub_callback(self, pose_message):
        '''*****************METHOD DOCSTRING***************************
        Name: func_ros_sub_callback

        Objective: Callback Function for ROS Topic ('/turtle1/pose') Subscription

        Arguments: Message containing the position coordinates of turtle

        Returns: None
        ***************************************************************'''
        self._curr_x = pose_message.x
        self._curr_y = pose_message.y
        self._curr_theta = pose_message.theta

    #-------------------------------------------------------
    # Function to move the turtle in turtlesim_node straight
    def func_move_straight(self, param_dis, param_speed, param_dir):
        '''**************************METHOD DOCSTRING***********************************
        Name: func_move_straight

        Objective: Function to move the turtle in turtlesim_node straight
                    as per the received goal

        Arguments: distance, speed, direction(forward/backward)

        Returns: None
        ********************************************************************************'''
        obj_velocity_mssg = Twist()

        # Storing the start position of the turtle
        start_x = self._curr_x
        start_y = self._curr_y

        # Move the turtle till it reaches the desired position by publishing to Velocity topic
        handle_pub_vel = rospy.Publisher(self._config_ros_pub_topic, Twist, queue_size=10)

        # 10 Hz : Loop will its best to run 10 times in 1 second
        var_loop_rate = rospy.Rate(10)

        # Set the Speed of the Turtle according to the direction
        if param_dir == 'b':
            obj_velocity_mssg.linear.x = (-1) * abs(int(param_speed))
        else:
            obj_velocity_mssg.linear.x = abs(int(param_speed))

        # Move till desired distance is covered
        dis_moved = 0.0

        while not rospy.is_shutdown():

            # Send feedback to the client
            obj_msg_feedback = msgTurtleFeedback()

            obj_msg_feedback.cur_x = self._curr_x
            obj_msg_feedback.cur_y = self._curr_y
            obj_msg_feedback.cur_theta = self._curr_theta

            self._sas.publish_feedback(obj_msg_feedback)

            if dis_moved < param_dis:
                handle_pub_vel.publish(obj_velocity_mssg)

                var_loop_rate.sleep()

                dis_moved = abs(
                    math.sqrt(((self._curr_x - start_x) ** 2) + ((self._curr_y - start_y) ** 2)))
                print 'Distance Moved: {}'.format(dis_moved)
            else:
                break

        # Stop the Turtle after desired distance is covered
        obj_velocity_mssg.linear.x = 0
        handle_pub_vel.publish(obj_velocity_mssg)
        print 'Destination Reached'

    def func_rotate(self, param_degree, param_speed, param_dir):
        '''***********************METHOD DOCSTRING*********************************
        Name: func_rotate

        Objective: Function to rotate the turtle in turtlesim_node as
                    per the goal received

        Arguments: angle in degrees, speed, direction of rotation

        Returns: None
        ***************************************************************************'''
        obj_velocity_mssg = Twist()

        # Store start Theta of the turtle
        start_degree = abs(math.degrees(self._curr_theta))
        current_degree = abs(math.degrees(self._curr_theta))

        # Rotate the turtle till desired angle is reached
        handle_pub_vel = rospy.Publisher(
            self._config_ros_pub_topic, Twist, queue_size=10)

        # 10 Hz : Loop will its best to run 10 times in 1 second
        var_loop_rate = rospy.Rate(10)

        # Set the speed of rotation according to param_dir
        if param_dir == 'a':
            obj_velocity_mssg.angular.z = math.radians(
                abs(int(param_speed)))  # Anticlockwise
        else:
            # Clockwise
            obj_velocity_mssg.angular.z = (-1) * \
                math.radians(abs(int(param_speed)))

        # Rotate till desired angle is reached
        degree_rotated = 0.0

        while not rospy.is_shutdown():
            if round(degree_rotated) < param_degree:
                handle_pub_vel.publish(obj_velocity_mssg)

                var_loop_rate.sleep()

                current_degree = abs(math.degrees(self._curr_theta))
                degree_rotated = abs(current_degree - start_degree)
                print 'Degree Rotated: {}'.format(degree_rotated)
            else:
                break

        # Stop the Turtle after the desired angle is reached
        obj_velocity_mssg.angular.z = 0
        handle_pub_vel.publish(obj_velocity_mssg)
        print 'Angle Reached'

    def func_on_rx_goal(self, obj_msg_goal):
        '''*************METHOD DOCSTRING**************************
        Name: func_on_rx_goal

        Objective: Function to process Goals and send Results

        Arguments: goal message

        Returns: None
        **********************************************************'''
        rospy.loginfo("Received a Goal from Client.")
        rospy.loginfo(obj_msg_goal)

        # --- Goal Processing Section ---
        self.func_rotate(obj_msg_goal.angle, '10', 'a')
        self.func_move_straight(obj_msg_goal.distance, '1', 'f')

        # Send Result to the Client
        obj_msg_result = msgTurtleResult()
        obj_msg_result.final_x = self._curr_x
        obj_msg_result.final_y = self._curr_y
        obj_msg_result.final_theta = self._curr_theta

        rospy.loginfo("send goal result to client")
        self._sas.set_succeeded(obj_msg_result)

def main():
    '''*******************FUNCTION DOCSTRING*********************
    Name: main

    Objective: Driver function. this function creates an object
                and calls respective functions for moving the Turtle

    Arguments: None

    Returns: None
    ************************************************************'''
    # Initializing ROS Node
    rospy.init_node('node_simple_action_server_turtle')

    # Creating Simple Action Server object.
    obj_server = SimpleActionServerTurtle()

    # Subscribing to Pose of the Turtle
    rospy.Subscriber('/turtle1/pose', Pose, obj_server.func_ros_sub_callback)

    # Do not exit and loop forever.
    rospy.spin()


if __name__ == '__main__':
    main()
