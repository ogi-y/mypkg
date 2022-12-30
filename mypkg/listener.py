# SPDX-FileCopyrightText: 2022 Yoshihiro Ogishima
# SPDX-Licende-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from color_msgs.msg import Color

def cb(msg):
    global node
    node.get_logger().info("Listen Red:%d Green:%d Blue:%d" f" 色\033[48;2;{msg.red};{msg.green};{msg.blue}m     \033[0m" % (msg.red, msg.green, msg.blue))
    


def main():
    rclpy.init()
    global node
    node = Node("listener")
    pub = node.create_subscription(Color, "color", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()