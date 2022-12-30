#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
ls -l
ls ./src/ -l
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log #|
#grep 'Listen.*Red:.*Green:.*Blue:.*色'
timeout 3 ros2 launch mypkg rgbChange_service.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log #|
#grep 'ColorCode:'
