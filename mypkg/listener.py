import rclpy
from rclpy.node import Node
from color_msgs.msg import Color

def cb(msg):
    global node
    node.get_logger().info("Listenaaa: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Color, "color", cb, 10)

rclpy.spin(node)