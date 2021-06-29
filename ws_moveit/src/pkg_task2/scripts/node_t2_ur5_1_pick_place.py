#!/usr/bin/env python
'''
This module makes the UR5 robot to pick a box from the shelf, place it in the bin
and return to it's initial position
'''
from __future__ import print_function

import sys
import rospy

import moveit_commander
from moveit_commander.conversions import pose_to_list

import moveit_msgs.msg
import geometry_msgs.msg
from pkg_vb_sim.srv import vacuumGripper

def all_close(goal, actual, tolerance):
    """
    Convenience method for testing if a list of values are within a tolerance of
    their counterparts in another list
    @param: goal       A list of floats, a Pose or a PoseStamped
    @param: actual     A list of floats, a Pose or a PoseStamped
    @param: tolerance  A float
    @returns: bool
    """
    #all_equal = True
    if isinstance(goal, list):
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif isinstance(goal, geometry_msgs.msg.PoseStamped):
        return all_close(goal.pose, actual.pose, tolerance)

    elif isinstance(goal, geometry_msgs.msg.Pose):
        return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

    return True


class MoveGroupPythonInteface(object):
    """MoveGroupPythonInteface is the class that holds all the required variables and methods
    to control the UR5 robot
    """
    def __init__(self):
        '''
        Constructor for the class MoveGroupPythonInteface.
        Here all the required initializations are done
        '''
        super(MoveGroupPythonInteface, self).__init__()

        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('node_t2_ur5_1_pick_place', anonymous=True)

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to a planning group (group of joints).
        ## This interface can be used to plan and execute motions:
        group_name = "ur5_1_planning_group"
        move_group = moveit_commander.MoveGroupCommander(group_name)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                       moveit_msgs.msg.DisplayTrajectory,
                                                       queue_size=20)

        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)

        # We can also print the name of the end-effector link for this group:
        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)

        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")

        # Misc. variables
        self.box_name = 'box'
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

    def go_to_joint_state(self, j_0, j_1, j_2, j_3, j_4, j_5):
        '''
        This method makes the arm go to provided target joint angles.
        the six joint angles in radians are provided as arguments.
        '''
        move_group = self.move_group

        # We can get the joint values from the group and adjust some of the values:
        joint_goal = move_group.get_current_joint_values()
        joint_goal[0] = j_0
        joint_goal[1] = j_1
        joint_goal[2] = j_2
        joint_goal[3] = j_3
        joint_goal[4] = j_4
        joint_goal[5] = j_5
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()

        # For testing:
        current_joints = move_group.get_current_joint_values()
        return all_close(joint_goal, current_joints, 0.01)

    def wait_for_state_update(self, box_is_known=False, box_is_attached=False, timeout=4):
        '''
        This method ensures all the changes are reflected successfully in the Planning Scene
        '''
        box_name = self.box_name
        scene = self.scene

        ## If the Python node dies before publishing a collision object update message, the message
        ## could get lost and the box will not appear. To ensure that the updates are
        ## made, we wait until we see the changes reflected in the
        ## ``get_attached_objects()`` and ``get_known_object_names()`` lists.
        ## Here, we call this function after adding,
        ## removing, attaching or detaching an object in the planning scene. We then wait
        ## until the updates have been made or ``timeout`` seconds have passed
        start = rospy.get_time()
        seconds = rospy.get_time()
        while (seconds - start < timeout) and not rospy.is_shutdown():
            # Test if the box is in attached objects
            attached_objects = scene.get_attached_objects([box_name])
            is_attached = len(attached_objects.keys()) > 0

            # Test if the box is in the scene.
            # Note that attaching the box will remove it from known_objects
            is_known = box_name in scene.get_known_object_names()

            # Test if we are in the expected state
            if (box_is_attached == is_attached) and (box_is_known == is_known):
                return True

            # Sleep so that we give other threads time on the processor
            rospy.sleep(0.1)
            seconds = rospy.get_time()

        # If we exited the while loop without returning then we timed out
        return False


    def add_box(self, timeout=4):
        '''
        Through this method the box is added to the RViz world.
        The position and dimensions of the box needs to be specified
        '''
        box_name = self.box_name
        scene = self.scene


        ## First, we will add a box in the planning scene:
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "world"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.x = 0.04
        box_pose.pose.position.y = 0.47
        box_pose.pose.position.z = 1.92
        box_name = "box"
        scene.add_box(box_name, box_pose, size=(0.15, 0.15, 0.15))

        self.box_name = box_name
        return self.wait_for_state_update(box_is_known=True, timeout=timeout)


    def attach_box(self, timeout=4):
        '''
        This method makes the box attach to the end effector of the UR5 robot
        '''
        box_name = self.box_name
        robot = self.robot
        scene = self.scene
        eef_link = self.eef_link
        group_names = self.group_names


        ## Next, we will attach the box to the UR5 wrist. Manipulating objects requires the
        ## robot be able to touch them without the planning scene reporting the contact as a
        ## collision. By adding link names to the ``touch_links`` array, we are telling the
        ## planning scene to ignore collisions between those links and the box.
        grasping_group = 'ur5_1_planning_group'
        touch_links = robot.get_link_names(group=grasping_group)
        scene.attach_box(eef_link, box_name, touch_links=touch_links)

        # We wait for the planning scene to update.
        return self.wait_for_state_update(box_is_attached=True, box_is_known=False, timeout=timeout)


    def detach_box(self, timeout=4):
        '''
        This method makes the box detach from the end effector of the UR5 robot
        '''
        box_name = self.box_name
        scene = self.scene
        eef_link = self.eef_link

        ## We detach the object from the UR5:
        scene.remove_attached_object(eef_link, name=box_name)

        # We wait for the planning scene to update.
        return self.wait_for_state_update(box_is_known=True, box_is_attached=False, timeout=timeout)


    def remove_box(self, timeout=4):
        '''
        This method removes the box from RViz world
        '''
        box_name = self.box_name
        scene = self.scene

        ## We can remove the box from the world.
        scene.remove_world_object(box_name)

        ##The object must be detached before we can remove it from the world

        # We wait for the planning scene to update.
        return self.wait_for_state_update(box_is_attached=False, box_is_known=False,
                                          timeout=timeout)


def main():
    '''
    Driver function. In this function the class object is created,
    ROS Service communication is established and required methods are invoked for
    completing the task
    '''
    rospy.wait_for_service('/eyrc/vb/ur5_1/activate_vacuum_gripper')
    try:
        command_ur5 = MoveGroupPythonInteface()

        #Now we create a client object to control vacuum gripper through ROS Service
        vacuum_grip = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper', vacuumGripper)
        command_ur5.add_box()

        #Going to pick the box from the shelf
        command_ur5.go_to_joint_state(0.9773, -1.4486, 0.349, -2.0071, -0.9948, 0.0)
        command_ur5.attach_box()

        #Making the Vacuum Gripper to attach with the box in Gazebo
        result = vacuum_grip(activate_vacuum_gripper=True)
        rospy.loginfo(result)

        #Going to place the box in the Bin
        command_ur5.go_to_joint_state(0.3665, -2.2514, -1.7278, -0.2268, 1.4835, -0.2443)
        command_ur5.detach_box()

        #Detaching the box from the UR5 robot
        result = vacuum_grip(activate_vacuum_gripper=False)
        rospy.loginfo(result)
        command_ur5.remove_box()

        #Going to the 'allZeroes' as the task is finished
        command_ur5.go_to_joint_state(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    except rospy.ROSInterruptException:
        return
    except rospy.ServiceException:
        rospy.loginfo("Service call to Vacuum Gripper failed")
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
