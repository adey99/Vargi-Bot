# CMake generated Testfile for 
# Source directory: /home/arunava/ws_moveit/src/vb_simulation_pkgs/universal_robot/ur10_moveit_config
# Build directory: /home/arunava/ws_moveit/build/ur10_moveit_config
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_ur10_moveit_config_roslaunch-check_tests_moveit_planning_execution.xml "/home/arunava/ws_moveit/build/ur10_moveit_config/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/arunava/ws_moveit/build/ur10_moveit_config/test_results/ur10_moveit_config/roslaunch-check_tests_moveit_planning_execution.xml.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/arunava/ws_moveit/build/ur10_moveit_config/test_results/ur10_moveit_config" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/arunava/ws_moveit/build/ur10_moveit_config/test_results/ur10_moveit_config/roslaunch-check_tests_moveit_planning_execution.xml.xml\" \"/home/arunava/ws_moveit/src/vb_simulation_pkgs/universal_robot/ur10_moveit_config/tests/moveit_planning_execution.xml\" ")
subdirs("gtest")
