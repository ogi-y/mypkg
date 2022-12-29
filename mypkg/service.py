import rclpy
from rclpy.node import Node
from color_msgs.msg import Color
from color_msgs.srv import Query

def cb(msg):
    global r, g, b
    r = msg.red
    g = msg.green
    b = msg.blue
    node.get_logger().info("Listen Red:%d Green:%d Blue:%d" % (msg.red, msg.green, msg.blue))

def main():
    rclpy.init()
    global node
    global r,g,b
    r = -1
    g = -1
    b = -1
    node = Node("service")
    client = node.create_client(Query, "query")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info("待機中")
    pub = node.create_subscription(Color, "color", cb, 10)
    while b < 0:
        rclpy.spin_once(node)
    req = Query.Request()
    req.red = r
    req.green = g
    req.blue = b
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done(): 
            try:
               response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("ColorCode: %s" % response.color_code)
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()