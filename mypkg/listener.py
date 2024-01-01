# SPDX-FileCopyrightText: 2023 Yuta Sekino
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray

def cb(msg):
    global node
    n1, n2 = msg.data
    node.get_logger().info("Listen : %d,%d,%d" % (n1, n2))


rclpy.init()
node = Node("listener")
sub = node.create_subscription(Int16MultiArray, "countup", cb, 10)
rclpy.spin(node)
