# SPDX-FileCopyrightText: 2022 Yoshihiro Ogishima
# SPDX-Licende-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        )
    changer = launch_ros.actions.Node(
        package='mypkg',
        executable='changer',
        )
    service = launch_ros.actions.Node(
        package='mypkg',
        executable='service',
        output='screen'
        )

    return launch.LaunchDescription([talker, changer, service])