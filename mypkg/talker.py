# SPDX-FileCopyrightText: 2022 Yoshihiro Ogishima
# SPDX-Licende-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from color_msgs.msg import Color
import random

class Talker():
   def __init__(self, node):
      self.pub = node.create_publisher(Color, "color", 10)
      self.n = 0
      node.create_timer(0.5, self.cb)

   def cb(self):
      msg = Color()
      msg.red = random.randint(0, 255)
      msg.green = random.randint(0, 255)
      msg.blue = random.randint(0, 255)
      self.pub.publish(msg)
      self.n += 1

def main():
   rclpy.init()
   node = Node("talker")
   talker = Talker(node)   
   rclpy.spin(node)

if __name__ == '__main__':
   main()