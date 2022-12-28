import rclpy
from rclpy.node import Node
from color_msgs.msg import Color

class Talker():
   def __init__(self, node):
      self.pub = node.create_publisher(Color, "color", 10)
      self.n = 0
      node.create_timer(0.5, self.cb)

   def cb(self):
      msg = Color()
      msg.red = 0
      msg.green = 0
      msg.blue = 0
      msg.color_code = "000000"
      self.pub.publish(msg)
      self.n += 2

def main():
   rclpy.init()
   node = Node("talker")
   talker = Talker(node)   
   rclpy.spin(node)

if __name__ == '__main__':
   main()