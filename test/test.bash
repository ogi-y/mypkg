#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

echo "source /opt/ros/humble/setup.bash" >> $dir/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> $dir/.bashrc
echo "source ~/ros2_ws/install/local_setup.bash" >> $dir/.bashrc
cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen.*Red:.*Green:.*Blue:.*色'
