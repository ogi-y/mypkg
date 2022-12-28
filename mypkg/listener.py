import rclpy
from rclpy.node import Node
from color_msgs.msg import Color

def cb(msg):
    node.get_logger().info("Listen: %s" % msg.color_code)

def main():
    rclpy.init()
    global node
    node = Node("listener")
    pub = node.create_subscription(Color, "color", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()