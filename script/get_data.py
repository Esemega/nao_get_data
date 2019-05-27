#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('get_data', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "Robot Groups:", robot.get_group_names()
print ""
print "These are all available groups of the robot."
print "From which one you need information?"
group_name = raw_input()
#group_name = "right_arm"
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher(
    '/move_group/display_planned_path',
    moveit_msgs.msg.DisplayTrajectory, queue_size=1)
# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print "Reference frame of group:" + group_name
print "%s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print "End effector of group:" + group_name
print "%s" % eef_link

#You can get the current values of the joints, like this:
print "Current Joint Values of group:" + group_name
print group.get_current_joint_values()
#You can also get the current Pose of the end-effector of the robot, like this:
print "Current Pose of group " + group_name + ":", group.get_current_pose()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "Printing robot state"
print robot.get_current_state()
print ""

moveit_commander.roscpp_shutdown()
