# SPDX-FileCopyrightText: 2023 Yuta Sekino
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Int16: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
