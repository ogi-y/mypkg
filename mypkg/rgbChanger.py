# SPDX-FileCopyrightText: 2022 Yoshihiro Ogishima
# SPDX-Licende-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from color_msgs.srv import Query

def cb(request, response):
   if request.red < 16:
      r = "0" + str(format(request.red, 'x'))
   else:
      r = str(format(request.red, 'x'))
   if request.green < 16:
      g = "0" + str(format(request.green, 'x'))
   else:
      g = str(format(request.green, 'x'))
   if request.blue < 16:
      b = "0" + str(format(request.blue, 'x'))
   else:
      b = str(format(request.blue, 'x'))
   response.color_code = r + g + b
   
   return response

def main():
   rclpy.init()
   node = Node("changer")
   srv = node.create_service(Query, "query", cb) 
   rclpy.spin(node)

if __name__ == '__main__':
   main()