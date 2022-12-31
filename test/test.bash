#!/bin/bash
# SPDX-FileCopyrightText: 2022 Yoshihiro Ogishima
# SPDX-Licende-Identifier: BSD-3-Clause

ng () {
	echo NG at line $1
	res=1
}

res=0

dir=~
[ "$1" != "" ] && dir="$1"

source $dir/.bashrc
cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep "Listen Red:.*Green:.*Blue:.*色" || ng ${LINENO}
timeout 3 ros2 launch mypkg rgbChange_service.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep "R:.*G:.*B.*ColorCode:......" || ng ${LINENO}
[ "$res" = 0 ] && echo OK!
exit $res

