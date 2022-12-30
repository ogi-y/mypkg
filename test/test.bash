#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

export CMAKE_PREFIX_PATH=/opt/ros/humble/share/ament_cmake/
cd $dir/ros2_ws
ls ./src/ -l
ls ./src/color_msgs/ -l
ls ./src/mypkg/ -l
cat ./src/color_msgs/package.xml
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log #|
#grep 'Listen.*Red:.*Green:.*Blue:.*色'
timeout 3 ros2 launch mypkg rgbChange_service.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log #|
#grep 'ColorCode:'
