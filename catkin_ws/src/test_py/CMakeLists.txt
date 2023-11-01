




cmake_minimum_required(VERSION 3.0.2)
project(test_py)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime sensor_msgs
)

include_directories(

  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/simple_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
